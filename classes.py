from random import randint, choice
import subprocess
import platform
import random
import constants as c

class Enemy_Object():
    def __init__(self, pos, alive):
        self.pos = pos
        self.alive = alive

class Chest:
    def __init__(self, pos, show):
        self.pos = pos
        self.show = show
        self.items = ['potion']
        
class Equipment:
        def __init__(self):
            self.name = h.weighted_chest_choice()
            self.health = 0
            self.attack = 0
        def use_item():
            print("used item"+ self.name)
        

class Player:
    def __init__(self):
        self.hp = c.health
        self.exp = 0
        self.lvl = 1
        self.attacks = ['slash', 'stab', 'smash']
    def level_up(self):
        self.hp += 20
        self.lvl += 1
        print('LEVELED UP TO LVL ' + str(self.lvl))
    def damaged(self, lost_hp):
        self.hp -= lost_hp
    def attack(self, user_input):
        switcher = {
            '1': 5,
            '2': 10,
            '3': 20,
        }
        return switcher.get(user_input, 0)

class Enemy:
    def __init__(self):
        self.hp = c.level * 100
        self.lvl = c.level
        self.attacks = ['a', 'b', 'c']
    def damaged(self, lost_hp):
        self.hp -= int(lost_hp)
    def attack(self):
        return 10
    
        
class MapGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []
        self.chest = Chest((2,3), True)
        self.start = (1, 1)
        self.goal = (width-2, height-2)
        self.player = (1, 1)
        self.enemy = Enemy_Object((random.randint(1, width-2), random.randint(1, height-2)), True)


    def move_player(self, d):
        x = self.player[0]
        y = self.player[1]
        pos = None

        if d[0] == 'd':
            pos = (x + 1, y)
        if d[0] == 'a':
            pos = (x - 1, y)
        if d[0] == 'w':
            pos = (x, y - 1)
        if d[0] == 's':
            pos = (x, y + 1)
            

        if pos not in self.walls or pos not in self.walls:
            self.player = pos
        if pos == (0,1):
            pos == pos

        if pos == self.goal:
            print("You made it to the end!")
            
    def move_enemy(self):
        x = self.enemy.pos[0]
        y = self.enemy.pos[1]
        pos = None

        rand_move = random.randint(1, 4)

        if rand_move == 1:
            pos = (x + 1, y)
        if rand_move == 2:
            pos = (x - 1, y)
        if rand_move == 3:
            pos = (x, y - 1)
        if rand_move == 4:
            pos = (x, y + 1)
            

        if pos not in self.walls:
            self.enemy.pos = pos

    def battle_radius(self):
        px = self.player[0]
        py = self.player[1]
        ex = self.enemy.pos[0]
        ey = self.enemy.pos[1]
        if(abs(px-ex) < c.enemy_attack_radius and abs(py-ey) < c.enemy_attack_radius):
            return True
        else:
            return False
        
    def chest_radius(self):
        px = self.player[0]
        py = self.player[1]
        ex = self.chest.pos[0]
        ey = self.chest.pos[1]
        if(abs(px-ex) < c.enemy_attack_radius and abs(py-ey) < c.enemy_attack_radius):
            return True
        else:
            return False
