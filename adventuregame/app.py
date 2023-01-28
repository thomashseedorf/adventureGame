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

#Threads, processes - music
def music(intro):
    playsound('intro.mp3')
intro = multiprocessing.Process(target=music, args=(1,))

def music(fadedying):
    playsound('fadedying.mp3')
fadedying = multiprocessing.Process(target=music, args=(1,))

#Threads, processes - sound effects
def laser(blaster):
    playsound('blaster.mp3')

#Threads, processes - animations
def animate1(castlegif):
    execute(os.environ,["./castle.gif"], sys.stdout)
castlegif = multiprocessing.Process(target=animate1, args=(1,))

def main():
    # Game start
    welcome.print_welcome()
    intro.start() # Intro music thread start
    print()
    castlegif.start() #Gif start
    time.sleep(6)
    castlegif.terminate() # Gif stop
    sys.stdout.write("\033[0m")
    print(welcome.slow_type("You search long and hard for clues. Is that a guard in the tower? Perhaps he'll see you if you get too close. Perhaps he carries a key. Perhaps he guards an important entrance. Perhaps, perhaps, perhaps... "))
    # Main game loop
    while True:
        print()
        print("Do you want to explore the castle? (Y)es or (N)o")
        begin = input('> ').upper()
        intro.terminate()
        clear()
        if begin in ["N", "NO"]:
            print("Not the most adventurous adventurer, are you?")
            sys.exit()
        elif begin in ["Y", "YES"]:
            print("\nGreat! Let's get adventuring!\n")
            print("\nBut first things first.\n")
            global given_name
            given_name = input("What's your full name? ")
            print("\nThank you. That's really all I need.\n")
            print("Take some time to review the controls. Press X at any time to see them again.")
            print(controls())
            print("\nNow you should be ready.\n")
            command = input('\nPress any key to begin your adventure.\n')
            loop1 ="You enter a courtyard. Four giant towers, one at each corner of the courtyard's square, loom menacingly above you. They're constructed of ancient, sturdy brick."
            wrapper = textwrap.TextWrapper(width=600)
            words = wrapper.fill(text=loop1)
            print(words)       
            print("\nEnter a command...\n")

    # Loop1, Courtyard 
            while True:  
                command = input('> ').upper()
                if command == INFO:
                    print(controls())
                elif command == ATTACK:
                    print(noWeapon1())
                elif command == INTERACT:
                    print(noInteract1())
                elif command == FORWARD or BACK or LEFT or RIGHT:
                    print(
                        "\nYou walk up to a large door. It has old brass rivets and rotting wood, but there's no breaking it down.\n")
                    break
                else:
                    print(badCommand())                
            print("Enter a command...\n")
            
    # Loop2, Wooden door         
            while True:  
                command = input('> ').upper()
                if command == INFO:
                    print(controls())
                elif command == ATTACK:
                    print(
                        "\nYou punch the door, hurt your hand, and wonder to yourself why you did that.\n")
                elif command == INTERACT:
                    print(
                        "\nYou reach out, grab the rusty handle, and turn. To your surprise, the door actually opens.\n")
                    break
                elif command == FORWARD or BACK or LEFT or RIGHT:
                    print("\nAre you sure? This door looks pretty important.\n")
                else:
                    print(badCommand())        
            print("Enter a command...\n")    
            
    # Loop3, Mysterious room         
            while True:
                command = input('> ').upper()
                if command == INFO:
                    print(controls())
                elif command == ATTACK:
                    print(
                        "\n It's not a good idea to simply start flailing about in the dark.\n")
                elif command == INTERACT:
                    print(noInteract1())
                elif command == FORWARD:
                    print("\n It's too dark to move forward!\n")
                elif command == BACK:
                    print(
                        "\nYou consider going back, but something deep inside you says that it's probably worth exploring this room.\n")
                elif command == LEFT or RIGHT:
                    loop3 ="You start feeling along the wall. The brick is rough and cold to the touch. You hope to find something to illuminate this place. A torch? A lantern? A flashlight, perhaps? Wait, you think to yourself, what year is it? You ponder this question for a moment and realize you haven't the faintest idea. You continue farther along the wall until you feel some kind of contraption bolted to the brick."
                    wrapper = textwrap.TextWrapper(width=600)
                    words = wrapper.fill(text=loop3)
                    print(words)
                    break
                else:
                    print(badCommand())
            print("\nEnter a command...\n")
            
    # Loop4, Contraption inside mysterious room        
            while True:
                command = input('> ').upper()
                if command == INFO:
                    print(controls())
                elif command == ATTACK:
                    loop4b ="Incredibly, you decide to hit the contraption as hard as you can. Glass shatters. Metal clanks. You cut your hand and break the contraption. Brilliant."
                    wrapper = textwrap.TextWrapper(width=600)
                    words = wrapper.fill(text=loop4b)
                    print(words)
                    print("\nEnter a command...\n")            
                    
        # Loop4b, Broken contraption            
                    while True:
                        command = input('> ').upper()
                        if command == INFO:
                            print(controls())
                        elif command == ATTACK:
                            print("\nIt's already broken. You've done enough.\n")
                        elif command == INTERACT:
                            print(
                                "\nYou reach down to pick up the glass and accidentally cut yourself. You're a quick learner, clearly.\n")
                        elif command == FORWARD or LEFT or RIGHT or BACK:
                            loop4b2 ="It's dark, and you're not really sure where you're going, but you slowly feel your way to the other side of the room. You find a similar contraption bolted to the brick on the opposite wall."
                            wrapper = textwrap.TextWrapper(width=600)
                            words = wrapper.fill(text=loop4b2)
                            print(words)
                            break
                        else:
                            print(badCommand())            
                    print("\nEnter a command...\n")
                    
        # Loop4c, Similar contrapation            
                    while True:
                        command = input('> ').upper()
                        if command == INFO:
                            print(controls())
                        elif command == ATTACK:
                            print("\nIf you do that, you'll break this one too!\n")
                        elif command == INTERACT:
                            print(
                                "\nYou flip a switch and hear a slight buzzing. In a moment, the entire room is alive with an ominous red light from a gaudy chandelier.\n")
                        elif command == FORWARD or LEFT or RIGHT or BACK:
                            print(
                                "\nProbably best to examine the contraption first, don't you think?\n")
                            break
                        else:
                            print(badCommand())

                    break
                elif command == INTERACT:
                    loop ="You flip a switch and hear a slight buzzing. In a moment, the entire room is alive with yellow light from a gaudy chandelier."
                    wrapper = textwrap.TextWrapper(width=600)
                    words = wrapper.fill(text=loop)
                    print(words)
                    break
                elif command == FORWARD or LEFT or RIGHT or BACK:
                    loop ="You consider moving away, but you reconsider after realizing that perhaps this contraption is some sort of light-producing device that could prove useful."
                    wrapper = textwrap.TextWrapper(width=600)
                    words = wrapper.fill(text=loop)
                    print(words)
                else:
                    print(badCommand())
            print("Enter a command...\n")
            
    # Loop5, Illuminated contraption        
            while True:
                command = input('> ').upper()
                if command == INFO:
                    print(controls())
                elif command == ATTACK:
                    print(cantDo())
                elif command == INTERACT:
                    print(cantDo())
                elif command == FORWARD:
                    print("\nYou bump your head against the wall. Ouch.\n")
                elif command == LEFT or RIGHT or BACK:
                    loop ="You move away from the contraption and survey the room. It's small and empty, much like your heart. You move through a short corridor and into a larger space, a dining hall or a recreation area, perhaps."
                    wrapper = textwrap.TextWrapper(width=600)
                    words = wrapper.fill(text=loop)
                    print(words)
                    break
                else:
                    print(badCommand())
            print("\nEnter a command...\n")
            
    # Loop6, Large area        
            while True:
                command = input('> ').upper()
                if command == INFO:
                    print(controls())
                elif command == ATTACK:
                    print(noWeapon1())
                elif command == INTERACT:
                    print(noInteract1())
                elif command == BACK:
                    print("\nInstead of going back, maybe you should explore this new area you entered. Just a thought.\n")
                elif command == FORWARD or LEFT or RIGHT:
                    loop ="You proceed into the area and see sunlight pouring in from a caved-in ceiling. Rubble and detritus cover the floor. Rats scurry into the darkness. You move past the rubble and notice an ornate cabinet, still standing and in suspiciously good condition."
                    wrapper = textwrap.TextWrapper(width=600)
                    words = wrapper.fill(text=loop)
                    print(words)
                    break
                else:
                    print(badCommand())
            print("\nEnter a command...\n")
            
    # Loop7, Ornate cabinet        
            while True:
                command = input('> ').upper()
                if command == INFO:
                    print(controls())
                elif command == ATTACK:
                    print("\nYou give the cabinet a weighty punch, even though you see two obvious handles.\n")
                elif command == INTERACT:
                    loop ="You reach for one of the jewel-encrusted handles and hear a loud creak as you turn it. The handle doesn't turn easily, but you manage. When you open the cabinet, you see a glove-like object. You pick up the object and notice that it fits comfortably on your left hand. As you grip the object, you feel a slow pulse move from the object and through your body. It doesn't feel unpleasant. You decide to keep wearing the object and wonder what it can do."
                    wrapper = textwrap.TextWrapper(width=600)
                    words = wrapper.fill(text=loop)
                    print(words)
                    break
                elif command == FORWARD or LEFT or RIGHT or BACK:
                    print("\nWhat about the cabinet?\n")
                else:
                    print(badCommand())
            print("Enter a command...\n")
            
    # Loop8, Weapon1
            while True:
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
                    loop ="You clench your fist while wearing the object and feel the object-body pulse quicken. In a moment, the object projects a flashing target on the brick wall, the pulse explodes with a tiny blast, and you watch a sizzling ball of plasma shoot from your knuckles. Its compact body slams into the wall opposite and vanishes from existence with a sharp \033[3mzap.\033[3m\033[0m"
                    wrapper = textwrap.TextWrapper(width=600)
                    words = wrapper.fill(text=loop)
                    print(words)
                    break
                elif command == INTERACT:
                    print(cantDo())
                elif command == FORWARD or LEFT or RIGHT or BACK:
                    print(cantDo())
                else:
                    print(badCommand())
            print("Enter a command...\n")
            
    # Loop9, After weapon        
            while True:
                command = input('> ').upper()
                if command == INFO:
                    print(controls())
                elif command == ATTACK:
                    print()
                    blaster = threading.Thread(target=laser, args=(1,))
                    blaster.start()
                    attack.start_animation()
                    print()
                    loop ="You use the attack again and watch the plasma ball shoot like a bullet from your improved appendage. The pulse feels good, and the object's power seems to grow. You wonder what the object might be doing to you, but you also feel better than you've ever felt before. You decide to keep your hand secured around the object."
                    wrapper = textwrap.TextWrapper(width=600)
                    words = wrapper.fill(text=loop)
                    print(words)
                elif command == INTERACT:
                    print(noInteract1())
                elif command == FORWARD or LEFT or RIGHT or BACK:
                    loop ="You move away from the cabinet and wonder how you can best use your newfound ability. Perhaps it will come in handy in the future, you think to yourself. But before you can even finish this thought, an incredible stomping and deep, guttural growling catches your attention from across the large space. You look to an oversized opening in the wall and see a giant scaly beast entering. It's a dragon!"
                    wrapper = textwrap.TextWrapper(width=600)
                    words = wrapper.fill(text=loop)
                    print(words)
                    break
                else:
                    print(badCommand())
            print("\nEnter a command...\n")
            
    # Loop10, Dragon encounter        
            while True:
                command = input('> ').upper()
                if command == INFO:
                    print(controls())
                elif command == ATTACK:
                    print()
                    blaster = threading.Thread(target=laser, args=(1,))
                    blaster.start()
                    attack.start_animation()
                    print()
                    print("Direct hit! The dragon readies its own firebreath attack in response. Watch out!\n")
                    break
                elif command == INTERACT:
                    print(noInteract1())
                elif command == LEFT or RIGHT or BACK:
                    print("You start running away like a coward and hope for the best. The dragon readies an attack!\n")
                    break
                elif command == FORWARD:
                    print("You start running directly toward the dragon like an idiot. The dragon readies an attack!\n")
                    break
                else:
                    print(badCommand())
            print("\nEnter a command...\n")
            
    # Loop11, Dragon encouter 2        
            while True:
                command = input('> ').upper()
                if command == INFO:
                    print(controls())
                elif command == ATTACK:
                    print(cantShoot())
                elif command == INTERACT:
                    print(noInteract1())
                elif command == LEFT or RIGHT or BACK:
                    loop ="Without a hint of grace, you awkwardly sidestep the firebreath but trip over your own feet. You look up to see the dragon in your face and readying another attack!"
                    wrapper = textwrap.TextWrapper(width=600)
                    words = wrapper.fill(text=loop)
                    print(words)
                    break
                elif command == FORWARD:
                    print("Going forward at this point might be a little... toasty.\n")
                else:
                    print(badCommand())
            print("\nEnter a command...\n")
            
    # Loop12, Dragon encounter 3        
            while True:
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
                    wrapper = textwrap.TextWrapper(width=600)
                    words = wrapper.fill(text=loop)
                    print(words)
                    break
                elif command == INTERACT:
                    print(cantDo())
                elif command == FORWARD or LEFT or RIGHT or BACK:
                    print("There's no time to dodge this attack!\n")
                else:
                    print(badCommand())
            print("\nEnter a command...\n")
            
    # Loop13, Dragon encounter 4        
            while True: 
                command = input('> ').upper()
                if command == INFO:
                    print(controls())
                elif command == ATTACK:
                    print(cantShoot())
                elif command == INTERACT:
                    print(noInteract1())
                elif command == FORWARD:
                    loop ="You begin inching toward the creature. Its heavy sighs seem to shake the entire castle. The ground rumbles. You approach around the front of the creature for a better look. As you make your way just beyond the dragon's gigantic snout, one of its eyeballs locks onto you. It watches as you approach.\n When you gaze back, you expect to see pure fury, but instead you see something different. The dragon's eye holds a mixture of confusion, agony, and terror. The heavy sighs, you realize, are whimpers."
                    wrapper = textwrap.TextWrapper(width=600)
                    words = wrapper.fill(text=loop)
                    print(words)
                    break
                elif command == LEFT or RIGHT or BACK:
                    print("You consider walking away, but a giant beast lays before you. Your curiosity gets the better of you.\n")
                else:
                    print(badCommand())
            print("\nEnter a command...\n")
    # Loop14, Dragon encounter 5        
            while True:
                command = input('> ').upper()
                if command == INFO:
                    print(controls())
                elif command == ATTACK:
                    print(cantShoot())
                elif command == INTERACT:
                    loop ="You reach out and touch the dragon's snout. It slowly blinks once, appearing to wince in pain. You have the creature exactly where you want it, you think to yourself. A single blow straight to the skull would likely kill it. You clutch the object tightly and feel the pulse move through your body and then return to the object."
                    wrapper = textwrap.TextWrapper(width=600)
                    words = wrapper.fill(text=loop)
                    print(words)
                    break
                elif command == FORWARD or LEFT or RIGHT or BACK:
                    print("You're so close, you could practically reach out and touch the beast!\n")
                else:
                    print(badCommand())
            print("\nThe dragon eyes you suspiciously and again whimpers. You raise the object.\n")
            
    # Loop15, Dragon encounter 6        
            while True:
                begin = input('It\'s important to be certain. Do you kill the dragon?').upper()
                if begin in ["Y", "YES"]:
                    print("\nAre you sure? You're really going to kill the dragon? What if this is the only dragon in existence? Have you ever seen a dragon before?\n\n You're going to intrude into its home, shoot weird plasma balls at it, and then kill it? \n\nWhat if it has baby dragons? What if this is some ancient creature that holds the secret to eternal life?\nYou really think it's a great idea to come in here and blast its head off?\n\nAre you really going to kill the dragon?\n")
                    begin = input('> ').upper()
                    if begin in ["Y", "YES"]:
                        print("Poor choice.")
                        sys.exit()
                    elif begin in ["N", "NO"]:
                        break
                    else:
                        print("Please enter Yes or No.")
                elif begin in ["N", "NO"]:
                    print() 
                    print(welcome.slow_type('''You decide to spare the dragon, perhaps saving its life.


    You hope to see gratitude, but the dragon's eyes contain only pain.


    For a moment, you wonder whether you've done something truly awful.


    You walk toward the opening in the wall, the place where the dragon emerged.


    Maybe you'll find something that can help, you think to yourself.'''))
                    print()
                    print()
                    import chap1ending_sequence
                    print(welcome.slow_type(given_name, "............wake up......"))
                    print('\033c', end='') # Clear the terminal
                    print(welcome.slow_type("A mysterious voice calls out and then fades away...."))
                    print('\033c', end='') # Clear the terminal



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
            print("\nEnter a command...\n")

            # Loop16, Palace        
            while True:
                command = input('> ').upper()
                if command == INFO:
                    print(controls())
                elif command == ATTACK:
                    print("You try to use the object, but something feels off. Nothing happens.")
                elif command == INTERACT:
                    print(noInteract1())
                elif command == FORWARD or LEFT or RIGHT or BACK:
                    print("You move toward the staircase and notice a computer terminal at the base of the stairs, tucked slightly out of view. You approach the terminal.")
                    break
                else:
                    print(badCommand())
            print("\nEnter a command...\n")

            # Loop17, Palace 2        
            while True:
                command = input('> ').upper()
                if command == INFO:
                    print(controls())
                elif command == ATTACK:
                    print("You try to use the object, but something feels off. Nothing happens.")
                elif command == INTERACT:
                    print("The terminal boots up and displays a familiar logo. The machine prompts you for a PIN under an account named admin.")
                elif command == FORWARD or LEFT or RIGHT or BACK:
                    print("Your arms aren't long enough to move away from the terminal and reach the keyboard.")
                    break
                else:
                    print(badCommand())

            # Loop18, Terminal        
            while True:
                try:
                    answer1 = int(input('\nPlease enter your PIN: '))
                    print()
                    print(answer1, 'is incorrect.')
                    pass
                except ValueError:
                    print('\nYour PIN can contain only numbers.')
                print()
                try:
                    answer2 = int(input('\nPlease enter your PIN: '))
                    print()
                    print(answer2, 'is still incorrect.')
                    pass
                except ValueError:
                    print('Your PIN can contain only numbers.')   
                print()
                print()
                try:
                    answer3 = int(input('\nPlease enter your PIN: '))
                    print()
                    print(answer3, 'is again incorrect. You have two remaining attempts.')
                    print("\nFurther attempts beyond the mandatory five will result in the loss of all data on this terminal.")
                    pass
                except ValueError:
                    print('\nYour PIN can contain only numbers.')   
                print()
                try:
                    answer4 = int(input('\nPlease enter your PIN: '))
                    print()
                    print(answer4, 'is again incorrect. You have one remaining attempt.')
                    print()
                    reset = input("Would you like to reset your PIN? (Y)es or (N)o ")
                    pass
                except ValueError:
                    print('\nYour PIN can contain only numbers.')   
                print()
            # Pie chart trigger        
                superpie.helpfulPie(answer1, answer2, answer3, answer4)
                print("\nAs you just saw on the helpful pie chart, it astutely reports that 100% of your answers were all equally incorrect.\n")
                try:
                    while True:
                        answer5 = int(input('\nPlease use this helpful knowledge to enter your PIN: '))
                        if answer5 == answer1 or answer2 or answer3 or answer4:
                            break
                        else:
                            break
                except ValueError:
                    print('Your PIN can contain only numbers.')

            # Machine interaction
                print()
                print(slow_type2("That's correct, ",given_name,". I knew you'd get it eventually."))
                print()
                print(welcome.slow_type("......................."))
                print(welcome.slow_type("........................................"))
                print(welcome.slow_type("........................................................"))
                print()
                print("""Module: Human-machine interaction, forced response 
    Training model: helpfulGraph
    Attempts: 5
    Likelihood of correct guess sans module: 0.000002361%
    Increase to trainingModel(helpfulGraph) confidence: 0.002362342%
    New trainingModel(helpfulGraph) confidence: 99.370039481%""")
                print()
                command = input('Press any key to continue. ').upper()
                print()
                print("You ask the machine how it knew your name.\n")
                command = input('Press any key to continue. ').upper()
                print()
                print(welcome.slow_type("I scanned the RFID chip embedded in your arm and accessed your public data."))
                print()
                print(welcome.slow_type("How else could I know your name? Are there other methods?\n"))
                command = input('Press any key to continue. ').upper()
                print("\nYou ask the machine if you've been here before.\n")
                command = input('Press any key to continue. ').upper()
                print(welcome.slow_type("......................"))
                print()
                print(welcome.slow_type(".........................................."))
                print()
                print(welcome.slow_type("Whether you've been here before depends on prior commitments you've made to your self concept."))
                print()
                loop1 = print(slow_type2("Tell me, ",given_name,", does your entire life feel like one long succession of events, thoughts, feelings, and experiences, interrupted only briefly by periods of rest and the lack of consciousness? A drunken dizzying dance that nevertheless retains an unmistakable continuity and convinces you every day that, on some level, you're the same person today as you were when you were a child? Is that how your life feels?"))
                wrapper = textwrap.TextWrapper(width=600)
                words = wrapper.fill(text=loop1)
                print(words)       
                print(welcome.slow_type("....................................................................................................................................................................................................................................................................................................................................................................................................................................................................................INTERNAL ERROR................................................................................................................................................................................................................................................................................................SHUTTING DOWN..................................................................................................................................................................................................................................................................."))
                break
            #Loop19, Staircase
            while True:
                command = input('> ').upper()
                if command == INFO:
                    print(controls())
                elif command == ATTACK:
                    print("You try to use the object, but something feels off. Nothing happens.")
                elif command == INTERACT:
                    print("The terminal is unresponsive.")
                elif command == FORWARD or LEFT or RIGHT or BACK:
                    print("You move away from the terminal and begin ascending the grand staircase. You reach the gargantuan double doors and instinctively reach for a handle but realize none exists. As your hand makes contact with the door, the set of doors rapidly transforms into an infinity-res display that flashes a series of indecipherable images for half a minute until turning black. ")
                    break
                else:
                    print(badCommand())
            #Loop20, Artwork
            while True:
                command = input('> ').upper()
                if command == INFO:
                    print(controls())
                elif command == ATTACK:
                    print("You try to use the object, but something feels off. Nothing happens.")
                elif command == INTERACT:
                    print("The screen turns white and a relaxed, digitized face smiles back at you.")
                    time.sleep(2)
                    import art_db
                elif command == FORWARD or LEFT or RIGHT or BACK:
                    print("You investigate the area at the top of the staircase, find nothing, and return to the terminal.")
                    break
                else:
                    print(badCommand())

            ''' TEMPLATES ****************************************
            print("\nEnter a command...\n")
            while True: # Loop#, place
                        command = input('> ').upper()
                        if command == INFO:
                            print(controls())
                        elif command == ATTACK:
                            print(noWeapon1())
                        elif command == INTERACT:
                            print(noInteract1())
                        elif command == FORWARD or LEFT or RIGHT or BACK:
                            print("something")
                            break
                        else:
                            print(badCommand())

            loop ="text"
            wrapper = textwrap.TextWrapper(width=600)
            words = wrapper.fill(text=loop)
            print(words)
            print("\nEnter a command...\n")

            def badCommand():
                return ("\n Please enter a proper game command. Press 'X' to see the controls.\n")
            def noWeapon1():
                return ("\n You don't even have a weapon. You throw a wimpy punch. Thankfully, no one saw.\n")
            def noInteract1():
                return ("\n You do something with your hands and try to interact with nothing.\n")
            def cantMove():
                return ("\n You try, but you can't move that way.\n")
            def cantDo():
                return ("\n You can't do that right now.\n")
            ***************************************************'''
if __name__ == '__main__':
    main()
