#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib
import subprocess as su
from termcolor import colored

class Hash:

    @staticmethod
    def press_continue():
        try:
            resp = input(colored("Press Enter For Continue...", "light_blue", attrs=['bold']))
            su.run("clear", shell=True)
            return
        except (KeyboardInterrupt,EOFError):
            Hash.clear()
            return
        
    #Terminal Clear Function
    @staticmethod
    def clear():
        su.run("clear", shell=True)

    #Main Function
    @staticmethod
    def hash():
        Hash.clear()
        while True:
            print(colored(fr'''
 _____                                                      _____ 
( ___ )----------------------------------------------------( ___ )
 |   |                                                      |   | 
 |   |  _   _    _    ____  _   _   _____ ___   ___  _      |   | 
 |   | | | | |  / \  / ___|| | | | |_   _/ _ \ / _ \| |     |   | 
 |   | | |_| | / _ \ \___ \| |_| |   | || | | | | | | |     |   | 
 |   | |  _  |/ ___ \ ___) |  _  |   | || |_| | |_| | |___  |   | 
 |   | |_| |_/_/   \_\____/|_| |_|   |_| \___/ \___/|_____| |   | 
 |___|                                                      |___| 
(_____)----------------------------------------------------(_____)

{colored("[01] - MD5      .......................", "red", attrs=['bold'])}{colored("[Create MD5 Hash]", "green", attrs=['bold'])}
{colored("[02] - SHA-1    .......................", "red", attrs=['bold'])}{colored("[Create SHA-1 Hash]", "green", attrs=['bold'])}
{colored("[03] - SHA-256  .......................", "red", attrs=['bold'])}{colored("[Create SHA-256 Hash]", "green", attrs=['bold'])}
{colored("[04] - SHA-512  .......................", "red", attrs=['bold'])}{colored("[Create SHA-512]", "green", attrs=['bold'])}
{colored("[00] - Exit     .......................", "red", attrs=['bold'])}{colored("[Main Menu]", "green", attrs=['bold'])}
    ''', "light_blue", attrs=['bold']))
            
            try:
                choice = int(input(colored("Enter : ", "green", attrs=['bold']))) # User Input
            except (KeyboardInterrupt, EOFError, ValueError):
                break
            
            if choice == 1:
                
                Hash.clear() # Clear
                
                try:
                    value = input(colored("Enter : ", "green", attrs=['bold'])).encode() # Get Clear Text From User
                except (KeyboardInterrupt, EOFError):
                    break
                
                hash = hashlib.md5(value).hexdigest() #MD-5 Hash
                print(colored("MD5 Hash : ", "light_blue", attrs=['bold']) + colored(hash, "green", attrs=['bold'])) #Print Hash Value

                Hash.press_continue() #Press Any Key For Continue
            
            elif choice == 2:
                
                Hash.clear()

                try:
                    value = input(colored("Enter : ", "green", attrs=['bold'])).encode()
                except (KeyboardInterrupt, EOFError):
                    break

                hash = hashlib.sha1(value).hexdigest() #SHA-1 HASH
                print(colored("SHA-1 Hash : ", "light_blue", attrs=['bold']) + colored(hash, "green", attrs=['bold'])) #Print Hash Value

                Hash.press_continue()

            elif choice == 3:
                
                Hash.clear()
                try:
                    value = input(colored("Enter : ", "green", attrs=['bold'])).encode()
                except (KeyboardInterrupt, EOFError):
                    break

                hash = hashlib.sha256(value).hexdigest() #SHA-256 HASH
                print(colored("SHA-256 Hash : ", "light_blue", attrs=['bold']) + colored(hash, "green", attrs=['bold'])) #Print Hash Value

                Hash.press_continue()
            
            elif choice == 4:
                Hash.clear()

                try:
                    value = input(colored("Enter : ", "green", attrs=['bold'])).encode()
                except (KeyboardInterrupt, EOFError):
                    break

                hash = hashlib.sha512(value).hexdigest() #SHA-512 HASH
                print(colored("SHA-512 Hash : ", "light_blue", attrs=['bold']) + colored(hash, "green", attrs=['bold'])) #Print Hash Value

                Hash.press_continue()
            
            elif choice == 0:
                break
            else:
                Hash.clear()
                continue
