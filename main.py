#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from termcolor import colored
import subprocess as su
from time import sleep
from tools import commons
from tools import ovpn
from tools import idrsa
from tools import genhash
from tools import crackhash
from tools import starthydra
from tools import listener
from tools import reverse
from tools import venom
from tools import nmapscan
from tools import gobusterscan

clear = (lambda: su.run("clear", shell=True)) # Terminal Clear

bye = (lambda: print(colored("\nThank's For Using...", "green", attrs=['bold']))) # Exit Message

def menu():
    
    clear()
    print(colored(fr"""
 _____                                                                          _____ 
( ___ )                                                                        ( ___ )
 |TR |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|TR | 
 |TR |                                                                          |TR | 
 |TR |                                                                          |TR | 
 |TR |  _   _    _    ____ _  _____ _   _  ____   _____ ___   ___  _     ____   |TR | 
 |TR | | | | |  / \  / ___| |/ /_ _| \ | |/ ___| |_   _/ _ \ / _ \| |   / ___|  |TR | 
 |TR | | |_| | / _ \| |   | ' / | ||  \| | |  _    | || | | | | | | |   \___ \  |TR | 
 |TR | |  _  |/ ___ \ |___| . \ | || |\  | |_| |   | || |_| | |_| | |___ ___) | |TR | 
 |TR | |_| |_/_/   \_\____|_|\_\___|_| \_|\____|   |_| \___/ \___/|_____|____/  |TR | 
 |TR |                                                                          |TR | 
 |TR |                                                                          |TR | 
 |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| 
(_____)                  Made for CTF and Penetration Testing                  (_____)
                                       
""", "blue", attrs=['bold']))

    print(f""" 
{colored("[*] Some tools require root privileges. Please run them with sudo if needed.", "white", "on_red", attrs=['bold'])}
{colored("[01]", "red", attrs=['bold'])} - Nmap Scans ............................  {colored("(Scan services and ports)", "green", attrs=['bold'])}                       {colored('[ENUMERATION]', 'light_red')}
{colored("[02]", "red", attrs=['bold'])} - Gobuster Scans ........................  {colored("(Directory discovery)", "green", attrs=['bold'])}                           {colored('[ENUMERATION]', 'light_red')}
{colored("[03]", "red", attrs=['bold'])} - Start Burp Suite ......................  {colored("(Launch Burp Suite)", "green", attrs=['bold'])}                             {colored('[ENUMERATION]', 'light_red')}
{colored("[04]", "red", attrs=['bold'])} - Start Wireshark .......................  {colored("(Launch Wireshark)", "green", attrs=['bold'])}                              {colored('[ENUMERATION]', 'light_red')}
{colored("[05]", "red", attrs=['bold'])} - Create Payload ........................  {colored("(Create payloads with msfvenom)", "green", attrs=['bold'])}                 {colored('[TOOL]', 'light_red')}
{colored("[06]", "red", attrs=['bold'])} - Reverse Shells ........................  {colored("(Generate reverse shell)", "green", attrs=['bold'])}                        {colored('[TOOL]', 'light_red')}
{colored("[07]", "red", attrs=['bold'])} - Start Listener ........................  {colored("(Start a listener / netcat)", "green", attrs=['bold'])}                     {colored('[TOOL]', 'light_red')}
{colored("[08]", "red", attrs=['bold'])} - Launch Metasploit .....................  {colored("(Start Metasploit Framework)", "green", attrs=['bold'])}                    {colored('[TOOL]', 'light_red')}
{colored("[09]", "red", attrs=['bold'])} - Start Bettercap .......................  {colored("(Launch Bettercap)", "green", attrs=['bold'])}                              {colored('[TOOL]', 'light_red')}
{colored("[10]", "red", attrs=['bold'])} - Start Hydra ...........................  {colored("(Run Hydra for brute-force)", "green", attrs=['bold'])}                     {colored('[TOOL]', 'light_red')}
{colored("[11]", "red", attrs=['bold'])} - Generate Hash .........................  {colored("(Generate hashes: md5 / sha1 / sha256 etc.)", "green", attrs=['bold'])}     {colored('[TOOL]', 'light_red')}
{colored("[12]", "red", attrs=['bold'])} - Crack Hashes ..........................  {colored("(Crack hashes tool. Created by Furares)", "green", attrs=['bold'])}         {colored('[TOOL]', 'light_red')}
{colored("[13]", "red", attrs=['bold'])} - Crack id_rsa (SSH key) ................  {colored("(Crack an id_rsa private key — offline)", "green", attrs=['bold'])}         {colored('[TOOL]', 'light_red')}
{colored("[14]", "red", attrs=['bold'])} - Connect to OpenVPN Server .............  {colored("(Start OpenVPN connection)", "green", attrs=['bold'])}                      {colored('[TOOL]', 'light_red')}
{colored("[15]", "red", attrs=['bold'])} - Download Most Common Tools ............  {colored("(Install common pentest tools)", "green", attrs=['bold'])}                  {colored('[INFO]', 'light_red')}
{colored("[16]", "red", attrs=['bold'])} - Update System Tools ...................  {colored("(Update system & tools)", "green", attrs=['bold'])}                         {colored('[INFO]', 'light_red')}
{colored("[00]", "red", attrs=['bold'])} - EXIT ..................................  {colored("(Exit)", "green", attrs=['bold'])}                                          {colored('[EXIT]', 'light_red')}
""")                                     
    


def main():
    
    while True:
        menu()
        
        # Get Input From User #
        try:
            choice = int(input("Enter ---> ")) # Main Input
        except (KeyboardInterrupt, EOFError):
            bye() # Exit Message
            break
        
        except ValueError:
            clear()
            continue

        # Run Scripts #
        if choice == 0: # EXIT Option # 
            
            bye()
            sleep(0.5)
            break

        elif choice == 16: # Update System Tools Option
            try:
                clear()
                
                print(colored("[+] System update is starting", "green", attrs=['bold']))
                sleep(0.5)
                
                su.run("sudo bash tools/run_update.sh", shell=True)

            except (KeyboardInterrupt, EOFError):
                break

            # ASK FOR CONTINUE #
            try:
                ask = input(colored("\nDo you want to continue (Y/n) : ", "blue", attrs=['bold']))
            except (KeyboardInterrupt, EOFError):
                
                bye()
                sleep(0.5)
                break
            
            if ask in ["", "y", "yes", "Y"]:
                continue
            else:
                bye()
                break
                
        # Install Common Pentest Tools                 
        elif choice == 15:
            common = commons.Commons()
            common.install()

        # Connect OpenVPN Server
        elif choice == 14:
            vpn = ovpn.Openvpn()
            vpn.main()

        # Crack id_rsa Key
        elif choice == 13:
            id_rsa = idrsa.Sshjohn()
            id_rsa.main()

        # Hash Cracker
        elif choice == 12:
            hashes = crackhash.Crackhash()
            hashes.crack()

        # Hash Generator
        elif choice == 11:
            run = genhash.Hash()
            run.hash()
        
        # Start Hydra
        elif choice == 10:
            hydra = starthydra.Runhydra()
            hydra.run()

        # Start Bettercap
        elif choice == 9:
            su.run("sudo apt-get install bettercap", shell=True)
            su.run("sudo bash tools/run_bettercap.sh", shell=True)

        # Start Metasploit
        elif choice == 8:
            su.run("sudo bash tools/run_metasploit.sh", shell=True)

        # Start Listener
        elif choice == 7:
            start_listen = listener.Start()
            start_listen.listen()
        
        # Reverse Shell
        elif choice == 6:
            reverse_shell = reverse.Reverse()
            reverse_shell.reverse()

        elif choice == 5:
            msfvenom = venom.Msf()
            msfvenom.run()
        
        # Start WireShark
        elif choice == 4:
            su.run("sudo bash tools/run_wireshark.sh", shell=True)

        # Start Burp Suite
        elif choice == 3:
            su.run("sudo bash tools/run_burp.sh", shell=True)

        # Start Gobuster Scan
        elif choice == 2:
            gobuster = gobusterscan.Buster()
            gobuster.run()

        #Nmap Scan
        elif choice == 1:
            scanner = nmapscan.Nmap()
            scanner.run()


if __name__ == "__main__":
    main()
