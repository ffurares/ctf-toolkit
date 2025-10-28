#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess as su
from termcolor import colored

class Start:

    @staticmethod
    def clear(): # Clear Terminal
        su.run("clear", shell=True)

    @staticmethod
    def listen(): # Start Listener Funciton
        #Start Loop
        while True:
        
            Start.clear()

            try:
                print(colored("Press CTRL + ^C For Back Main Menu", "white", "on_red", attrs=['bold'])) # INFO
                port = int(input(colored("Enter The Port : ", "light_blue", attrs=['bold']))) # Get Port
                su.run(f"nc -lvnp {port}", shell=True) # Run Command
            except (KeyboardInterrupt, EOFError):
                break
            except ValueError:
                Start.clear()
                continue