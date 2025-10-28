#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess as su
from termcolor import colored
from time import sleep
import shutil
import os


class Runhydra:

    
    @staticmethod
    def clear(): #Clear Function
        su.run("clear", shell=True)

    @staticmethod
    def press_continue(): #Press Enter Function
        try:
            resp = input(colored("Press Enter For Continue...", "light_blue", attrs=['bold']))
            su.run("clear", shell=True)
            return
        except (KeyboardInterrupt,EOFError):
            Runhydra.clear()
            return

    @staticmethod
    def hydra_install(): #Install hydra if not installed yet
        try:
            ask = input(colored("Hydra is Not Installed On Your System. Do You Want To Install Now (Y/n) : ", "light_blue", attrs=['bold']))
            if ask in ["", "y", "yes", "Y"]:
                su.run("sudo apt-get -y install hydra", shell=True)
                Runhydra.clear()
                return False
            else:
                return False
        except (KeyboardInterrupt, EOFError):
            return False
        

    @staticmethod
    def ftpbrute():
        Runhydra.clear()

        try:
            host = input(colored("Enter Target IP Address : ", "light_blue", attrs=['bold'])).strip() #Host
            if not host:
                print(colored("[-] Target IP/hostname required.", "red", attrs=['bold']))
                sleep(1)
                Runhydra.clear()
                return

            port_in = input(colored("Enter Port (Default : 21) : ", "light_blue", attrs=['bold'])).strip() # Port
            thread_in = input(colored("Enter Thread (Default : 16) : ", "light_blue", attrs=['bold'])).strip() # Thread

            username = input(colored("Enter Username : ", "light_blue", attrs=['bold'])).strip() # Username
            if not username:
                print(colored("[-] Username required.", "red", attrs=['bold']))
                sleep(1)
                Runhydra.clear()
                return

            wordlist = input(colored("Enter Wordlist File Path : ", "light_blue", attrs=['bold'])).strip() # Wordlist
            if not wordlist or not os.path.isfile(wordlist):
                print(colored(f"[-] Wordlist file not found: {wordlist}", "red", attrs=['bold']))
                sleep(1)
                Runhydra.clear()
                return

            verbose = input(colored("Do You Want To Use Verbose Mode (Y/n) : ", "light_blue", attrs=['bold'])).strip().lower() # Verbose

            try:
                port = int(port_in) if port_in else 21
            except ValueError:
                print(colored("[-] Invalid port number.", "red", attrs=['bold']))
                sleep(1)
                Runhydra.clear()
                return

            try:
                threads = int(thread_in) if thread_in else 16
            except ValueError:
                print(colored("[-] Invalid thread count.", "red", attrs=['bold']))
                sleep(1)
                Runhydra.clear()
                return

            cmd = [
            "hydra",
            "-l", username,
            "-P", wordlist,
            f"ftp://{host}",
            "-s", str(port),
            "-t", str(threads)
        ]

            if verbose in ("", "y", "yes"):
                cmd.append("-VV")

            print(colored("[*] Running:", "cyan", attrs=['bold']), " ".join(cmd))
            try:
                su.run(cmd, check=True)
            except su.CalledProcessError as e:
                print(colored(f"[-] hydra exited with non-zero status: {e.returncode}", "red"))
                sleep(1.5)
                return
            except FileNotFoundError:
                print(colored("[-] Failed to execute hydra (file not found).", "red"))
                sleep(1.5)
                return
            except Exception as e:
                print(colored(f"[-] Unexpected error: {e}", "red"))
                sleep(1.5)
                return
            
        except (KeyboardInterrupt, EOFError):
            Runhydra.clear() 
            return



        
    @staticmethod
    def sshbrute(): #SSH BRUTE FORCE 
        Runhydra.clear()

        try:
            host = input(colored("Enter Target IP Address : ", "light_blue", attrs=['bold'])).strip() #Host
            if not host:
                print(colored("[-] Target IP/hostname required.", "red", attrs=['bold']))
                sleep(1)
                Runhydra.clear()
                return

            port_in = input(colored("Enter Port (Default : 22) : ", "light_blue", attrs=['bold'])).strip() # Port
            thread_in = input(colored("Enter Thread (Default : 16) : ", "light_blue", attrs=['bold'])).strip() # Thread

            username = input(colored("Enter Username : ", "light_blue", attrs=['bold'])).strip() # Username
            if not username:
                print(colored("[-] Username required.", "red", attrs=['bold']))
                sleep(1)
                Runhydra.clear()
                return

            wordlist = input(colored("Enter Wordlist File Path : ", "light_blue", attrs=['bold'])).strip() # Wordlist
            if not wordlist or not os.path.isfile(wordlist):
                print(colored(f"[-] Wordlist file not found: {wordlist}", "red", attrs=['bold']))
                sleep(1)
                Runhydra.clear()
                return

            verbose = input(colored("Do You Want To Use Verbose Mode (Y/n) : ", "light_blue", attrs=['bold'])).strip().lower() # Verbose

            try:
                port = int(port_in) if port_in else 22
            except ValueError:
                print(colored("[-] Invalid port number.", "red", attrs=['bold']))
                sleep(1)
                Runhydra.clear()
                return

            try:
                threads = int(thread_in) if thread_in else 16
            except ValueError:
                print(colored("[-] Invalid thread count.", "red", attrs=['bold']))
                sleep(1)
                Runhydra.clear()
                return

            cmd = [
            "hydra",
            "-l", username,
            "-P", wordlist,
            f"ssh://{host}",
            "-s", str(port),
            "-t", str(threads)
        ]

            if verbose in ("", "y", "yes"):
                cmd.append("-VV")

            print(colored("[*] Running:\n", "cyan", attrs=['bold']), " ".join(cmd))
            try:
                su.run(cmd, check=True)
            except su.CalledProcessError as e:
                print(colored(f"[-] hydra exited with non-zero status: {e.returncode}", "red"))
                sleep(1.5)
                return
            except FileNotFoundError:
                print(colored("[-] Failed to execute hydra (file not found).", "red"))
                sleep(1.5)
                return
            except Exception as e:
                print(colored(f"[-] Unexpected error: {e}", "red"))
                sleep(1.5)
                return
            
        except (KeyboardInterrupt, EOFError):
            Runhydra.clear() 
            return
        
    @staticmethod
    def run(): #Main Function
        Runhydra.clear()
            
        while True:
            check = shutil.which("hydra")
            if not check:
            
                try:
                    ask = input(colored("Hydra is Not Installed On Your System. Do You Want To Install Now (Y/n) : ", "light_blue", attrs=['bold']))
                    if ask in ["", "y", "yes", "Y"]:
                        su.run("sudo apt-get -y install hydra", shell=True)
                        Runhydra.clear()
                        continue
                    else:
                        break
                except (KeyboardInterrupt, EOFError):
                    break
            print(colored(rf"""
)      )  (      (                          )      )   (    
( /(   ( /(  )\ )   )\ )    (        *   )  ( /(   ( /(   )\ ) 
)\())  )\())(()/(  (()/(    )\     ` )  /(  )\())  )\()) (()/( 
((_)\  ((_)\  /(_))  /(_))((((_)(    ( )(_))((_)\  ((_)\   /(_))
_((_)__ ((_)(_))_  (_))   )\ _ )\  (_(_())   ((_)   ((_) (_))  
| || |\ \ / / |   \ | _ \  (_)_\(_) |_   _|  / _ \  / _ \ | |   
| __ | \ V /  | |) ||   /   / _ \     | |   | (_) || (_) || |__ 
|_||_|  |_|   |___/ |_|_\  /_/ \_\    |_|    \___/  \___/ |____|

{colored("[01] SSH  ...................................", "red", attrs=['bold'])}{colored("[Brute Force SSH Server]", "green", attrs=['bold'])}                      
{colored("[02] FTP  ...................................", "red", attrs=['bold'])}{colored("[Brute Force FTP Server]", "green", attrs=['bold'])}
{colored("[00] Exit .................................. ", "red", attrs=['bold'])}{colored("[Back to Main Menu]", "green", attrs=['bold'])}
    """, "magenta", attrs=['bold']))
            
            try:
                choice = int(input(colored("Enter : ", "light_blue", attrs=['bold'])))    
            except (KeyboardInterrupt,EOFError,ValueError):
                break

            if choice == 0:
                break
            elif choice == 1:
                Runhydra.sshbrute()
                Runhydra.press_continue()
                Runhydra.clear()
                continue
            elif choice == 2:
                Runhydra.ftpbrute()
                Runhydra.press_continue()
                continue
            else:
                Runhydra.clear()
                continue