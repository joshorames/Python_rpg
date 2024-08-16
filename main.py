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
        
p.main_menu()
for x in range(c.max_stage):
    h.gen_level(x+1,c.max_stage)