"""This is a retro text-based adventure game.
    
    Version 1.0 12-20-2022"""
from playsound import playsound
from gif_for_cli.execute import execute
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=41, cols=130))
import time
import os
import welcome
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
    time.sleep(.1)
    cv2.imshow("I2", img2)
    cv2.moveWindow("I2", random.randrange(1920), random.randrange(1080)) # Move windows to (x,y) position
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

def clear():
    if os.name == 'nt': # Windows
        _ = os.system('cls') 
    else:
        _ = os.system('clear') #mac and linux (here, os.name is 'posix')

def music(fadedying):
    playsound('fadedying.mp3')
fadedying = multiprocessing.Process(target=music, args=(1,))

def music(piano):
    playsound('piano.mp3')
piano = multiprocessing.Process(target=music, args=(1,))


# Sequence start
while True:
        fadedying.start()
        time.sleep(.01)
        print(welcome.slow_type('''As you're leaving, you hear the dragon's terrible, earth-rumbling whimper one last time.


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
        death_animate() # Begin death collage
        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=1, cols=31))
        clear()
        fadedying.terminate()
        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=41, cols=130))
        break

piano.start()
import blinking_effect
print(welcome.slow_type("tom............wake up......"))
print('\033c', end='') # Clear the terminal
print(welcome.slow_type("A mysterious voice calls out and then fades away...."))
print('\033c', end='') # Clear the terminal