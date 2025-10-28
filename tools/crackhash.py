#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib
from termcolor import colored
import subprocess as su
from time import sleep


class Crackhash:

    @staticmethod
    def clear(): #Clear terminal
        su.run("clear", shell=True)

    @staticmethod
    def presscontinue(): #Ask User For Continue
        try:
            resp = input(colored("Press Enter For Continue...", "light_blue", attrs=['bold']))
            return
        except (KeyboardInterrupt, EOFError):
            return False
        

    @staticmethod
    def md5(): #Crack MD5 Hash Function
        
        Crackhash.clear() #Clear Terminal
        # Try Get Hash and Wordlist File
        try:
            hash = input(colored("Enter Hash : ", "light_blue", attrs=['bold']))
            wordlist_file = input(colored("Enter Wordlist File : ", "light_blue", attrs=['bold']))
        except (KeyboardInterrupt, EOFError):
            Crackhash.clear()
            return
        try:
            #Open Wordlist File
            with open(wordlist_file, 'r', encoding="utf-8", errors="ignore") as file:
                for line in file:
                    word = line.strip()
                    word_hash = hashlib.md5(word.encode()).hexdigest() # Return password to MD5 hash

                    if word_hash == hash: #If hashed word == hash
                        print(colored(f"Hash Found : {word}", "green", attrs=['bold'])) # Hash Found
                        with open("hash.log", "w") as file: #Add Hash In Log File
                            file.write(word_hash + ":" + word) # Add Hash and Clear Text Passphrase
                            print(colored("Hash Saved : hash.log", "green", attrs=['bold']))
                        
                        Crackhash.presscontinue() # Wait
                        Crackhash.clear() # Clear Terminal
                        break                    
                    
                    else: # If no match is found, keep trying
                        continue
                else: # If hash not in the wordlist
                    print(colored("Hash Not Found...", "red", attrs=['bold']))
                    Crackhash.presscontinue()
                    Crackhash.clear()
                    return
        except FileNotFoundError: #If Wordlist File Not Found
            print(colored(f"[-] Wordlist File Not Found : {wordlist_file}", "red", attrs=['bold']))
            sleep(1)
            Crackhash.clear()
            return
        
    @staticmethod
    def sha1(): # Crack SHA1 Hash Function
        Crackhash.clear() # Clear Screen

        #Get Hash and Wordlist File From User
        try:
            hash = input(colored("Enter Hash : ", "light_blue", attrs=['bold'])) #SHA1 HASH
            wordlist_file = input(colored("Enter Wordlist File Path : ", "light_blue", attrs=['bold'])) #WORDLIST
        except (KeyboardInterrupt, EOFError):
            Crackhash.clear()
            return
        
        try:
            with open(wordlist_file, 'r', encoding="utf-8", errors="ignore") as file: #OPEN WORDLIST FILE
                for line in file:
                    word = line.strip()
                    word_hash = hashlib.sha1(word.encode()).hexdigest() #GENERATE SHA1 HASH FROM EVERY WORD IN WORDLIST

                    if word_hash == hash: #IF FOUND HASH
                        print(colored(f"Hash Found : {word}", "green", attrs=['bold']))
                        with open("hash.log", "w") as file: #SAVE HASH IN LOG FILE
                            file.write(word_hash + ":" + word)
                            print(colored("Hash Saved : hash.log", "green", attrs=['bold']))

                        Crackhash.presscontinue()
                        Crackhash.clear()
                        break
                    else:
                        continue
                else: #IF HASH NOT IN THE WORDLIST
                    print(colored("Hash Not Found...", "red", attrs=['bold']))
                    Crackhash.presscontinue()
                    Crackhash.clear()
                    return
        except FileNotFoundError: #IF WORDLIST FILE PATH WAS WRONG :
            print(colored(f"[-] Wordlist File Not Found : {wordlist_file}", "red", attrs=['bold']))
            sleep(1)
            Crackhash.clear()
            return
        

    @staticmethod
    def sha256(): #Crack SHA256 Hash
        Crackhash.clear()

        #Get Hash and Wordlist File From User
        try:
        
            hash = input(colored("Enter Hash : ", "light_blue", attrs=['bold']))
            wordlist_file = input(colored("Enter Wordlist File Path : ", "light_blue", attrs=['bold']))
        
        except (KeyboardInterrupt, EOFError):
            Crackhash.clear()
            return
        
        #Open Wordlist File
        try: 
            with open(wordlist_file, 'r', encoding='utf-8', errors='ignore') as file: 
                for line in file:
                    word = line.strip()
                    word_hash = hashlib.sha256(word.encode()).hexdigest() #GENERATE SHA256 HASH FROM EVERY WORD IN WORDLIST

                    #IF HASH FOUND
                    if word_hash == hash:
                        
                        print(colored(f"Hash Found : {word}", "green", attrs=['bold']))
                        with open("hash.log", 'w') as file:
                            file.write(word_hash + ":" + word)
                            print(colored("Hash Saved : hash.log", "green", attrs=['bold']))
                        Crackhash.presscontinue()
                        Crackhash.clear()                    
                        break
                    
                    #TRY
                    else:
                        continue
                
                #IF HASH NOT FOUND
                else:
                    print(colored("Hash Not Found...", "red", attrs=['bold']))
                    Crackhash.presscontinue()
                    Crackhash.clear()
                    return
        except FileNotFoundError:
            print(colored(f"[-] Wordlist File Not Found : {wordlist_file}", "red", attrs=['bold']))
            sleep(1)
            Crackhash.clear()
            return
        
    
    @staticmethod
    def sha512(): #Crack SHA512 Hash
        Crackhash.clear()

        try:
        
            hash = input(colored("Enter Hash : ", "light_blue", attrs=['bold']))
            wordlist_file = input(colored("Enter Wordlist File Path : ", "light_blue", attrs=['bold']))
        
        except (KeyboardInterrupt, EOFError):
            Crackhash.clear()
            return
        
        try: #Start Wordlist
            with open(wordlist_file, 'r', encoding='utf-8', errors='ignore') as file:
                for line in file:
                    word = line.strip()
                    word_hash = hashlib.sha512(word.encode()).hexdigest()

                    # IF PASSWORD FOUND
                    if word_hash == hash:
                        print(colored(f"Hash Found : {word}", "green", attrs=['bold']))
                        with open("hash.log", 'w') as file:
                            file.write(word_hash + ":" + word)
                            print(colored("Hash Saved : hash.log", "green", attrs=['bold']))
                        Crackhash.presscontinue()
                        Crackhash.clear()                    
                        break
                    else:
                        continue
                else:
                    print(colored("Hash Not Found...", "red", attrs=['bold']))
                    Crackhash.presscontinue()
                    Crackhash.clear()
                    return
        except FileNotFoundError:
            print(colored(f"[-] Wordlist File Not Found : {wordlist_file}", "red", attrs=['bold']))
            sleep(1)
            Crackhash.clear()
            return


        

    @staticmethod
    def crack(): #Main Function
        Crackhash.clear() # Clear Terminal
        while True:
            print(colored(rf"""
    )                                               
 ( /(               )     (                       ) 
 )\())    )      ( /(     )\   (       )       ( /( 
((_)\  ( /(  (   )\())  (((_)  )(   ( /(   (   )\())
 _((_) )(_)) )\ ((_)\   )\___ (()\  )(_))  )\ ((_)\ 
| || |((_)_ ((_)| |(_) ((/ __| ((_)((_)_  ((_)| |(_)
| __ |/ _` |(_-<| ' \   | (__ | '_|/ _` |/ _| | / / 
|_||_|\__,_|/__/|_||_|   \___||_|  \__,_|\__| |_\_\ 

{colored("[01] - MD5      .............................","light_blue", attrs=['bold'])}{colored("[Crack MD5 Hash]", "green", attrs=['bold'])}
{colored("[02] - SHA-1    .............................","light_blue", attrs=['bold'])}{colored("[Crack SHA-1 Hash]", "green", attrs=['bold'])}
{colored("[03] - SHA-256  .............................","light_blue", attrs=['bold'])}{colored("[Crack SHA-256 Hash]", "green", attrs=['bold'])}
{colored("[04] - SHA-512  .............................","light_blue", attrs=['bold'])}{colored("[Crack SHA-512 Hash]", "green", attrs=['bold'])}                      
{colored("[00] - Exit     .............................","light_blue", attrs=['bold'])}{colored("[Back To Main Menu]", "green", attrs=['bold'])}
""", "red", attrs=['bold']))
            
            #Get Choice From User
            try:
                choice = int(input(colored("Enter : ", "light_blue", attrs=['bold'])))
            except (KeyboardInterrupt, EOFError,ValueError):
                break
            
            #MD-5 Hash Crack
            if choice == 1:
                Crackhash.md5()
            #SHA1 Hash Crack
            elif choice == 2:
                Crackhash.sha1()
            #SHA256 Hash Crack
            elif choice == 3:
                Crackhash.sha256()
            #SHA512 Hash Crack
            elif choice == 4:
                Crackhash.sha512()
            #Exit
            elif choice == 0:
                break
            else:
                Crackhash.clear()
                continue