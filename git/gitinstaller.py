#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess as su
from time import sleep

# ProjectDiscovery Httpx
def httpx_install():
    repo = "https://github.com/projectdiscovery/httpx.git"
    su.run(["git", "clone", repo], check=True)
    sleep(1)

# ProjectDiscovery Nuclei
def nuclei_install():
    repo = "https://github.com/projectdiscovery/nuclei.git"
    su.run(["git", "clone", repo], check=True)
    sleep(1)

# Seclists
def seclists_install():
    repo = "https://github.com/danielmiessler/SecLists.git" 
    su.run(["git", "clone", repo], check=True)
    sleep(1)

# Setoolkit
def setoolkit_install():
    repo = "https://github.com/trustedsec/social-engineer-toolkit.git"
    su.run(["git", "clone", repo], check=True)
    sleep(1)

# Stormbreaker
def stormbreaker_install():
    repo = "https://github.com/ultrasecurity/Storm-Breaker"
    su.run(["git", "clone", repo], check=True)
    sleep(1)

# Subfinder
def subfinder_install():
    repo = "https://github.com/projectdiscovery/subfinder.git"
    su.run(["git", "clone", repo], check=True)
    sleep(1)

# Zphisher
def zphisher_install():
    repo = "https://github.com/htr-tech/zphisher.git"
    su.run(["git", "clone", repo], check=True)
    sleep(1)
