#helper functions
import time
import os
from random import randint, choice
import subprocess
import platform
import random
import constants as c
import pages as p
import classes as o
import helpers as h
import dictionary as d

def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

def weighted_choice(dict):
    items=[]
    weights=[]
    for key, value in dict.items() :
        items.append(key)
        weights.append(value)

    chosen = random.choices(items, weights, k=1)
    return chosen

        
def draw_grid(g, width=2):
    for y in range(g.height):  
        for x in range(g.width):
            if (x, y) in g.walls:
                symbol = '█'
            elif (x, y) == g.player:
                symbol = 'O'
            elif (x, y) == g.chest.pos and g.chest.show == True:
                symbol = '□'
            elif (x, y) == g.enemy.pos and g.enemy.alive == True:
                symbol = '♛'
            elif (x, y) == g.start:
                symbol = '<'
            elif (x, y) == g.goal:
                symbol = '>'
            else:
                symbol = ' '
            print("%%-%ds" % width % symbol, end="")
        print()
        
def get_walls(g: o.MapGrid, pct=.25) -> list:
        out = []
        for i in range(int(g.height*g.width*pct)//2):

            x = randint(2, g.width-3)
            y = randint(2, g.height-3)

            out.append((x, y))
            out.append((x + choice([-1, 0, 1]), y + choice([-1, 0, 1])))

        for y in range(g.height):
            for x in range(g.width):
                if (x, y) == (0,y):
                    out.append((x,y))
                elif (x, y) == (x,0):
                    out.append((x,y))
                elif (x, y) == (x,g.width-1):
                    out.append((x,y))
                elif (x, y) == (g.height-1,y):
                    out.append((x,y))
        return out
    
def gen_level(curr_stage, max_stage):
    g = o.MapGrid(c.map_size, c.map_size)
    g.walls = get_walls(g)

    while g.player != g.goal:
        h.draw_grid(g)
        d = input()
        if(d == 'w' or d == 'a' or d == 's' or d == 'd'):
            g.move_player(d)
            g.move_enemy()
        if(d == 'e'):
            inventory()
            inv_sel = input('Selected Item:')
            index=0
            for x in c.items:
                if(inv_sel == str(index+1)):
                    print('You selected the '+ c.items[index])
                index+=1
            input()
        h.clear_screen()
        if(g.battle_radius() == True and g.enemy.alive == True):
            battle(g.enemy)
        if(g.chest_radius() == True and g.chest.show == True):
            chest_open()
            g.chest.show = False
            input()
    h.clear_screen()
    if(curr_stage == max_stage):
        p.winner()
    else:
        p.level_complete()
        c.level+=1

def chest_open():
    chest_drop = weighted_choice(d.chest_drop_chances)[0]
    print('You Have oped a chest. You received a ['+ chest_drop+']')
    c.items.append(chest_drop)

def inventory():
    p.inventory(c.items)

def battle(enemy_alive):
    player = o.Player()
    enemy = o.Enemy()
    while enemy.hp > 0 and player.hp > 0:
        print("Commence Battle!")
        print("Lvl: "+ str(player.lvl)+ "                                               Enemy LVL: "+ str(enemy.lvl))
        print("Exp: "+ str(player.exp))
        print("HP: "+ str(player.hp)+ "                                               Enemy HP: "+ str(enemy.hp))
        p.battle_page()
        print('(1) ' + player.attacks[0])
        print('(2) ' + player.attacks[1])
        print('(3) ' + player.attacks[2])
        attack = input()
        enemy.damaged(int(player.attack(attack)))
        player.damaged(enemy.attack())
        h.clear_screen()
    if(player.hp <= 0):
        print('YOU DIED')
        p.lose()
    else:
        print('YOU VANQUISHED THE ENEMY!')
        enemy_alive.alive = False
        player.level_up()
        input('press button to continue...')
        h.clear_screen()
