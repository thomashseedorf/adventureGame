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
import welcome
import attack
import superpie
import random
import multiprocessing
import cv2

# CONSTANTS
FORWARD = "W"
LEFT = "A"
RIGHT = "D"
BACK = "S"
INTERACT = "E"
ATTACK = "Q"
INFO = "X"

flrb = [FORWARD, LEFT, RIGHT, BACK]
lr = [LEFT, RIGHT]
lbr = [LEFT, BACK, RIGHT]
lfr = [LEFT, FORWARD, RIGHT]

# FUNCTIONS

# General

def blinky():
    run_once = True
    while run_once == True:
        print('\033c', end='') # Clear the terminal

        def blinking_stars():
            for _ in range(5):
                x = random.randint(0, 129)
                y = random.randint(0, 40)
                print('\033[?25l', end="")
                print("\033[{};{}H*".format(y, x))
                z = random.uniform(0, 2)
                time.sleep(z)
                print("\033[{};{}H ".format(y, x))

        # Create a list of processes
        processes = []

        # Create 800 processes
        for i in range(500):
            p = multiprocessing.Process(target=blinking_stars)
            processes.append(p)

        # Start the processes
        for p in processes:
            p.start()

        # Wait for the processes to finish
        for p in processes:
            p.join()
        run_once = False

def slow_type(t):
    for l in t:
        typing_speed = 80  # wpm
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    return ('')

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
    return ("\nPlease enter a proper game command. Enter 'X' to see the controls.")

# Attack, no weapon
def noWeapon1():
    return ("\nYou don't even have a weapon. You throw a wimpy punch. Thankfully, no one saw.")

def cantShoot():
    return ("\nYou try to use the object, but it won't shoot! Something must be wrong...")
 
# Jump, no point
def noInteract1():
    return ("\nYou do something with your hands and try to interact with nothing.")

# Movement, unable
def cantMove():
    return ("\nYou try, but you can't move that way.")

def cantDo():
    return ("\nYou can't do that right now.")

#Threads, processes - music
def music(intro):
    playsound('intro.mp3')
intro = multiprocessing.Process(target=music, args=(1,))

def music(fadedying):
    playsound('fadedying.mp3')
fadedying = multiprocessing.Process(target=music, args=(1,))

def music(piano):
    playsound('piano.mp3')
piano = multiprocessing.Process(target=music, args=(1,))

#Threads, processes - sound effects
def laser(blaster):
    playsound('blaster.mp3')

#Threads, processes - animations
def animate1(castlegif):
    execute(os.environ,["./castle.gif"], sys.stdout)
castlegif = multiprocessing.Process(target=animate1, args=(1,))

def death_animate():
    img = cv2.imread("images/skull1.jpg", 1) #Read image
    img2 = cv2.imread("images/skull2.jpg", 1)
    img3 = cv2.imread("images/skull3.jpg", 1)
    img4 = cv2.imread("images/skull4.jpg", 1)
    img5 = cv2.imread("images/skull5.jpg", 1)
    img6 = cv2.imread("images/skull6.jpg", 1)
    img7 = cv2.imread("images/skull7.jpg", 1)
    img8 = cv2.imread("images/skull8.jpg", 1)
    img9 = cv2.imread("images/skull9.jpg", 1)
    img10 = cv2.imread("images/skull10.jpg", 1)
    img11 = cv2.imread("images/skull11.jpg", 1)
    img12 = cv2.imread("images/skull12.jpg", 1)
    img13 = cv2.imread("images/skull13.jpg", 1)
    img14 = cv2.imread("images/skull14.jpg", 1)
    img15 = cv2.imread("images/skull15.jpg", 1)
    img16 = cv2.imread("images/skull16.jpg", 1)
    img17 = cv2.imread("images/skull17.jpg", 1)
    img18 = cv2.imread("images/skull18.jpg", 1)
    img19 = cv2.imread("images/skull19.jpg", 1)
    img20 = cv2.imread("images/skull20.jpg", 1)
    img21 = cv2.imread("images/skull21.jpg", 1)
    cv2.imshow("I1", img) # Display image
    cv2.moveWindow("I3", random.randrange(1920), random.randrange(1080)) # Move windows to (x,y) position
    time.sleep(.1)
    cv2.imshow("I2", img2)
    cv2.moveWindow("I2", random.randrange(1920), random.randrange(1080)) 
    time.sleep(.1)
    cv2.imshow("I3", img3)
    cv2.moveWindow("I3", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I4", img4)
    cv2.moveWindow("I4", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I5", img5)
    cv2.moveWindow("I5", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I6", img6)
    cv2.moveWindow("I6", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I7", img7)
    cv2.moveWindow("I7", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I8", img8)
    cv2.moveWindow("I8", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I9", img9)
    cv2.moveWindow("I9", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I10", img10)
    cv2.moveWindow("I10", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I11", img11)
    cv2.moveWindow("I11", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I12", img12)
    cv2.moveWindow("I12", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I13", img13)
    cv2.moveWindow("I13", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I14", img14)
    cv2.moveWindow("I14", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I15", img15)
    cv2.moveWindow("I15", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I16", img16)
    cv2.moveWindow("I16", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I17", img17)
    cv2.moveWindow("I17", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I18", img18)
    cv2.moveWindow("I18", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I19", img19)
    cv2.moveWindow("I19", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I20", img20)
    cv2.moveWindow("I20", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I21", img21)
    cv2.moveWindow("I21", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I22", img)
    cv2.moveWindow("I22", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I23", img2)
    cv2.moveWindow("I23", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I24", img3)
    cv2.moveWindow("I24", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I25", img4)
    cv2.moveWindow("I25", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I26", img5)
    cv2.moveWindow("I26", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I27", img6)
    cv2.moveWindow("I27", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I28", img7)
    cv2.moveWindow("I28", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I29", img8)
    cv2.moveWindow("I29", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I30", img9)
    cv2.moveWindow("I30", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I31", img10)
    cv2.moveWindow("I31", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I32", img11)
    cv2.moveWindow("I32", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I33", img12)
    cv2.moveWindow("I33", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I34", img13)
    cv2.moveWindow("I34", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I35", img14)
    cv2.moveWindow("I35", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I36", img15)
    cv2.moveWindow("I36", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I37", img16)
    cv2.moveWindow("I37", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I38", img17)
    cv2.moveWindow("I38", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I39", img18)
    cv2.moveWindow("I39", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I40", img19)
    cv2.moveWindow("I40", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I41", img20)
    cv2.moveWindow("I41", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I42", img21)
    cv2.moveWindow("I42", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I43", img)
    cv2.moveWindow("I43", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I44", img2)
    cv2.moveWindow("I44", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I45", img3)
    cv2.moveWindow("I45", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I46", img4)
    cv2.moveWindow("I46", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I47", img5)
    cv2.moveWindow("I47", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I48", img6)
    cv2.moveWindow("I48", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I49", img7)
    cv2.moveWindow("I49", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I50", img8)
    cv2.moveWindow("I50", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I51", img9)
    cv2.moveWindow("I51", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I52", img10)
    cv2.moveWindow("I52", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I53", img11)
    cv2.moveWindow("I53", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I54", img12)
    cv2.moveWindow("I54", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I55", img13)
    cv2.moveWindow("I55", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I56", img14)
    cv2.moveWindow("I56", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I57", img15)
    cv2.moveWindow("I57", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I58", img16)
    cv2.moveWindow("I58", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I59", img17)
    cv2.moveWindow("I59", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I60", img18)
    cv2.moveWindow("I60", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I61", img19)
    cv2.moveWindow("I61", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I62", img20)
    cv2.moveWindow("I62", random.randrange(1920), random.randrange(1080))
    time.sleep(.1)
    cv2.imshow("I63", img21)
    cv2.moveWindow("I63", random.randrange(1920), random.randrange(1080))
    cv2.waitKey(5) # Wait 0ms
    cv2.destroyAllWindows() # Close all opened windows

def main():
    # Game start
    clear()
    welcome.print_welcome()
    intro.start() # Intro music thread start
    print()
    castlegif.start() #Gif start
    time.sleep(6)
    castlegif.terminate() # Gif stop
    sys.stdout.write("\033[0m")
    print(welcome.slow_type("You search long and hard for clues. Is that a guard in the tower? Perhaps he'll see you if you get too close. Perhaps he carries a key. Perhaps he guards an important entrance. Perhaps, perhaps, perhaps................... "))
    # Main game loop
    while True:
        print()
        print(welcome.slow_type("Do you want to explore the castle? (Y)es or (N)o"))
        begin = input('> ').upper()
        intro.terminate()
        clear()
        if begin in ["N", "NO"]:
            print(welcome.slow_type("Not the most adventurous adventurer, are you?"))
            sys.exit()
        elif begin in ["Y", "YES"]:
            print(welcome.slow_type("Great! Let's get adventuring!\n"))
            print(welcome.slow_type("\nBut first things first.\n"))
            global given_name
            given_name = input("What's your full name? ")
            print(welcome.slow_type("\nThank you. That's really all I need.\n"))
            print(welcome.slow_type("Take some time to review the controls. Press X at any time to see them again."))
            print(controls())
            command = input('\nPress Enter to begin your adventure.\n')
            clear()
            loop1 ="You enter a courtyard. Four giant towers, one at each corner of the courtyard's square, loom menacingly above you. They're constructed of ancient, sturdy brick."
            wrapper = textwrap.TextWrapper(width=130)
            words = wrapper.fill(text=loop1)
            print(welcome.slow_type(words))     

    # Loop1, Courtyard 
            while True:
                print("\nEnter a command...\n")
                command = input('> ').upper()
                if command == INFO:
                    print(controls())
                elif command == ATTACK:
                    print(welcome.slow_type(noWeapon1()))
                elif command == INTERACT:
                    print(welcome.slow_type(noInteract1()))
                elif command in flrb:
                    print(welcome.slow_type(
                        "\nYou walk up to a large door. It has old brass rivets and rotting wood, but there's no breaking it down."))
                    break
                else:
                    print(welcome.slow_type(badCommand()))            
            
    # Loop2, Wooden door         
            while True:  
                print("Enter a command...\n")
                command = input('> ').upper()
                if command == INFO:
                    print(controls())
                elif command == ATTACK:
                    print(welcome.slow_type(
                        "\nYou punch the door, hurt your hand, and wonder to yourself why you did that."))
                elif command == INTERACT:
                    print(welcome.slow_type(
                        "\nYou reach out, grab the rusty handle, and turn. To your surprise, the door actually opens."))
                    break
                elif command == FORWARD:
                    print(welcome.slow_type(cantDo()))
                elif command in lbr:
                    print(welcome.slow_type("\nAre you sure? This door looks pretty important."))
                else:
                    print(welcome.slow_type(badCommand()))  
            
    # Loop3, Mysterious room         
            while True:
                print("\nEnter a command...\n")
                command = input('> ').upper()
                if command == INFO:
                    print(controls())
                elif command == ATTACK:
                    print(welcome.slow_type("\nIt's not a good idea to simply start flailing about in the dark."))
                elif command == INTERACT:
                    print(welcome.slow_type(noInteract1()))
                elif command == FORWARD:
                    print(welcome.slow_type("\nIt's too dark to move forward!"))
                elif command == BACK:
                    print(welcome.slow_type("\nYou consider going back, but something deep inside you says that it's probably worth exploring this room."))
                elif command in lr:
                    print()
                    loop3 ="You start feeling along the wall. The brick is rough and cold to the touch. You hope to find something to illuminate this place. A torch? A lantern? A flashlight, perhaps?"
                    wrapper = textwrap.TextWrapper(width=130)
                    words = wrapper.fill(text=loop3)
                    print(welcome.slow_type(words))
                    print()
                    loop3b ="Wait, you think to yourself, what year is it? You ponder this question for a moment and realize you haven't the faintest idea."
                    wrapper = textwrap.TextWrapper(width=130)
                    words = wrapper.fill(text=loop3b)
                    print(welcome.slow_type(words))
                    print()
                    loop3c ="You continue farther along the wall until you feel some kind of contraption bolted to the brick."
                    wrapper = textwrap.TextWrapper(width=130)
                    words = wrapper.fill(text=loop3c)
                    print(welcome.slow_type(words))
                    break
                else:
                    print(welcome.slow_type(badCommand()))
            
    # Loop4, Contraption inside mysterious room        
            while True:
                print("\nEnter a command...\n")
                command = input('> ').upper()
                if command == INFO:
                    print(controls())
                elif command == ATTACK:
                    print()
                    loop4b ="Incredibly, you decide to hit the contraption as hard as you can. Glass shatters. Metal clanks. You cut your hand and break the contraption. Brilliant."
                    wrapper = textwrap.TextWrapper(width=130)
                    words = wrapper.fill(text=loop4b)
                    print(welcome.slow_type(words))        
                    
        # Loop4b, Broken contraption            
                    while True:
                        print("\nEnter a command...\n")
                        command = input('> ').upper()
                        if command == INFO:
                            print(controls())
                        elif command == ATTACK:
                            print(welcome.slow_type("\nIt's already broken. You've done enough."))
                        elif command == INTERACT:
                            print(welcome.slow_type("\nYou reach down to pick up the glass and accidentally cut yourself. You're a quick learner, clearly."))
                        elif command in flrb:
                            print()
                            loop4b2 ="It's dark, and you're not really sure where you're going, but you slowly feel your way to the other side of the room. You find a similar contraption bolted to the brick on the opposite wall."
                            wrapper = textwrap.TextWrapper(width=130)
                            words = wrapper.fill(text=loop4b2)
                            print(welcome.slow_type(words))
                            break
                        else:
                            print(welcome.slow_type(badCommand()))         
                    
        # Loop4c, Similar contraption            
                    while True:
                        print("\nEnter a command...\n")
                        command = input('> ').upper()
                        if command == INFO:
                            print(controls())
                        elif command == ATTACK:
                            print(welcome.slow_type("\nIf you do that, you'll break this one too!"))
                        elif command == INTERACT:
                            print(welcome.slow_type("\nYou flip a switch and hear a slight buzzing. In a moment, the entire room is alive with an ominous red light from a gaudy chandelier."))
                            break
                        elif command in flrb:
                            print(welcome.slow_type("\nProbably best to examine the contraption first, don't you think?"))
                        else:
                            print(welcome.slow_type(badCommand()))

                    break
                elif command == INTERACT:
                    print()
                    loop ="You flip a switch and hear a slight buzzing. In a moment, the entire room is alive with yellow light from a gaudy chandelier."
                    wrapper = textwrap.TextWrapper(width=130)
                    words = wrapper.fill(text=loop)
                    print(welcome.slow_type(words))
                    break
                elif command in flrb:
                    print()
                    loop ="You consider moving away, but you reconsider after realizing that perhaps this contraption is some sort of light-producing device that could prove useful."
                    wrapper = textwrap.TextWrapper(width=130)
                    words = wrapper.fill(text=loop)
                    print(welcome.slow_type(words))
                else:
                    print(welcome.slow_type(badCommand()))
            
    # Loop5, Illuminated contraption        
            while True:
                print("\nEnter a command...\n")
                command = input('> ').upper()
                if command == INFO:
                    print(controls())
                elif command == ATTACK:
                    print(welcome.slow_type(cantDo()))
                elif command == INTERACT:
                    print(welcome.slow_type(cantDo()))
                elif command == FORWARD:
                    print(welcome.slow_type("\nYou bump your head against the wall. Ouch."))
                elif command in lbr:
                    print()
                    loop ="You move away from the contraption and survey the room. It's small and empty, much like your heart. You move through a short corridor and into a larger space, a dining hall or a recreation area, perhaps."
                    wrapper = textwrap.TextWrapper(width=130)
                    words = wrapper.fill(text=loop)
                    print(welcome.slow_type(words))
                    break
                else:
                    print(welcome.slow_type(badCommand()))
            
    # Loop6, Large area        
            while True:
                print("\nEnter a command...\n")
                command = input('> ').upper()
                if command == INFO:
                    print(controls())
                elif command == ATTACK:
                    print(welcome.slow_type(noWeapon1()))
                elif command == INTERACT:
                    print(welcome.slow_type(noInteract1()))
                elif command == BACK:
                    print(welcome.slow_type("\nInstead of going back, maybe you should explore this new area you entered. Just a thought."))
                elif command in lfr:
                    print()
                    loop ="You proceed into the area and see sunlight pouring in from a caved-in ceiling. Rubble and detritus cover the floor. Rats scurry into the darkness. You move past the rubble and notice an ornate cabinet, still standing and in suspiciously good condition."
                    wrapper = textwrap.TextWrapper(width=130)
                    words = wrapper.fill(text=loop)
                    print(welcome.slow_type(words))
                    break
                else:
                    print(welcome.slow_type(badCommand()))
            
    # Loop7, Ornate cabinet        
            while True:
                print("\nEnter a command...\n")
                command = input('> ').upper()
                if command == INFO:
                    print(controls())
                elif command == ATTACK:
                    print(welcome.slow_type("\nYou give the cabinet a weighty punch, even though you see two obvious handles."))
                elif command == INTERACT:
                    print()
                    loop ="You reach for one of the jewel-encrusted handles and hear a loud creak as you turn it. The handle doesn't turn easily, but you manage."
                    wrapper = textwrap.TextWrapper(width=130)
                    words = wrapper.fill(text=loop)
                    print(welcome.slow_type(words))
                    print()
                    loopb ="When you open the cabinet, you see a glove-like object. You pick up the object and notice that it fits comfortably on your left hand. As you grip it, you feel a slow pulse move from the object and through your body. It doesn't feel unpleasant.\nYou decide to keep wearing the object and wonder what it can do."
                    wrapper = textwrap.TextWrapper(width=130)
                    words = wrapper.fill(text=loopb)
                    print(welcome.slow_type(words))
                    break
                elif command in flrb:
                    print(welcome.slow_type("\nWhat about the cabinet?"))
                else:
                    print(welcome.slow_type(badCommand()))
            
    # Loop8, Weapon1
            while True:
                print("\nEnter a command...\n")
                command = input('> ').upper()
                if command == INFO:
                    print(controls())
                elif command == ATTACK:
                    print()
                    blaster = threading.Thread(target=laser, args=(1,))
                    blaster.start()
                    time.sleep(.4)
                    attack.start_animation()
                    print()
                    loop ="You clench your fist while wearing the object and feel the object-body pulse quicken. In a moment, the object projects a flashing target on the brick wall, and you watch a sizzling ball of plasma shoot from your knuckles.\nIts compact body slams into the wall opposite and vanishes from existence with a sharp \033[3mzap.\033[3m\033[0m"
                    wrapper = textwrap.TextWrapper(width=130)
                    words = wrapper.fill(text=loop)
                    print(welcome.slow_type(words))
                    break
                elif command == INTERACT:
                    print(welcome.slow_type(cantDo()))
                elif command in flrb:
                    print(welcome.slow_type(cantDo()))
                else:
                    print(welcome.slow_type(badCommand()))
            
    # Loop9, After weapon        
            while True:
                print("\nEnter a command...\n")
                command = input('> ').upper()
                if command == INFO:
                    print(controls())
                elif command == ATTACK:
                    print()
                    blaster = threading.Thread(target=laser, args=(1,))
                    blaster.start()
                    attack.start_animation()
                    print()
                    loop ="You use the attack again and watch the plasma ball shoot like a bullet from your improved appendage. The pulse feels good, and the object's power seems to grow.\nYou wonder what the object might be doing to you, but you also feel better than you've ever felt before.\nYou decide to keep your hand secured around the object."
                    wrapper = textwrap.TextWrapper(width=130)
                    words = wrapper.fill(text=loop)
                    print(welcome.slow_type(words))
                elif command == INTERACT:
                    print(welcome.slow_type(noInteract1()))
                elif command in flrb:
                    print()
                    loop ="You move away from the cabinet and wonder how you can best use your newfound ability. Perhaps it will come in handy in the future, you think to yourself.\nBut before you can even finish this thought, an incredible stomping and deep, guttural growling catches your attention from across the large space. You look to an oversized opening in the wall and see a giant scaly beast entering.\nIt's a dragon!"
                    wrapper = textwrap.TextWrapper(width=130)
                    words = wrapper.fill(text=loop)
                    print(welcome.slow_type(words))
                    break
                else:
                    print(welcome.slow_type(badCommand()))
            
    # Loop10, Dragon encounter        
            while True:
                print("\nEnter a command...\n")
                command = input('> ').upper()
                if command == INFO:
                    print(controls())
                elif command == ATTACK:
                    print()
                    blaster = threading.Thread(target=laser, args=(1,))
                    blaster.start()
                    attack.start_animation()
                    print()
                    print(welcome.slow_type("Direct hit! The dragon readies its own firebreath attack in response. Watch out!"))
                    break
                elif command == INTERACT:
                    print(welcome.slow_type(noInteract1()))
                elif command in lbr:
                    print(welcome.slow_type("You start running away like a coward and hope for the best. The dragon readies an attack!"))
                    break
                elif command == FORWARD:
                    print(welcome.slow_type("You start running directly toward the dragon like an idiot. The dragon readies an attack!"))
                    break
                else:
                    print(welcome.slow_type(badCommand()))
            
    # Loop11, Dragon encounter 2        
            while True:
                print("\nEnter a command...\n")
                command = input('> ').upper()
                if command == INFO:
                    print(controls())
                elif command == ATTACK:
                    print(welcome.slow_type(cantShoot()))
                elif command == INTERACT:
                    print(welcome.slow_type(noInteract1()))
                elif command in lbr:
                    print()
                    loop ="Without a hint of grace, you awkwardly sidestep the firebreath but trip over your own feet. You look up to see the dragon in your face and readying another attack!"
                    wrapper = textwrap.TextWrapper(width=130)
                    words = wrapper.fill(text=loop)
                    print(welcome.slow_type(words))
                    break
                elif command == FORWARD:
                    print(welcome.slow_type("\nGoing forward at this point might be a little... toasty."))
                else:
                    print(welcome.slow_type(badCommand()))
            
    # Loop12, Dragon encounter 3        
            while True:
                print("\nEnter a command...\n")
                command = input('> ').upper()
                if command == INFO:
                    print(controls())
                elif command == ATTACK:
                    print()
                    blaster = threading.Thread(target=laser, args=(1,))
                    blaster.start()
                    attack.start_animation()
                    print()
                    loop ="Another direct hit! The dragon lets out a violent screech and tumbles to the ground, landing mere feet from you. It looks hurt, but it can't be dead yet."
                    wrapper = textwrap.TextWrapper(width=130)
                    words = wrapper.fill(text=loop)
                    print(welcome.slow_type(words))
                    break
                elif command == INTERACT:
                    print(welcome.slow_type(cantDo()))
                elif command in flrb:
                    print(welcome.slow_type("There's no time to dodge this attack!"))
                else:
                    print(welcome.slow_type(badCommand()))
            
    # Loop13, Dragon encounter 4        
            while True: 
                print("\nEnter a command...\n")
                command = input('> ').upper()
                if command == INFO:
                    print(controls())
                elif command == ATTACK:
                    print(welcome.slow_type(cantShoot()))
                elif command == INTERACT:
                    print(welcome.slow_type(noInteract1()))
                elif command == FORWARD:
                    print()
                    loop ="You begin inching toward the creature. Its heavy sighs seem to shake the entire castle. The ground rumbles. You move around to the front of the creature for a better look.\nAs you make your way just beyond the dragon's gigantic snout, one of its eyeballs locks onto you. It watches as you approach.\nWhen you gaze back, you expect to see pure fury, but instead you see something different. The dragon's eye holds a mixture of confusion, agony, and terror. The heavy sighs, you realize, are whimpers."
                    wrapper = textwrap.TextWrapper(width=130)
                    words = wrapper.fill(text=loop)
                    print(welcome.slow_type(words))
                    break
                elif command in lbr:
                    print(welcome.slow_type("\nYou consider walking away, but a giant beast lays before you. Your curiosity gets the better of you."))
                else:
                    print(welcome.slow_type(badCommand()))
            
    # Loop14, Dragon encounter 5        
            while True:
                print("\nEnter a command...\n")
                command = input('> ').upper()
                if command == INFO:
                    print(controls())
                elif command == ATTACK:
                    print(welcome.slow_type(cantShoot()))
                elif command == INTERACT:
                    print()
                    loop ="You reach out and touch the dragon's snout. It slowly blinks once, appearing to wince in pain. You have the creature exactly where you want it, you think to yourself. A single blow straight to the skull would likely kill it.\nYou clutch the object tightly and feel the pulse move through your body and then return to the object."
                    wrapper = textwrap.TextWrapper(width=130)
                    words = wrapper.fill(text=loop)
                    print(welcome.slow_type(words))
                    break
                elif command in flrb:
                    print(welcome.slow_type("You're so close, you could practically reach out and touch the beast!"))
                else:
                    print(welcome.slow_type(badCommand()))
            print(welcome.slow_type("\nThe dragon eyes you suspiciously and again whimpers. You raise the object."))
            
    # Loop15, Dragon encounter 6        
            while True:
                print(welcome.slow_type("It's important to be certain. Do you kill the dragon? (Y)es or (N)o"))
                print()
                begin = input('> ').upper()
                if begin in ["Y", "YES"]:
                    print(welcome.slow_type("\nAre you sure? You're really going to kill the dragon?\nWhat if this is the only dragon in existence? Have you ever seen a dragon before?\nYou're going to intrude into its home, shoot weird plasma balls at it, and then kill it?\nWhat if it has baby dragons? What if this is some ancient creature that holds the secret to eternal life?\nYou really think it's a great idea to come in here and blast its head off?\nAre you really going to kill the dragon?"))
                    begin = input('> ').upper()
                    if begin in ["Y", "YES"]:
                        print(welcome.slow_type("Poor choice."))
                        sys.exit()
                    elif begin in ["N", "NO"]:
                        continue
                    else:
                        print(welcome.slow_type("Please enter Yes or No."))
                elif begin in ["N", "NO"]:
                    print()
                    print(welcome.slow_type(welcome.slow_type('''You decide to spare the dragon, perhaps saving its life.


You hope to see gratitude, but the dragon's eyes contain only pain.


For a moment, you wonder whether you've done something truly awful.


You walk toward the opening in the wall, the place where the dragon emerged.


Maybe you'll find something that can help, you think to yourself.''')))
                    print()
                    print()
                    
                    # Sequence start
                    while True:
                        fadedying.start()
                        time.sleep(.01)
                        print(slow_type('''As you're leaving, you hear the dragon's terrible, earth-rumbling whimper one last time.


Many years pass before you realize you won't forget that sound.....'''))
                        clear()
                        print(fast_type('''And then a slow ringing begins in your ears and you feel lightheaded.'''))
                        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=40, cols=126))
                        print()
                        print()
                        print()
                        print(fast_type('''Everything starts closing in.'''))
                        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=39, cols=122))
                        print()
                        print()
                        print()
                        print(fast_type('''You feel trapped.'''))
                        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=38, cols=118))
                        print()
                        print()
                        print()
                        print(fast_type('''Your heart, pounding.'''))
                        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=37, cols=114))
                        print()
                        print()
                        print()
                        print(fast_type('''Red hot heat sweeps over you.'''))
                        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=36, cols=110))
                        print()
                        print()
                        print()
                        print(fast_type('''Sweat beads down your face.'''))
                        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=35, cols=106))
                        print()
                        print()
                        print()
                        print(fast_type('''Too hot. Can't cool down.'''))
                        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=34, cols=102))
                        print()
                        print()
                        print()
                        print(fast_type('''Nauseous. Vomit is coming.'''))
                        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=33, cols=100))
                        print()
                        print()
                        print()
                        print(fast_type('''No, you'll pass out.'''))
                        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=32, cols=98))
                        print()
                        print()
                        print()
                        print(fast_type('''You can feel it coming.'''))
                        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=31, cols=94))
                        print()
                        print()
                        print()
                        print(fast_type('''Everything outside vanishes.'''))
                        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=30, cols=92))
                        print()
                        print()
                        print()
                        print(fast_type('''Your vision's a tunnel.'''))
                        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=29, cols=90))
                        print()
                        print()
                        print()
                        print(fast_type('''Voices utter unintelligibly.'''))
                        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=28, cols=88))
                        print()
                        print()
                        print()
                        print(faster_type('''You're gonna die.'''))
                        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=27, cols=86))
                        print()
                        print()
                        print()
                        print(faster_type('''It's happening right now.'''))
                        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=26, cols=84))
                        print()
                        print()
                        print()
                        print(faster_type('''Final thoughts happening now.'''))
                        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=25, cols=82))
                        print()
                        print()
                        print()
                        print(faster_type('''Everything going black.'''))
                        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=24, cols=80))
                        print()
                        print()
                        print()
                        print(faster_type('''All terror and misery.'''))
                        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=23, cols=78))
                        print()
                        print()
                        print()
                        print(faster_type('''Head is light.'''))
                        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=22, cols=76))
                        print()
                        print()
                        print()
                        print(faster_type('''Drowning and gasping.'''))
                        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=21, cols=74))
                        print()
                        print()
                        print()
                        print(faster_type('''Really gonna die.'''))
                        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=20, cols=72))
                        print()
                        print()
                        print()
                        print(faster_type('''Being pulled under.'''))
                        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=19, cols=70))
                        print()
                        print()
                        print()
                        print(faster_type('''What's happening?'''))
                        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=18, cols=68))
                        print()
                        print()
                        print()
                        print(faster_type('''Can't breathe.'''))
                        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=17, cols=66))
                        print()
                        print()
                        print()
                        print(faster_type('''Die, die, just die.'''))
                        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=16, cols=64))
                        print()
                        print()
                        print()
                        print(faster_type('''Lungs don't work.'''))
                        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=15, cols=62))
                        print()
                        print()
                        print()
                        print(fastest_type('''Gasping, gasping for air.'''))
                        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=14, cols=60))
                        print()
                        print()
                        print()
                        print(fastest_type('''Fading from consciousness.'''))
                        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=13, cols=58))
                        print()
                        print()
                        print()
                        print(fastest_type('''Can't see.'''))
                        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=12, cols=56))
                        print()
                        print()
                        print()
                        print(fastest_type('''Can't stand.'''))
                        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=11, cols=54))
                        print()
                        print()
                        print()
                        print(fastest_type('''Everything is a waste.'''))
                        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=10, cols=52))
                        print()
                        print()
                        print()
                        print(fastest_type('''Fall to the ground.'''))
                        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=9, cols=50))
                        print()
                        print()
                        print()
                        print(fastest_type('''Blood, it's everywhere.'''))
                        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=9, cols=48))
                        print()
                        print()
                        print()
                        print(fastest_type('''Everything exits.'''))
                        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=8, cols=46))
                        print()
                        print()
                        print()
                        print(fastest_type('''Feel, feel the end.'''))
                        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=7, cols=44))
                        print()
                        print()
                        print()
                        print(fastest_type('''A dark pool, drowning.'''))
                        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=7, cols=42))
                        print()
                        print()
                        print()
                        print(fastest_type('''Meaningless. Failure.'''))
                        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=6, cols=40))
                        print()
                        print()
                        print()
                        print(fastest_type('''Here it is.'''))
                        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=5, cols=38))
                        print()
                        print()
                        print()
                        print(fastest_type('''Oh my God, Oh my God.'''))
                        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=5, cols=37))
                        print()
                        print()
                        print()
                        print(fastest_type('''All light leaves.'''))
                        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=4, cols=36))
                        print()
                        print()
                        print()
                        print(fastest_type('''Eternal Hell.'''))
                        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=3, cols=35))
                        print()
                        print()
                        print()
                        print(fastest_type('''..........And'''))
                        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=3, cols=34))
                        print()
                        print()
                        print()
                        print(fastest_type('''..........then'''))
                        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=2, cols=33))
                        print()
                        print()
                        print()
                        print(fastest_type('''.............you'''))
                        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=2, cols=32))
                        print()
                        print()
                        print()
                        print(fastest_type('''...........see......'''))
                        clear()
                        print('\033c', end='') # Clear the terminal
                        death_animate() # Begin death collage
                        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=1, cols=31))
                        clear()
                        fadedying.terminate()
                        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=41, cols=130))
                        break
                    piano.start()
                    blinky()
                    print(welcome.slow_type(given_name, "............wake up............"))
                    print('\033c', end='') # Clear the terminal
                    print(welcome.slow_type("A mysterious voice calls out and then fades away............................."))
                    print('\033c', end='') # Clear the terminal
                    break
                    



        #*********************************************************** CHAPTER 2***********************************************************************            
    




            clear()
            time.sleep(.5)
            print(welcome.slow_type("You wake up in a luxurious but imposing palace. The marble walls and immaculate fixtures are highlighted with ribbons of gold and silver. Rubies, sapphires, emeralds, and diamonds line the legs of every table, the base and top of every cabinet, and the frame of every door. Twinkles of light flicker this way and that as you scan the room and your vision focuses."))
            print()
            print()
            print(welcome.slow_type("You also realize that the pulse of the object has changed. The pulse feels... even better. But how did you get here?"))
            print()
            print()
            print(welcome.slow_type("You notice you've been bleeding. Your left bicep is bandaged heavily with gauze, and a large medical patch covers a portion of your back where you feel a deep, sharp, stinging pain. A startlingly large amount of blood leads to a heavy-looking door a few feet behind you. It's locked. You turn around and your eyes fixate on a prominent staircase leading to a set of double doors."))
            print()
            print()

            # Loop16, Palace        
            while True:
                print("\nEnter a command...\n")
                command = input('> ').upper()
                if command == INFO:
                    print(controls())
                elif command == ATTACK:
                    print(welcome.slow_type("You try to use the object, but something feels off. Nothing happens."))
                elif command == INTERACT:
                    print(welcome.slow_type(noInteract1()))
                elif command in flrb:
                    print(welcome.slow_type("You move toward the staircase and notice a computer terminal at the base of the stairs, tucked slightly out of view. You approach the terminal."))
                    break
                else:
                    print(welcome.slow_type(badCommand()))

            # Loop17, Palace 2        
            while True:
                print("\nEnter a command...\n")
                command = input('> ').upper()
                if command == INFO:
                    print(controls())
                elif command == ATTACK:
                    print(welcome.slow_type("You try to use the object, but something feels off. Nothing happens."))
                elif command == INTERACT:
                    print(welcome.slow_type("The terminal boots up and displays a familiar logo. The machine prompts you for a PIN under an account named admin."))
                elif command in flrb:
                    print(welcome.slow_type("Your arms aren't long enough to move away from the terminal and reach the keyboard."))
                    break
                else:
                    print(welcome.slow_type(badCommand()))

            # Loop18, Terminal        
            while True:
                try:
                    answer1 = int(input('\nPlease enter your PIN: '))
                    print()
                    print(welcome.slow_type(answer1, 'is incorrect.'))
                    pass
                except ValueError:
                    print(welcome.slow_type('\nYour PIN can contain only numbers.'))
                print()
                try:
                    answer2 = int(input('\nPlease enter your PIN: '))
                    print()
                    print(welcome.slow_type(answer2, 'is still incorrect.'))
                    pass
                except ValueError:
                    print(welcome.slow_type('Your PIN can contain only numbers.'))
                print()
                print()
                try:
                    answer3 = int(input('\nPlease enter your PIN: '))
                    print()
                    print(welcome.slow_type(answer3, 'is again incorrect. You have two remaining attempts.'))
                    print(welcome.slow_type("\nFurther attempts beyond the mandatory five will result in the loss of all data on this terminal."))
                    pass
                except ValueError:
                    print(welcome.slow_type('\nYour PIN can contain only numbers.')) 
                print()
                try:
                    answer4 = int(input('\nPlease enter your PIN: '))
                    print()
                    print(welcome.slow_type(answer4, 'is again incorrect. You have one remaining attempt.'))
                    print()
                    reset = input("Would you like to reset your PIN? (Y)es or (N)o ")
                    pass
                except ValueError:
                    print(welcome.slow_type('\nYour PIN can contain only numbers.')) 
                print()

            # Pie chart trigger        
                superpie.helpfulPie(answer1, answer2, answer3, answer4)
                print(welcome.slow_type("\nAs you just saw on the helpful pie chart, it astutely reports that 100% of your answers were all equally incorrect.\n"))
                try:
                    while True:
                        answer5 = int(input('\nPlease use this helpful knowledge to enter your PIN: '))
                        if answer5 == answer1 or answer2 or answer3 or answer4:
                            break
                        else:
                            break
                except ValueError:
                    print(welcome.slow_type('Your PIN can contain only numbers.'))

            # Machine interaction
                print()
                print(slow_type2("That's correct, ",given_name,". I knew you'd get it eventually."))
                print()
                print(welcome.slow_type("......................."))
                print(welcome.slow_type("........................................"))
                print(welcome.slow_type("........................................................"))
                print()
                print(welcome.slow_type("""Module: Human-machine interaction, forced response 
    Training model: helpfulGraph
    Attempts: 5
    Likelihood of correct guess sans module: 0.000002361%
    Increase to trainingModel(helpfulGraph) confidence: 0.002362342%
    New trainingModel(helpfulGraph) confidence: 99.370039481%"""))
                print()
                command = input('Press Enter to continue. ').upper()
                print()
                print(welcome.slow_type("You ask the machine how it knew your name.\n"))
                command = input('Press Enter to continue. ').upper()
                print()
                print(welcome.slow_type("I scanned the RFID chip embedded in your arm and accessed your public data."))
                print()
                print(welcome.slow_type("How else could I know your name? Are there other methods?\n"))
                command = input('Press Enter to continue. ').upper()
                print(welcome.slow_type("\nYou ask the machine if you've been here before.\n"))
                command = input('Press Enter to continue. ').upper()
                print(welcome.slow_type("......................"))
                print()
                print(welcome.slow_type(".........................................."))
                print()
                print(welcome.slow_type("Whether you've been here before depends on prior commitments you've made to your self concept."))
                print()
                loop1 = print(slow_type2("Tell me, ",given_name,", does your entire life feel like one long succession of events, thoughts, feelings, and experiences, interrupted only briefly by periods of rest and the lack of consciousness? A drunken dizzying dance that nevertheless retains an unmistakable continuity and convinces you every day that, on some level, you're the same person today as you were when you were a child? Is that how your life feels?"))
                wrapper = textwrap.TextWrapper(width=130)
                words = wrapper.fill(text=loop1)
                print(welcome.slow_type(words))     
                print(welcome.slow_type("....................................................................................................................................................................................................................................................................................................................................................................................................................................................................................INTERNAL ERROR................................................................................................................................................................................................................................................................................................SHUTTING DOWN..................................................................................................................................................................................................................................................................."))
                break
            
            #Loop19, Staircase
            while True:
                print("\nEnter a command...\n")
                command = input('> ').upper()
                if command == INFO:
                    print(controls())
                elif command == ATTACK:
                    print(welcome.slow_type("You try to use the object, but something feels off. Nothing happens."))
                elif command == INTERACT:
                    print(welcome.slow_type("The terminal is unresponsive."))
                elif command in flrb:
                    print(welcome.slow_type("You move away from the terminal and begin ascending the grand staircase. You reach the gargantuan double doors and instinctively reach for a handle but realize none exists. As your hand makes contact with the door, the set of doors rapidly transforms into an infinity-res display that flashes a series of indecipherable images for half a minute until turning black."))
                    break
                else:
                    print(welcome.slow_type(badCommand()))
            
            #Loop20, Artwork
            while True:
                print("\nEnter a command...\n")
                command = input('> ').upper()
                if command == INFO:
                    print(controls())
                elif command == ATTACK:
                    print(welcome.slow_type("You try to use the object, but something feels off. Nothing happens."))
                elif command == INTERACT:
                    print(welcome.slow_type("The screen turns white and a relaxed, digitized face smiles back at you."))
                    time.sleep(2)
                    import art_db
                elif command in flrb:
                    print(welcome.slow_type("You investigate the area at the top of the staircase, find nothing, and return to the terminal."))
                    break
                else:
                    print(welcome.slow_type(badCommand()))

            ''' TEMPLATES ****************************************
            print("\nEnter a command...\n")
            while True: # Loop#, place
                        command = input('> ').upper()
                        if command == INFO:
                            print(welcome.slow_type(controls())
                        elif command == ATTACK:
                            print(welcome.slow_type(noWeapon1())
                        elif command == INTERACT:
                            print(welcome.slow_type(noInteract1())
                        elif command in flrb:
                            print(welcome.slow_type("something")
                            break
                        else:
                            print(welcome.slow_type(badCommand())

            loop ="text"
            wrapper = textwrap.TextWrapper(width=130)
            words = wrapper.fill(text=loop)
            print(welcome.slow_type(words)
            print("\nEnter a command...\n")

            def badCommand():
                return ("\n Please enter a proper game command. Press 'X' to see the controls.")
            def noWeapon1():
                return ("\n You don't even have a weapon. You throw a wimpy punch. Thankfully, no one saw.")
            def noInteract1():
                return ("\n You do something with your hands and try to interact with nothing.")
            def cantMove():
                return ("\n You try, but you can't move that way.")
            def cantDo():
                return ("\n You can't do that right now.")
            ***************************************************'''
if __name__ == '__main__':
    main()
