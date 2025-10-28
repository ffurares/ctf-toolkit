#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess as su
from termcolor import colored
from time import sleep
import os

class Buster:

    @staticmethod
    def clear(): #clear screen
        su.run("clear", shell=True)
    
    @staticmethod
    def press_continue(): #press enter for continue
        try:
            enter = input(colored("Press Enter For Continue...", "light_blue", attrs=['bold']))
            return
        except (KeyboardInterrupt, EOFError):
            return
        
    @staticmethod
    def run():
        while True:
            Buster.clear()
            print(colored(fr"""
  ____  ___  ____  _   _ ____ _____ _____ ____  
 / ___|/ _ \| __ )| | | / ___|_   _| ____|  _ \ 
| |  _| | | |  _ \| | | \___ \ | | |  _| | |_) |
| |_| | |_| | |_) | |_| |___) || | | |___|  _ < 
 \____|\___/|____/ \___/|____/ |_| |_____|_| \_\   
-------------------------------------------------
{colored("[01] ", "red", attrs=['bold'])}- {colored("gobuster dir -u <url> -w <wordlist>", "green", attrs=['bold'])}
{colored("[02] ", "red", attrs=['bold'])}- {colored("gobuster dir -u <url> -x php,html,txt,bak -w <wordlist>", "green", attrs=['bold'])}                   
{colored("[03] ", "red", attrs=['bold'])}- {colored("gobuster dir -u <url> -w <wordlist> -t <thread> -o <output_file>", "green", attrs=['bold'])}
{colored("[04] ", "red", attrs=['bold'])}- {colored("gobuster dir -u <url> -x php,html,txt,bak -w <wordlist> -t <thread> -o <output_file>", "green", attrs=['bold'])}
{colored("[00] ", "red", attrs=['bold'])}- {colored("Back to Main Menu", "green", attrs=['bold'])}
""", "blue", attrs=['bold']))
            
            try:
            
                enter = int(input(colored("Enter : ", "light_blue", attrs=['bold']))) #Get enter from user
            
            except (KeyboardInterrupt, EOFError, ValueError):
                break

            #Back to main menu option
            if enter == 0:
                break

            #[01] Gobuster scan option
            elif enter == 1:
                try:
                    Buster.clear()
                    
                    url = input(colored("Enter Target URL : ", "light_blue", attrs=['bold'])) #Enter url
                    if not url: #If user not input a valid url
                        print(colored("Target URL Required...", "red", attrs=['bold']))
                        sleep(1)
                        continue
                    
                    if not (url.startswith("https://") or url.startswith("http://")): #Check url if not starts with http or https, add in url variable
                        url = "http://" + url


                    wordlist = input(colored("Enter Wordlist File Path : ", "light_blue", attrs=['bold'])) #Get wordlist file
                    
                    if os.path.exists(wordlist): #If wordlist file found :
                        su.run(["gobuster", "dir", "-u", url, "-w", wordlist], check=True) #Run Code
                        Buster.press_continue() #Press Enter Input

                    else: #If wordlist file not found
                        print(colored("Wordlist File Not Found...", "red", attrs=['bold']))
                        sleep(1)
                        continue

                #Debugging
                except su.CalledProcessError as e:
                    print(colored(f"[-] Error Occured ---> {e}", "red", attrs=['bold']))
                    Buster.press_continue()
                    
                except (KeyboardInterrupt, EOFError):
                    Buster.press_continue()

            #[02] Gobuster scan option
            elif enter == 2:
                try:
                    Buster.clear()
                    
                    url = input(colored("Enter Target URL : ", "light_blue", attrs=['bold'])) #Enter url
                    if not url:#If user not input a valid url
                        print(colored("Target URL Required...", "red", attrs=['bold']))
                        sleep(1)
                        continue
                    wordlist = input(colored("Enter Wordlist File Path : ", "light_blue", attrs=['bold'])) #Enter wordlist file
                    
                    if os.path.exists(wordlist): #If wordlist file found :
                        su.run(["gobuster", "dir", "-u", url, "-x", "php,html,txt,bak", "-w", wordlist], check=True) #Run code
                        Buster.press_continue()

                    else: #If wordlist file not found
                        print(colored("Wordlist File Not Found...", "red", attrs=['bold']))
                        sleep(1)
                        continue


                except su.CalledProcessError as e:
                    print(colored(f"[-] Error Occured ---> {e}", "red", attrs=['bold']))
                    Buster.press_continue()
                    
                except (KeyboardInterrupt, EOFError):
                    Buster.press_continue()

            #[03] Gobuster scan option
            elif enter == 3:
                try:
                    Buster.clear()
                    
                    url = input(colored("Enter Target URL : ", "light_blue", attrs=['bold'])) #Enter url
                    if not url:#If user not input a valid url
                        print(colored("Target URL Required...", "red", attrs=['bold']))
                        sleep(1)
                        continue
                    
                    thread = int(input(colored("Enter thread count (0 - 100) : ", "light_blue", attrs=['bold']))) #Enter thread count

                    if thread <= 0 or thread > 100: #check thread input
                        print(colored("Invalid Thread Option...", "red", attrs=['bold']))
                        sleep(1)
                        continue                    
                    
                    output_file = input(colored("Enter Output File : ", "light_blue", attrs=['bold'])) #Enter output_file
                    if not output_file:
                        print(colored("[-] Output File Required...", "red", attrs=['bold']))
                        sleep(1)
                        continue

                    wordlist = input(colored("Enter Wordlist File Path : ", "light_blue", attrs=['bold'])) #Enter wordlist file
                    
                    if os.path.exists(wordlist): #If wordlist file found :
                        su.run(["gobuster", "dir", "-u", url, "-w", wordlist, "-t", str(thread), "-o", output_file], check=True) #Run code
                        Buster.press_continue()

                    else: #If wordlist file not found
                        print(colored("Wordlist File Not Found...", "red", attrs=['bold']))
                        sleep(1)
                        continue

                #Debugging
                except su.CalledProcessError as e:
                    print(colored(f"[-] Error Occured ---> {e}", "red", attrs=['bold']))
                    Buster.press_continue()
                    
                except (KeyboardInterrupt, EOFError):
                    Buster.press_continue()

                except ValueError:
                    print(colored("[-] Invalid Value...", "red", attrs=['bold']))
                    sleep(1)
                    continue


            elif enter == 4:
                try:
                    Buster.clear()
                    
                    url = input(colored("Enter Target URL : ", "light_blue", attrs=['bold'])) #Enter url
                    if not url:#If user not input a valid url
                        print(colored("Target URL Required...", "red", attrs=['bold']))
                        sleep(1)
                        continue
                    
                    thread = int(input(colored("Enter thread count (0 - 100) : ", "light_blue", attrs=['bold']))) #Enter thread count

                    if thread <= 0 or thread > 100: #check thread input
                        print(colored("Invalid Thread Option...", "red", attrs=['bold']))
                        sleep(1)
                        continue                    
                    
                    output_file = input(colored("Enter Output File : ", "light_blue", attrs=['bold'])) #Enter output_file
                    if not output_file:
                        print(colored("[-] Output File Required...", "red", attrs=['bold']))
                        sleep(1)
                        continue

                    wordlist = input(colored("Enter Wordlist File Path : ", "light_blue", attrs=['bold'])) #Enter wordlist file
                    
                    if os.path.exists(wordlist): #If wordlist file found :
                        su.run(["gobuster", "dir", "-u", url, "-x", "php,html,txt,bak", "-w", wordlist, "-t", str(thread), "-o", output_file], check=True) #Run code
                        Buster.press_continue()

                    else: #If wordlist file not found
                        print(colored("Wordlist File Not Found...", "red", attrs=['bold']))
                        sleep(1)
                        continue

                #Debugging
                except su.CalledProcessError as e:
                    print(colored(f"[-] Error Occured ---> {e}", "red", attrs=['bold']))
                    Buster.press_continue()
                    
                except (KeyboardInterrupt, EOFError):
                    Buster.press_continue()

                except ValueError:
                    print(colored("[-] Invalid Value...", "red", attrs=['bold']))
                    sleep(1)
                    continue