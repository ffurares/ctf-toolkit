#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess as su
from time import sleep
from termcolor import colored
import os
import shutil

class Openvpn:

    # Clear Function
    @staticmethod
    def clear():
        su.run("clear", shell=True)

    # OpenVPN Check
    @staticmethod
    def is_openvpn_in_path() -> bool:
        return shutil.which("openvpn") is not None

    # Main Function
    @staticmethod
    def main():
        while True:
            Openvpn.clear()
            # If OpenVPN is installed 
            if Openvpn.is_openvpn_in_path():
                try:
                    print(colored("Press CTRL + ^C For Back Main Menu", "white", "on_red", attrs=['bold']))
                    openvpn_file = input(colored("Enter Openvpn File : ", "light_blue", attrs=['bold'])) # Get OpenVPN Configuration File
                except KeyboardInterrupt:
                    break
                except EOFError:
                    break
                
                # Run Command and Connect OpenVPN Server
                if os.path.isfile(openvpn_file):
                    su.run(["sudo", "openvpn", openvpn_file], check=True)
                    Openvpn.clear()
                
                # If OpenVPN Configuration File Not Found :
                else:
                    print(colored("[-] OpenVPN Configuration File Not Found", "red", attrs=['bold']))
                    sleep(1)
                    Openvpn.clear()
                    continue
            # If OpenVPN not installed
            else:
                try:
                    ask = input(colored("OpenVPN not found. Install now? [Y/n] : ", "light_blue", attrs=['bold']))
                except KeyboardInterrupt:
                    break
                except EOFError:
                    break
                
                # Install OpenVPN
                if ask.strip().lower() in ["y", "yes", ""]:
                    su.run(["sudo", "apt", "-y", "install", "openvpn"], check=True)
                    Openvpn.clear()
                    continue
                else:
                    print(colored("Thanks For Using...", "green", attrs=['bold']))
                    break