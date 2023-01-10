import random
import time
import sys
import multiprocessing

sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=41, cols=130))

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

# Create 500 processes
for i in range(500):
    p = multiprocessing.Process(target=blinking_stars)
    processes.append(p)

# Start the processes
for p in processes:
    p.start()

# Wait for the processes to finish
for p in processes:
    p.join()


def blinking_stars2():
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

# Create 400 processes
for i in range(400):
    p = multiprocessing.Process(target=blinking_stars2)
    processes.append(p)

# Start the processes
for p in processes:
    p.start()

# Wait for the processes to finish
for p in processes:
    p.join()

def blinking_stars3():
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

# Create 300 processes
for i in range(300):
    p = multiprocessing.Process(target=blinking_stars3)
    processes.append(p)

# Start the processes
for p in processes:
    p.start()

# Wait for the processes to finish
for p in processes:
    p.join()

def blinking_stars4():
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

# Create 200 processes
for i in range(200):
    p = multiprocessing.Process(target=blinking_stars4)
    processes.append(p)

# Start the processes
for p in processes:
    p.start()

# Wait for the processes to finish
for p in processes:
    p.join()

print('\033c', end='') # Clear the terminal