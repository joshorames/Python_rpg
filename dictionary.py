import helpers as h

#USE FOR DATA DICTIONARIES
chest_drop_chances =  {
    "potions" : 0.6,
    "sword": 0.1,
    "shield": 0.1,
}

chest_drop_desc = {
    "potions": "Gives user health",
    "sword": "Gives user attack",
    "shield": "Gives user defense"
}

# for key, value in chest_drop_chances.items() :
#     print (value)

exp_needed_per_lvl = {
    1: 250,
    2: 1450,
    3: 8000,
    4: 45255,
    5: 256000
}

monster_hp_by_level = {
    1: 50,
    2: 70,
    3: 100,
    4: 130,
    5: 155
}

attacks_by_damage = {
    "Slash": 5,
    "Rain Slash": 10,
    "Rising Thrust": 15,
    "Hidden River Slash": 10,
    "Basic Storm Release": 10,
    "Adept Quick Hit": 10,
    "Waterfall Slash": 30,
    "Hellfire Smash": 70,
    "Dragon Strike": 50,
    "Comet Smash": 50,
}

attack_learn_chances =  {
    'Rain Slash': 0.1,
    'Rising Thrust': 0.9,
    'none': 0.1
}

attacks_by_level = {
    1: ['Slash','Rising Thrust'],
    2: ['Rain Slash']
}

