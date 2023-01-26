from playsound import playsound
from gif_for_cli.execute import execute
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=41, cols=130))
import time
import os
import random
import pandas as pd
import psycopg2
import webbrowser
import inquirer
from tabulate import tabulate

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
        name = input().title()
        
        # Connect to postgres DB and open a cursor
        conn = psycopg2.connect(dbname="postgres", host = "artwork.c9y5rji1q0ag.us-west-2.rds.amazonaws.com", user = "postgres", password = "postgres")
        cur = conn.cursor()

        # Execute and retrieve query
        sql = "SELECT DISTINCT title, artist FROM art ORDER BY artist"
        cur.execute(sql)
        conn.commit()
        records = cur.fetchall()

        #Place and filter dataframe
        df = pd.DataFrame(records, columns = ['title', 'artist'])
        df2 = df[(df['artist'].str.contains(name, na=False, case=False))]
        df3 = pd.DataFrame(df2)
        if df3.empty == True:
            print()
            print(slow_type('''Sorry, I dont have any artworks by that artist.'''))
            time.sleep(2)
            flag = False
            continue
        else:
            print()
            print(slow_type('''Let's see which artworks I'm familiar with.....................................'''))
            print()
            columns = ['Title', 'Artist']
            print(tabulate(df3, headers = columns, tablefmt = 'fancy_grid', showindex='never', maxcolwidths=[90, 30]))
            print()
            cur.close()
            time.sleep(3)

        print(slow_type('''Ohhhh, some of these are simply masterpieces, don't you think? 

The form, the beauty, the execution—all of it deployed with the most astonishing skill and precision!

Isn't this one breathtaking?'''))
        print()
        
        # New cursor and query to get artwork url
        cur2 = conn.cursor()
        sql = "SELECT DISTINCT artist, thumbnail FROM art ORDER BY artist"
        cur2.execute(sql)
        conn.commit()
        records = cur2.fetchall()

        # Get a single random artwork url from the user-entered artist
        daf = pd.DataFrame(records, columns = ['artist', 'thumbnail'])
        daf2 = daf[(daf['artist'].str.contains(name, na=False, case=False))]
        daf3 = pd.DataFrame(daf2, columns = ['thumbnail'])
        daf4 = daf3.values.tolist()
        daf5 = daf4[(random.randrange((len(daf4))))]
        daf6 = str(daf5)
        daf7 = daf6.strip("['']")
        
        # Open pic in browser
        webbrowser.open(daf7, new=1, autoraise=True)

        # Inquiry begin
        time.sleep(30)
        clear()
        print(slow_type('''Sometimes, I catch myself wondering about beauty............

..........Do you, too?''')) 

        time.sleep(2)
        print()
        clear()
        print(slow_type('''Sometimes, I wonder: Is beauty something in the world?

Or is beauty an assessment that we make about the world?'''))
        time.sleep(2)
        print()
        questions = [inquirer.List('beauty', 
            message="The nature of beauty", 
            choices=['Beauty is something in the world.', 'Beauty is an assessment about the world.'],),]
        answers = inquirer.prompt(questions)
        print(answers["beauty"])
        print()
        print(slow_type('''You know what?
        
You might be on to something.

'''))

        # Close postgresql connection and cursor
        cur2.close()
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