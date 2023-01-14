"""This is a retro text-based adventure game.
    
    Version 2.0 1-8-2022"""
from playsound import playsound
from gif_for_cli.execute import execute
import textwrap
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=41, cols=130))
import time
import threading
import os
import random
import multiprocessing
import pandas as pd
import psycopg2

# CONSTANTS
FORWARD = "W"
LEFT = "A"
RIGHT = "D"
BACK = "S"
INTERACT = "E"
ATTACK = "Q"
INFO = "X"

# FUNCTIONS

# General
def slow_type2(t, r, s):
    for l in t, r, s:
        typing_speed = 80  # wpm
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    return ('')

def fast_type(t):
    for l in t:
        typing_speed = 130  # wpm
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    return ('')

def faster_type(t):
    for l in t:
        typing_speed = 170  # wpm
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    return ('')

def fastest_type(t):
    for l in t:
        typing_speed = 200  # wpm
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    return ('')

def clear():
#windows
    if os.name == 'nt':
        _ = os.system('cls')
#mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')

def controls():
    return ("""                   
                                    CONTROLS:

                                  Forward:    W
                                  Left:       A
                                  Right:      D
                                  Back:       S
                                  Interact:   E
                                  Attack:     Q
                                  Answer:    Y/N
                                  Controls:   X
            

                               SYSTEM REQUIREMENTS:

                        If you're reading this, you're good.
        """)

# Game command reminder
def badCommand():
    return ("\n Please enter a proper game command. Press 'X' to see the controls.\n")

# Attack, no weapon
def noWeapon1():
    return ("\n You don't even have a weapon. You throw a wimpy punch. Thankfully, no one saw.\n")

def cantShoot():
    return ("\nYou try to use the object, but it won't shoot! Something must be wrong...\n")
 
# Jump, no point
def noInteract1():
    return ("\n You do something with your hands and try to interact with nothing.\n")

# Movement, unable
def cantMove():
    return ("\n You try, but you can't move that way.\n")

def cantDo():
    return ("\n You can't do that right now.\n")


def main():
    # Connect to postgres DB
    conn = psycopg2.connect(dbname="postgres", host = "artwork.c9y5rji1q0ag.us-west-2.rds.amazonaws.com", user = "postgres", password = "postgres")

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute and retrieve query
    cur.execute("SELECT * FROM art")
    records = cur.fetchall()
    print(records)

main()