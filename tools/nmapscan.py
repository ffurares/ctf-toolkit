#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess as su
from termcolor import colored
from time import sleep


class Nmap:
    
    @staticmethod
    def clear(): #clear screen
        su.run("clear", shell=True)
    
    @staticmethod
    def press_continue(): #Press enter for continue function
        try:
            enter = input(colored("Press Enter For Continue...", "light_blue", attrs=['bold']))
            return
        except (KeyboardInterrupt,EOFError):
            return
        
    @staticmethod
    def run(): #Main Function
        while True:
            Nmap.clear()
            print(colored(fr"""
 _   _ __  __    _    ____    ____   ____    _    _   _ 
| \ | |  \/  |  / \  |  _ \  / ___| / ___|  / \  | \ | |
|  \| | |\/| | / _ \ | |_) | \___ \| |     / _ \ |  \| |
| |\  | |  | |/ ___ \|  __/   ___) | |___ / ___ \| |\  |
|_| \_|_|  |_/_/   \_\_|     |____/ \____/_/   \_\_| \_|         
--------------------------------------------------------
{colored("[*] This menu provides basic automated Nmap scans only. Use manual commands for more advanced or specific options.", "white", "on_red", attrs=['bold'])}
{colored("[01] ", "red", attrs=['bold'])}- {colored("nmap <host>", "green", attrs=['bold'])}                         
{colored("[02] ", "red", attrs=['bold'])}- {colored("nmap -sS -Pn -n -A <host>", "green", attrs=['bold'])} {colored("Recommended", "white", "on_red", attrs=['bold'])}
{colored("[03] ", "red", attrs=['bold'])}- {colored("nmap -sT -Pn -n -A <host> -oN <output_file> -T <timing>", "green", attrs=['bold'])} {colored("Recommended", "white", "on_red", attrs=['bold'])}
{colored("[04] ", "red", attrs=['bold'])}- {colored("nmap -sS -A -oN <output_file> <host>", "green", attrs=['bold'])}
{colored("[05] ", "red", attrs=['bold'])}- {colored("nmap -sS -sV <host>", "green", attrs=['bold'])}
{colored("[06] ", "red", attrs=['bold'])}- {colored("nmap -sS -sC <host>", "green", attrs=['bold'])}
{colored("[07] ", "red", attrs=['bold'])}- {colored("nmap -sS -O <host>", "green", attrs=['bold'])}
{colored("[08] ", "red", attrs=['bold'])}- {colored("nmap -sS -T4 -A <host>", "green", attrs=['bold'])}
{colored("[09] ", "red", attrs=['bold'])}- {colored("nmap -sS -A -p- <host>", "green", attrs=['bold'])}
{colored("[10] ", "red", attrs=['bold'])}- {colored("nmap -sU <host>", "green", attrs=['bold'])}
{colored("[00] ", "red", attrs=['bold'])}- {colored("Back to Main Menu", "green", attrs=['bold'])}         
                          
""", "light_blue", attrs=['bold'])) #Print Main Menu
            
            try:
                choice = int(input(colored("Enter : ", "light_blue", attrs=['bold']))) #Get Enter
            except (KeyboardInterrupt, EOFError):
                break
            except ValueError:
                print(colored("Invalid Option...", "red", attrs=['bold']))
                sleep(1)
                continue

            #Exit Option
            if choice == 0: 
                break

            #Basic nmap scan
            elif choice == 1:
                Nmap.clear()
                try:
                    
                    ip = input(colored("Enter Host : ", "light_blue", attrs=['bold'])) #Get ip
                    if not ip: #If user not enter ip address
                        print(colored("[-] Host Required...", "red", attrs=['bold']))
                        sleep(1)
                        continue
                    su.run(["nmap", ip], check=True) #Run code
                    Nmap.press_continue() #Press enter for continue
                except su.CalledProcessError as e:
                    print(colored(f"[-] Error Occured ---> {e}", "red", attrs=['bold']))
                    sleep(1.5)
                    continue
                
                except(KeyboardInterrupt, EOFError):
                    break
            
            #[02] Nmap Scan
            elif choice == 2:
                Nmap.clear()
                try:
                    
                    ip = input(colored("Enter Host : ", "light_blue", attrs=['bold'])) #Get ip
                    if not ip:
                        print(colored("[-] Host Required...", "red", attrs=['bold'])) #Warning
                        sleep(1)
                        continue
                    su.run(["sudo", "nmap", "-sS", "-Pn", "-n", "-A", ip], check=True) #Run code
                    Nmap.press_continue()
                except su.CalledProcessError as e:
                    print(colored(f"[-] Error Occured ---> {e}", "red", attrs=['bold']))
                    sleep(1.5)
                    continue

                except(KeyboardInterrupt, EOFError):
                    break

            #[03] Nmap scan
            elif choice == 3:
                Nmap.clear()

                try:
                    
                    ip = input(colored("Enter Host : ", "light_blue", attrs=['bold'])) #Get ip 
                    if not ip:
                        print(colored("[-] Host Required...", "red", attrs=['bold'])) #If not ip
                        sleep(1)
                        continue
                    output_file = input(colored("Enter Output File : ", "light_blue", attrs=['bold'])) #Get output_file
                    if not output_file:
                        print(colored("[-] Output File Required...", "red", attrs=['bold'])) #If not output_file
                        sleep(1)
                        continue

                    timing = int(input(colored("Enter Timing 0 - 5 : ", "light_blue", attrs=['bold']))) #Enter timing
                    if not timing or timing < 0 or timing > 5: #If timing not match pattern
                        print(colored("[-] Invalid Timing...", "red", attrs=['bold']))
                        sleep(1)
                        continue


                    su.run(["sudo", "nmap", "-sT", "-Pn", "-n", "-A", ip, "-oN", output_file, "-T", str(timing)], check=True) #Run Command
                    Nmap.press_continue() #Press enter for continue
                
                except su.CalledProcessError as e:
                    print(colored(f"[-] Error Occured ---> {e}", "red", attrs=['bold']))
                    sleep(1.5)
                    continue
                except (KeyboardInterrupt, EOFError):
                    break
                except ValueError:
                    print(colored("[-] Invalid Option...", "red", attrs=['bold']))
                    sleep(1)
                    continue
            
            #[04] Nmap Scan
            elif choice == 4:
                Nmap.clear()

                try:
                    ip = input(colored("Enter Host : ", "light_blue", attrs=['bold'])) #Get ip 
                    if not ip:
                        print(colored("[-] Host Required...", "red", attrs=['bold'])) #If not ip
                        sleep(1)
                        continue
                    output_file = input(colored("Enter Output File : ", "light_blue", attrs=['bold'])) #Get output_file
                    if not output_file:
                        print(colored("[-] Output File Required...", "red", attrs=['bold'])) #If not output_file
                        sleep(1)
                        continue

                    su.run(["sudo", "nmap", "-sS", "-A", "-oN", output_file, ip]) #Run code
                    Nmap.press_continue()
                
                except su.CalledProcessError as e:
                    print(colored(f"[-] Error Occured ---> {e}", "red", attrs=['bold']))
                    sleep(1.5)
                    continue
                
                except (KeyboardInterrupt, EOFError):
                    break

            #[05] Nmap Scan
            elif choice == 5:
                Nmap.clear()

                try:
                    ip = input(colored("Enter Host : ", "light_blue", attrs=['bold'])) #Get ip
                    if not ip:
                        print(colored("[-] Host Required...", "red", attrs=['bold']))
                        sleep(1)
                        continue

                    su.run(["sudo", "nmap", "-sS", "-sV", ip]) #Run Code
                    Nmap.press_continue()
                except (KeyboardInterrupt, EOFError):
                    break
                except su.CalledProcessError as e:
                    print(colored(f"[-] Error Occured ---> {e}", "red", attrs=['bold']))
                    sleep(1.5)
                    continue

            #[06] Nmap Scan
            elif choice == 6:
                Nmap.clear()

                try:
                    ip = input(colored("Enter Host : ", "light_blue", attrs=['bold'])) #Get ip
                    if not ip:
                        print(colored("[-] Host Required...", "red", attrs=['bold']))
                        sleep(1)
                        continue

                    su.run(["sudo", "nmap", "-sS", "-sC", ip]) #Run Code
                    Nmap.press_continue()
                except (KeyboardInterrupt, EOFError):
                    break
                except su.CalledProcessError as e:
                    print(colored(f"[-] Error Occured ---> {e}", "red", attrs=['bold']))
                    sleep(1.5)
                    continue

            #[07] Nmap Scan
            elif choice == 7:
                Nmap.clear()

                try:
                    ip = input(colored("Enter Host : ", "light_blue", attrs=['bold'])) #Get ip
                    if not ip:
                        print(colored("[-] Host Required...", "red", attrs=['bold']))
                        sleep(1)
                        continue

                    su.run(["sudo", "nmap", "-sS", "-O", ip]) #Run Code
                    Nmap.press_continue()

                except (KeyboardInterrupt, EOFError):
                    break
                except su.CalledProcessError as e:
                    print(colored(f"[-] Error Occured ---> {e}", "red", attrs=['bold']))
                    sleep(1.5)
                    continue

            #[08] Nmap Scan
            elif choice == 8:
                Nmap.clear()

                try:
                    ip = input(colored("Enter Host : ", "light_blue", attrs=['bold'])) #Get ip
                    if not ip:
                        print(colored("[-] Host Required...", "red", attrs=['bold']))
                        sleep(1)
                        continue

                    su.run(["sudo", "nmap", "-sS", "-T4", "-A", ip]) #Run Code
                    Nmap.press_continue()
                except (KeyboardInterrupt, EOFError):
                    break
                except su.CalledProcessError as e:
                    print(colored(f"[-] Error Occured ---> {e}", "red", attrs=['bold']))
                    sleep(1.5)
                    continue
                
            #[09] Nmap Scan
            elif choice == 9:
                Nmap.clear()

                try:
                    ip = input(colored("Enter Host : ", "light_blue", attrs=['bold'])) #Get ip
                    if not ip:
                        print(colored("[-] Host Required...", "red", attrs=['bold']))
                        sleep(1)
                        continue

                    su.run(["sudo", "nmap", "-sS", "-A", "-p-", ip]) #Run Code
                    Nmap.press_continue()
                except (KeyboardInterrupt, EOFError):
                    break
                except su.CalledProcessError as e:
                    print(colored(f"[-] Error Occured ---> {e}", "red", attrs=['bold']))
                    sleep(1.5)
                    continue

            #[10] Nmap Scan
            elif choice == 10:
                Nmap.clear()

                try:
                    ip = input(colored("Enter Host : ", "light_blue", attrs=['bold'])) #Get ip
                    if not ip:
                        print(colored("[-] Host Required...", "red", attrs=['bold']))
                        sleep(1)
                        continue

                    su.run(["sudo", "nmap", "-sU", ip]) #Run Code
                    Nmap.press_continue()

                except (KeyboardInterrupt, EOFError):
                    break
                except su.CalledProcessError as e:
                    print(colored(f"[-] Error Occured ---> {e}", "red", attrs=['bold']))
                    sleep(1.5)
                    continue