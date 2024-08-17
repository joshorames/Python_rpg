from random import randint, choice
import subprocess
import platform
import random
import constants as c
import helpers as h
import dictionary as d

class Enemy_Object():
    def __init__(self, pos, alive):
        self.pos = pos
        self.alive = alive
        self.lvl = c.level

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
        self.exp = c.exp
        self.lvl = 1
        self.attacks = c.attacks
    def level_up(self):
        self.hp = c.health
        self.lvl = c.level
        print('LEVELED UP TO LVL ' + str(self.lvl))
        c.health+=100
        attack_learned = h.weighted_choice(d.attack_learn_chances)[0]
        if(attack_learned != 'none' ):
            print('You learned '+attack_learned+' attack')
            duplicated_att=''
            for att in c.attacks:
                if(attack_learned == att):
                    duplicated_att=att
                    print('You already know this move.')
                    break
            if(len(c.attacks) < 3 and duplicated_att==''):
                c.attacks.append(attack_learned)
            if(duplicated_att == '' and attack_learned != 'none'):
                print('Too many skills...')
                skill_replace = input('Choose a  skill to replace: ')
                for x in range(4):
                    if(skill_replace == str(x+1)):
                        c.attacks[x] = attack_learned
                        
                
    def damaged(self, lost_hp):
        self.hp -= lost_hp
    def attack(self, user_input):
        for x in range(4):
            if(user_input == str(x+1)):
                sel_attack = c.attacks[int(user_input)-1]
                attack_damage = d.attacks_by_damage[sel_attack]
                return int(attack_damage)

class Enemy:
    def __init__(self):
        self.hp = d.monster_hp_by_level[c.level]
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
