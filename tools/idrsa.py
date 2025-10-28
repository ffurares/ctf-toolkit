#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess as su
from time import sleep
from termcolor import colored 
import urllib.request
import os
import shutil
import sys


class Sshjohn:
    
    @staticmethod
    def clear(): # Clear Screen
        su.run("clear", shell=True)

    @staticmethod
    def run_ssh2john(id_rsa_file, output_file):
        try:
            proc = su.run(
                [sys.executable, "ssh2john.py", id_rsa_file],
                check=True,
                stdout=su.PIPE,
                stderr=su.PIPE,
                text=True
            )
        except su.CalledProcessError as e:
            print(colored("Error Occured...", "red", attrs=['bold']))
            print(e.stderr or str(e))
            return False
        try:
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(proc.stdout)
        except OSError as e:
            print(colored(f"Error Occured : {e}", "red", attrs=['bold']))
            return False

        print(colored(f"Successfully Cracked. Saved as ---> {output_file}", "green", attrs=['bold']))
        return True

    @staticmethod
    def main():
        while True:
            if os.path.isfile("ssh2john.py"):
                try:
                    Sshjohn.clear()
                    print(colored("Press CTRL + C For Back Main Menu", "white", "on_red", attrs=['bold']))
                    id_rsa_file = input(colored("Enter id_rsa File Path : ", "light_blue", attrs=['bold']))
                except (KeyboardInterrupt, EOFError):
                    break

                if os.path.isfile(id_rsa_file):
                    try:
                        output = input(colored("Enter Output File : ", "light_blue", attrs=['bold']))
                    except (KeyboardInterrupt, EOFError):
                        break

                    Sshjohn.run_ssh2john(id_rsa_file, output)
                    sleep(1)
                    Sshjohn.clear()

            else:
                try:
                    Sshjohn.clear()
                    ask = input(colored("Ssh2john not found. Install now? [Y/n] : ", "light_blue", attrs=['bold']))
                except (KeyboardInterrupt, EOFError):
                    break

                if ask.strip().lower() in ["y", "yes", ""]:
                    repo = "https://raw.githubusercontent.com/magnumripper/JohnTheRipper/bleeding-jumbo/run/ssh2john.py"
                    if shutil.which("wget"):
                        try:
                            su.run(["wget", "-q", repo, "-O", "ssh2john.py"], check=True)
                        except su.CalledProcessError as e:
                            print(colored("Wget Download Error : " + str(e), "red"))
                            break
                    else:
                        try:
                            urllib.request.urlretrieve(repo, "ssh2john.py")
                        except Exception as e:
                            print(colored("Error : " + str(e), "red"))
                            break

                    Sshjohn.clear()
                    continue
                else:
                    print(colored("Thanks For Using...", "green", attrs=['bold']))
                    break