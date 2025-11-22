try:
    import sys                  # import all the dependencies
    import tomllib
    import pygame
    import queue
    import threading
    import time                 # temporary, delete!
    from puzzle import Puzzle
except Exception as error:      # in case it breaks
    print(f"failed to to import modules: {error}!")
    sys.exit(1)

__version__ = "prefunctional"

command_queue = queue.Queue()   # initialize the command queue
ready = False

def input_handler_loop():       # the loop that handles input
    global ready
    while True:
        if ready:
            command = input(">>> ")
            command_queue.put(command)
            ready = False

threading.Thread(target=input_handler_loop, daemon=True).start()    # spawn the input loop

def logo():
    print("===================")    # yummy logo
    print("L   III N N EEE N N")
    print("L    I  NNN E   NNN")
    print("L    I  NNN EEE NNN")
    print("L    I  NNN E   NNN")
    print("LLL III N N EEE N N")
    print("===================")
    print(f"version {__version__}")
    print("===================")

logo()

running = True                  # get ready for main loop
ready = True
    
while running:                  # main loop
    while not command_queue.empty():
        command = command_queue.get()
        command = command.split()
        if command[0] == "quit":
            print("bye")
            running = False

        elif command[0] == "about":
            try:
                if command[1] != None:
                    print(f"heh, you found the easter {command[1]}!")
            except:
                    pass
            logo()

        elif command[0] == "load":
            try:
                with open(command[1], "rb") as file:
                    config = tomllib.load(file)
                puzzle = Puzzle(config)
                print(f"loaded: {command[1]}")
            except Exception as error:
                print(f"failed to load: {error}!")

        elif command[0] == "state":
            try:
                print(puzzle.positions)
            except:
                print("no puzzle loaded!")
        
        elif command[0] == "move":
            try:
                puzzle.apply_move(command[1])
            except Exception as error:
                print(f"failed to move: {error}!")

        else:
            print("unkown command")
        if running:
            ready = True
    time.sleep(0.01)
