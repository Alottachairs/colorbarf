# Color Barf
# by alottachairs
# 2023
# a simple terminal screensaver

import os
import time
import threading
import random as r
from pyfiglet import figlet_format
from termcolor import cprint

# Main Application functions
class App():
    def __init__(self): # When App launches, print welcome message and get input
        prompt = ""
        line = "-"
        welcome_message = figlet_format("Color Barf")
        cprint(line * 50,"blue")
        cprint(welcome_message, "green")
        cprint(line * 50,"yellow")
        prompt = input("Input Word: ")

        self.run(prompt=prompt) # After input, run the barf sequence

    def run(self, prompt):
        prompt = prompt
        inputLength = len(prompt)+1
        terminal = os.get_terminal_size()
        lines = terminal.lines
        columns = terminal.columns
        colors = ["black", "red",
                  "green", "yellow", 
                  "blue", "magenta",
                  "cyan", "white",
                  "light_grey", "dark_grey",
                  "light_red", "light_green",
                  "light_yellow", "light_blue",
                  "light_magenta", "light_cyan"]
        running = True
        def print_line(prompt,colors):
            for j in range(columns//inputLength):
                cprint(prompt, colors[r.randrange(0,len(colors))], end=" ")
        
        count = 0

        while(running): 
            count += 1
            print_line(prompt = prompt, colors=colors)
            time.sleep(0.05)
            print()

if __name__ == "__main__":
    app = App()
