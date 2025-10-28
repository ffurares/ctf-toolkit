#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from termcolor import colored
import subprocess as su
from time import sleep
from common import installer
from git import gitinstaller


class Commons:

    @staticmethod
    def clear():
        su.run("clear", shell=True)

    # Exit Message
    @staticmethod
    def bye():
        print(colored("Thank's For Using...", "green", attrs=['bold']))

    # Ask User For Continue
    @staticmethod
    def ask_continue():
        try:
            resp = input(colored("\nDo you want to continue (Y/n) : ", "light_blue", attrs=['bold']))
            su.run("clear", shell=True)
            return resp.strip().lower() in ("", "y", "yes")
        except (KeyboardInterrupt, EOFError):
            print(colored("\nThanks For Using...", "green", attrs=['bold']))
            sleep(0.5)
            return False

    # Installation Menu
    @staticmethod
    def install_menu():
        
        print(colored(fr"""
┌─────────────────────────────────────────────────────────────────────────────┐
│ _____ ___   ___  _       ___ _   _ ____ _____  _    _     _     _____ ____  │
│|_   _/ _ \ / _ \| |     |_ _| \ | / ___|_   _|/ \  | |   | |   | ____|  _ \ │
│  | || | | | | | | |      | ||  \| \___ \ | | / _ \ | |   | |   |  _| | |_) |│
│  | || |_| | |_| | |___   | || |\  |___) || |/ ___ \| |___| |___| |___|  _ < │
│  |_| \___/ \___/|_____| |___|_| \_|____/ |_/_/   \_\_____|_____|_____|_| \_\│
└─────────────────────────────────────────────────────────────────────────────┘

{colored("01- Hydra           ..................................", "light_blue", attrs=['bold'])} {colored('[BRUTE-FORCE]', 'light_red', attrs=['bold'])}
{colored("02- Medusa          ..................................", "light_blue", attrs=['bold'])} {colored('[BRUTE-FORCE]', 'light_red', attrs=['bold'])}
{colored("03- Hashcat         ..................................", "light_blue", attrs=['bold'])} {colored('[BRUTE-FORCE]', 'light_red', attrs=['bold'])}
{colored("04- John            ..................................", "light_blue", attrs=['bold'])} {colored('[BRUTE-FORCE]', 'light_red', attrs=['bold'])}
{colored("05- Nmap            ..................................", "light_blue", attrs=['bold'])} {colored('[ENUMERATION]', 'light_red', attrs=['bold'])}
{colored("06- Masscan         ..................................", "light_blue", attrs=['bold'])} {colored('[ENUMERATION]', 'light_red', attrs=['bold'])}
{colored("07- Nikto           ..................................", "light_blue", attrs=['bold'])} {colored('[ENUMERATION]', 'light_red', attrs=['bold'])}
{colored("08- Gobuster        ..................................", "light_blue", attrs=['bold'])} {colored('[ENUMERATION]', 'light_red', attrs=['bold'])}
{colored("09- Dirsearch       ..................................", "light_blue", attrs=['bold'])} {colored('[ENUMERATION]', 'light_red', attrs=['bold'])}
{colored("10- Dirb            ..................................", "light_blue", attrs=['bold'])} {colored('[ENUMERATION]', 'light_red', attrs=['bold'])}
{colored("11- FFuF            ..................................", "light_blue", attrs=['bold'])} {colored('[ENUMERATION]', 'light_red', attrs=['bold'])}
{colored("12- Wfuzz           ..................................", "light_blue", attrs=['bold'])} {colored('[ENUMERATION]', 'light_red', attrs=['bold'])}
{colored("13- Sqlmap          ..................................", "light_blue", attrs=['bold'])} {colored('[ENUMERATION]', 'light_red', attrs=['bold'])}
{colored("14- Bettercap       ..................................", "light_blue", attrs=['bold'])} {colored('[ENUMERATION]', 'light_red', attrs=['bold'])}
{colored("15- Wireshark       ..................................", "light_blue", attrs=['bold'])} {colored('[ENUMERATION]', 'light_red', attrs=['bold'])}
{colored("16- Netdiscover     ..................................", "light_blue", attrs=['bold'])} {colored('[ENUMERATION]', 'light_red', attrs=['bold'])}
{colored("17- Aircrack-ng     ..................................", "light_blue", attrs=['bold'])} {colored('[ENUMERATION]', 'light_red', attrs=['bold'])}
{colored("18- Proxychains4    ..................................", "light_blue", attrs=['bold'])} {colored('[PRIVACY]', 'light_red', attrs=['bold'])}          
{colored("19- Tor             ..................................", "light_blue", attrs=['bold'])} {colored('[PRIVACY]', 'light_red', attrs=['bold'])}
{colored("20- BeEF            ..................................", "light_blue", attrs=['bold'])} {colored('[EXPLOITATION]', 'light_red', attrs=['bold'])}
{colored("21- Docker          ..................................", "light_blue", attrs=['bold'])} {colored('[COMMON-TOOL]', 'light_red', attrs=['bold'])}
{colored("22- Binwalk         ..................................", "light_blue", attrs=['bold'])} {colored('[COMMON-TOOL]', 'light_red', attrs=['bold'])}
{colored("23- Steghide        ..................................", "light_blue", attrs=['bold'])} {colored('[COMMON-TOOL]', 'light_red', attrs=['bold'])}
{colored("24- Crunch          ..................................", "light_blue", attrs=['bold'])} {colored('[COMMON-TOOL]', 'light_red', attrs=['bold'])}

{colored("----------------------- EXTERNAL TOOLS -----------------------", "green", attrs=['bold'])}

{colored("25- Storm-Breaker   ..................................", "light_blue", attrs=['bold'])} {colored('[GITHUB-TOOL]', 'light_red', attrs=['bold'])}
{colored("26- Subfinder       ..................................", "light_blue", attrs=['bold'])} {colored('[GITHUB-TOOL]', 'light_red', attrs=['bold'])}
{colored("27- Httpx           ..................................", "light_blue", attrs=['bold'])} {colored('[GITHUB-TOOL]', 'light_red', attrs=['bold'])}
{colored("28- Nuclei          ..................................", "light_blue", attrs=['bold'])} {colored('[GITHUB-TOOL]', 'light_red', attrs=['bold'])}
{colored("29- Zphisher        ..................................", "light_blue", attrs=['bold'])} {colored('[GITHUB-TOOL]', 'light_red', attrs=['bold'])}
{colored("30- SecLists        ..................................", "light_blue", attrs=['bold'])} {colored('[GITHUB-TOOL]', 'light_red', attrs=['bold'])}
{colored("31- Setoolkit       ..................................", "light_blue", attrs=['bold'])} {colored('[GITHUB-TOOL]', 'light_red', attrs=['bold'])}
{colored("00- Main Menu       ..................................", "light_blue", attrs=['bold'])} {colored('[MAIN-MENU]', 'light_red', attrs=['bold'])}


                      """, "light_blue", attrs=['bold']))
        
    @staticmethod
    def install(): # Main Install Function
        while True:
            Commons.clear()
            Commons.install_menu() # MENU #
            try:
                choice = int(input("Enter Choice : ")) # MAIN USER INPUT #
            except KeyboardInterrupt:
                break
            except ValueError:
                print(colored("Please Enter a Valid Option", "red", attrs=['bold']))
                sleep(1)
                Commons.clear()
                continue
            
            #Exit
            if choice == 0:
                break
            
            #Hydra
            elif choice == 1:
                Commons.clear()
                installer.hydra_install()
                Commons.clear()
                
            #Medusa
            elif choice == 2:
                Commons.clear()
                installer.medusa_install()
                Commons.clear()
            
            #hashcat
            elif choice == 3:
                Commons.clear()
                installer.hashcat_install()
                Commons.clear()

            #John
            elif choice == 4:
                Commons.clear()
                installer.john_install()
                Commons.clear()

            #Nmap
            elif choice == 5:
                Commons.clear()
                installer.nmap_install()
                Commons.clear()

            #Masscan
            elif choice == 6:
                Commons.clear()
                installer.masscan_install()
                Commons.clear()
            
            #Nikto
            elif choice == 7:
                Commons.clear()
                installer.nikto_install()
                Commons.clear()

            #Gobuster
            elif choice == 8:
                Commons.clear()
                installer.gobuster_install()
                Commons.clear()

            #Dirsearch
            elif choice == 9:
                Commons.clear()
                installer.dirsearch_install()
                Commons.clear()

            #Dirb
            elif choice == 10:
                Commons.clear()
                installer.dirb_install()
                Commons.clear()
            
            #Ffuf
            elif choice == 11:
                Commons.clear()
                installer.ffuf_install()
                Commons.clear()

            #Wfuzz
            elif choice == 12:
                Commons.clear()
                installer.wfuzz_install()
                Commons.clear()

            #Sqlmap
            elif choice == 13:
                Commons.clear()
                installer.sqlmap_install()
                Commons.clear()
            
            #Bettercap
            elif choice == 14:
                Commons.clear()
                installer.bettercap_install()
                Commons.clear()

            #Wireshark
            elif choice == 15:
                Commons.clear()
                installer.wireshark_install()
                Commons.clear()

            #Netdiscover
            elif choice == 16:
                Commons.clear()
                installer.netdiscover_install()
                Commons.clear()

            #Aircrack
            elif choice == 17:
                Commons.clear()
                installer.aircrack_install()
                Commons.clear()

            #Proxychains4
            elif choice == 18:
                Commons.clear()
                installer.proxychains_install()
                Commons.clear()

            #Tor
            elif choice == 19:
                Commons.clear()
                installer.tor_install()
                Commons.clear()
            #Beef
            elif choice == 20:
                Commons.clear()
                installer.beef_install()
                Commons.clear()
            
            #Docker
            elif choice == 21:
                Commons.clear()
                installer.docker_install()
                Commons.clear()

            #Binwalk
            elif choice == 22:
                Commons.clear()
                installer.binwalk_install()
                Commons.clear()
            
            #Steghide
            elif choice == 23:
                Commons.clear()
                installer.steghide_install()
                Commons.clear()
            #Crunch
            elif choice == 24:
                Commons.clear()
                installer.crunch_install()
                Commons.clear()



            #Storm-Breaker
            elif choice == 25:
                Commons.clear()
                gitinstaller.stormbreaker_install()
                sleep(1.5)
                Commons.clear()

            #Subfinder
            elif choice == 26:
                Commons.clear()
                gitinstaller.subfinder_install()
                sleep(1.5)
                Commons.clear()

            #Httpx
            elif choice == 27:
                Commons.clear()
                gitinstaller.httpx_install()
                sleep(1.5)
                Commons.clear()

            #Nuclei
            elif choice == 28:
                Commons.clear()
                gitinstaller.nuclei_install()
                sleep(1.5)
                Commons.clear()

            #Zphisher
            elif choice == 29:
                Commons.clear()
                gitinstaller.zphisher_install()
                sleep(1.5)
                Commons.clear()

            #Seclists
            elif choice == 30:
                Commons.clear()
                gitinstaller.seclists_install()
                sleep(1.5)
                Commons.clear()

            #Setoolkit
            elif choice == 31:
                Commons.clear()
                gitinstaller.setoolkit_install()
                sleep(1.5)
                Commons.clear()

            else:
                Commons.clear()
                continue