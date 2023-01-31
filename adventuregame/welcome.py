import os
import sys
import time
import random
from termcolor import cprint
from playsound import playsound
import multiprocessing

def music2(title):
    playsound('title.mp3')

title = multiprocessing.Process(target=music2, args=(1,))

typing_speed = 80  # wpm

def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    return ('')

# define our clear function
def clear():

# for windows
    if os.name == 'nt':
        _ = os.system('cls')

# for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')


def print_welcome():
    title.start() # Title music thread start
    try:
        col = os.get_terminal_size().columns
    except:
        col = 200
    welcome_str = """
                                               _____________   ____________  __________   
                                              / ____/ ____/ | / / ____/ __ \/  _/ ____/   
                                             / / __/ __/ /  |/ / __/ / /_/ // // /        
                                            / /_/ / /___/ /|  / /___/ _, _// // /___      
                                            \____/_____/_/ |_/_____/_/ |_/___/\____/      
                                                                    
                          _____________  ________   ___    ____ _    _________   __________  ______  ______   
                         /_  __/ ____/ |/ /_  __/  /   |  / __ \ |  / / ____/ | / /_  __/ / / / __ \/ ____/   
                          / / / __/  |   / / /    / /| | / / / / | / / __/ /  |/ / / / / / / / /_/ / __/      
                         / / / /___ /   | / /    / ___ |/ /_/ /| |/ / /___/ /|  / / / / /_/ / _, _/ /___      
                        /_/ /_____//_/|_|/_/    /_/  |_/_____/ |___/_____/_/ |_/ /_/  \____/_/ |_/_____/      
                                                                                                            
                                                   _________    __  _________
                                                  / ____/   |  /  |/  / ____/
                                                 / / __/ /| | / /|_/ / __/   
                                                / /_/ / ___ |/ /  / / /___   
                                                \____/_/  |_/_/  /_/_____/    
                                                
"""
    print(welcome_str.center(col))
    print(slow_type('                                                  Created by Tom Seedorf                '))
    print()
    cprint("                                                   Press Enter to start", attrs=['blink'])
    begin = input('> ')
    clear()
    title.terminate()
    print(slow_type('''
    
You see a large castle in the distance...


Its beauty entrances you...


Is that someone in the tower?


You stop and peer upward at a brilliant yellow belfry...


You hope to remain unseen while determining your next move...


You look for clues to assist your entry..........'''))
