from playsound import playsound
from gif_for_cli.execute import execute
import textwrap
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=41, cols=130))
import time
import os
import random
import pandas as pd
import psycopg2
import webbrowser

# General
def slow_type(t):
    for l in t:
        typing_speed = 80  # wpm
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

def main():
    flag = True
    while True:
        clear()
        if flag == True:
            print(slow_type('''Do you have a favorite artist?'''))
        else:
            print(slow_type('''Perhaps you have another favorite artist?'''))
        print()
        name = input()
        
        # Connect to postgres DB
        conn = psycopg2.connect(dbname="postgres", host = "artwork.c9y5rji1q0ag.us-west-2.rds.amazonaws.com", user = "postgres", password = "postgres")
        
        # Open a cursor to perform database operations
        cur = conn.cursor()

        # Execute and retrieve query
        sql = "SELECT title, artist FROM art"
        cur.execute(sql)
        records = cur.fetchall()

        #Place and format in dataframe
        df = pd.DataFrame(records, columns = ['title', 'artist'])
        pd.set_option('display.max_colwidth', 500, 'display.max_rows', 50)

        df2 = df[(df['artist'].str.contains(name, na=False, case=False))]
        df3 = pd.DataFrame(df2)

        if df3.empty == True:
            print(slow_type('''Sorry, I dont have any artworks by that artist.'''))
            flag = False
        else:
            print()
            print(slow_type('''Let's see which artworks I'm familiar with.........'''))
            print()
            print(df3)
            print()
            time.sleep(3)
            print(slow_type('''Ohhhh, some of these are simply masterpieces, don't you think? 
            
The form, the beauty, the execution—all of it deployed with the most astonishing skill and precision! 
            
Sometimes I catch myself wondering about beauty............

..........Do you, too? 

Sometimes I wonder: Is beauty something in the world?

Or is beauty an assessment we make about the world?'''))
            print()
            beauty = input()
        

        # Open pic in browser
        # webbrowser.open(url, new=1, autoraise=True)
        # Close postgresql connection
        cur.close()
        conn.close()

main()

#def main():
#   while True:
#        print()
#        print("Who's an artist that you like?")
#        artist = input('> ')
#        if artist in ["artist", "artist"]:
#            print("Not the most adventurous adventurer, are you?")
#            sys.exit()
#        elif artist in ["artist", "artist"]: