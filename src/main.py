try:
    import sys                  # import all the dependencies
    import tomllib
    import pygame
    import queue
    import threading
    import time                 # temporary, delete!
except Exception as error:      # in case it breaks
    print(f"failed to to import modules: {error}!")
    sys.exit(1)

__version__ = "2025.11.21.1"

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
        if command == "quit":
            running = False
        elif command == "about":
            logo()
        if running:
            ready = True
    time.sleep(0.01)
