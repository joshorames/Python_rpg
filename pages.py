#pages only
import helpers as h

def main_menu():
    print(r"""
___________.__               ________                       
\__    ___/|  |__   ____    /  _____/_____    _____   ____  
  |    |   |  |  \_/ __ \  /   \  ___\__  \  /     \_/ __ \ 
  |    |   |   Y  \  ___/  \    \_\  \/ __ \|  Y Y  \  ___/ 
  |____|   |___|  /\___  >  \______  (____  /__|_|  /\___  >
                \/     \/          \/     \/      \/     \/
                Created from Boredom
            press any button to continue...
                """)
    input()
    h.clear_screen()
def level_complete():
    print(r"""
.____ ____   ____.____      _________                       .__          __             .___
|    |\   \ /   /|    |     \_   ___ \  ____   _____ ______ |  |   _____/  |_  ____   __| _/
|    | \   Y   / |    |     /    \  \/ /  _ \ /     \\____ \|  | _/ __ \   __\/ __ \ / __ | 
|    |__\     /  |    |___  \     \___(  <_> )  Y Y  \  |_> >  |_\  ___/|  | \  ___// /_/ | 
|_______ \___/   |_______ \  \______  /\____/|__|_|  /   __/|____/\___  >__|  \___  >____ | 
        \/               \/         \/             \/|__|             \/          \/     \/
        """)
    input('press button to continue...')
def winner():
    print(r"""
 __      __.__                            
/  \    /  \__| ____   ____   ___________ 
\   \/\/   /  |/    \ /    \_/ __ \_  __ \
 \        /|  |   |  \   |  \  ___/|  | \/
  \__/\  / |__|___|  /___|  /\___  >__|   
       \/          \/     \/     \/            
        """)
    input('press button to continue...')
def lose():
    print(r"""
_____.___.________   ____ ___  ________  .______________________   
\__  |   |\_____  \ |    |   \ \______ \ |   \_   _____/\______ \  
 /   |   | /   |   \|    |   /  |    |  \|   ||    __)_  |    |  \ 
 \____   |/    |    \    |  /   |    `   \   ||        \ |    `   \
 / ______|\_______  /______/   /_______  /___/_______  //_______  /
 \/               \/                   \/            \/         \/ """)
    input('press button to continue...')
    quit()
def battle_page():
    print(r"""        
              / \                                                   / \ 
              | |                                                   | |
              |.|                                                   |.|
              |.|                                                   |.|
              |:|      __                                   __      |:|
            ,_|:|_,   /  )                                 (  \   ,_|:|_,
              (Oo    / _I_                                 _I_ \    oO)
               +\ \  || __|                               |__ ||  / /+
                  \ \||___|                               |___||/ /
                    \ /.:.\-\                           /-/.:.\ /
                     |.:. /-----\                    /-----\ .:.|
                     |___|::oOo::|                  |::oOo::|___|
                     /   |:<_T_>:|                  |:<_T_>:|   \
                    |_____\ ::: /                    \ ::: /_____|
                     | |  \ \:/                        \:/    | |
                     | |   | |                          | |   | |
                     \ /   | \___                    ___/ |   \ /  
                     / |   \_____\                  /_____/   | \
                     `-'                                      '-`                       
        """)
    
def inv_bar(num_of_items):
    arr = []
    for i in range(num_of_items):
        arr.append('=')
    string = ''.join(str(x) for x in arr)
    return string
    
def inventory(items):
    items_copy=items
    number = len(items_copy)
    while(number < 6):
        items_copy.append('[]')
        number+=1
    print("""Inventory""")
    if(items_copy):
        print('╔'+inv_bar(len(items_copy[0]))+'╦'+inv_bar(len(items_copy[1]))+'╦'+inv_bar(len(items_copy[2]))+'╦'+inv_bar(len(items_copy[3]))+'╦'+inv_bar(len(items_copy[4]))+'╦'+inv_bar(len(items_copy[5]))+'╗')
        print('║'+str(items_copy[0])+'║'+str(items_copy[1])+'║'+str(items_copy[2])+'║'+str(items_copy[3])+'║'+str(items[4])+'║'+str(items_copy[5])+'║')
        print('╚'+inv_bar(len(items_copy[0]))+'╩'+inv_bar(len(items_copy[1]))+'╩'+inv_bar(len(items_copy[2]))+'╩'+inv_bar(len(items_copy[3]))+'╩'+inv_bar(len(items_copy[4]))+'╩'+inv_bar(len(items_copy[5]))+'╝')