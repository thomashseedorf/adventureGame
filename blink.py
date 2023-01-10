import random
import time
import sys
import multiprocessing
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=41, cols=130))

def create_process(i):
    def blinking_stars():
      while True:
        x = random.randint(0, 129)
        y = random.randint(0, 40)
        print("\033[{};{}H*".format(y, x))
        z = random.uniform(0, 2)
        time.sleep(z)
        print("\033[{};{}H ".format(y, x))
        time.sleep(z)
        print("\033[{};{}H*".format(y, x))
        z = random.uniform(0, 2)
        time.sleep(z)
        print("\033[{};{}H ".format(y, x))
        time.sleep(z)
        print("\033[{};{}H*".format(y, x))
        z = random.uniform(0, 2)
        time.sleep(z)
        print("\033[{};{}H ".format(y, x))
        time.sleep(z)
        print("\033[{};{}H*".format(y, x))
        z = random.uniform(0, 2)
        time.sleep(z)
        print("\033[{};{}H ".format(y, x))
        time.sleep(z)
        print("\033[{};{}H*".format(y, x))
        z = random.uniform(0, 2)
        time.sleep(z)
        print("\033[{};{}H ".format(y, x))
        time.sleep(z)
        print("\033[{};{}H*".format(y, x))
        z = random.uniform(0, 2)
        time.sleep(z)
        print("\033[{};{}H ".format(y, x))
        time.sleep(z)
        print("\033[{};{}H*".format(y, x))
        z = random.uniform(0, 2)
        time.sleep(z)
        print("\033[{};{}H ".format(y, x))
        time.sleep(z)
        print("\033[{};{}H*".format(y, x))
        z = random.uniform(0, 2)
        time.sleep(z)
        print("\033[{};{}H ".format(y, x))
        time.sleep(z)
        print("\033[{};{}H*".format(y, x))
        z = random.uniform(0, 2)
        time.sleep(z)
        print("\033[{};{}H ".format(y, x))
        time.sleep(z)
        print("\033[{};{}H*".format(y, x))
        z = random.uniform(0, 2)
        time.sleep(z)
        print("\033[{};{}H ".format(y, x))
        time.sleep(z)
    return multiprocessing.Process(target=blinking_stars)

processes175 = [create_process(i) for i in range(1, 175)]
processes150 = [create_process(i) for i in range(1, 150)]
processes125 = [create_process(i) for i in range(1, 125)]
processes100 = [create_process(i) for i in range(1, 100)]
processes75 = [create_process(i) for i in range(1, 75)]
processes50 = [create_process(i) for i in range(1, 50)]
processes25 = [create_process(i) for i in range(1, 25)]
processes10 = [create_process(i) for i in range(1, 10)]
processes5 = [create_process(i) for i in range(1, 5)]


print('\033c', end='') # Clear the terminal

for process in processes150:
  process.start()
  print('\033[?25l', end="")
time.sleep(3)
for process in processes150:
  process.terminate()

print('\033c', end='') # Clear the terminal

for process in processes125:
  process.start()
  print('\033[?25l', end="")
time.sleep(3)
for process in processes125:
  process.terminate()

print('\033c', end='') # Clear the terminal

for process in processes100:
  process.start()
  print('\033[?25l', end="")
time.sleep(3)
for process in processes100:
  process.terminate()

print('\033c', end='') # Clear the terminal

for process in processes50:
  process.start()
  print('\033[?25l', end="")
time.sleep(3)
for process in processes50:
  process.terminate()

print('\033c', end='') # Clear the terminal

for process in processes25:
  process.start()
  print('\033[?25l', end="")
time.sleep(3)
for process in processes25:
  process.terminate()

print('\033c', end='') # Clear the terminal

for process in processes10:
  process.start()
  print('\033[?25l', end="")
time.sleep(3)
for process in processes10:
  process.terminate()

print('\033c', end='') # Clear the terminal

for process in processes5:
  process.start()
  print('\033[?25l', end="")
time.sleep(3)
for process in processes5:
  process.terminate()

print('\033c', end='') # Clear the terminal