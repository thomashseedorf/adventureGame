import random
import time
import multiprocessing


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
        for i in range(800):
            p = multiprocessing.Process(target=blinking_stars)
            processes.append(p)

        # Start the processes
        for p in processes:
            p.start()

        # Wait for the processes to finish
        for p in processes:
            p.join()
        run_once = False