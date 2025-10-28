import subprocess as su
from time import sleep

# Install Most Common Tools
def aircrack_install():
    su.run(["sudo", "apt", "-y", "install", "aircrack-ng"], check=True)
    sleep(1.5)
def beef_install():
    su.run(["sudo", "apt", "-y", "install", "beef"], check=True)
    sleep(1.5)

def bettercap_install():
    su.run(["sudo", "apt", "-y", "install", "bettercap"], check=True)
    sleep(1.5)

def binwalk_install():
    su.run(["sudo", "apt", "-y", "install", "binwalk"], check=True)
    sleep(1.5)

def crunch_install():
    su.run(["sudo", "apt", "-y", "install", "crunch"], check=True)
    sleep(1.5)

def dirb_install():
    su.run(["sudo", "apt", "-y", "install", "dirb"], check=True)
    sleep(1.5)

def dirsearch_install():
    su.run(["sudo", "apt", "-y", "install", "dirsearch"], check=True)
    sleep(1.5)

def docker_install():
    su.run(["sudo", "apt", "-y", "install", "docker.io"], check=True)
    sleep(1.5)

def ffuf_install():
    su.run(["sudo", "apt", "-y", "install", "ffuf"], check=True)
    sleep(1.5)

def gobuster_install():
    su.run(["sudo", "apt", "-y", "install", "gobuster"], check=True)
    sleep(1.5)

def hashcat_install():
    su.run(["sudo", "apt", "-y", "install", "hashcat"], check=True)
    sleep(1.5)

def hydra_install():
    su.run(["sudo", "apt", "-y", "install", "hydra"], check=True)
    sleep(1.5)

def john_install():
    su.run(["sudo", "apt", "-y", "install", "john"], check=True)
    sleep(1.5)

def masscan_install():
    su.run(["sudo", "apt", "-y", "install", "masscan"], check=True)
    sleep(1.5)

def medusa_install():
    su.run(["sudo", "apt", "-y", "install", "medusa"], check=True)
    sleep(1.5)

def netdiscover_install():
    su.run(["sudo", "apt", "-y", "install", "netdiscover"], check=True)
    sleep(1.5)

def nikto_install():
    su.run(["sudo", "apt", "-y", "install", "nikto"], check=True)
    sleep(1.5)

def nmap_install():
    su.run(["sudo", "apt", "-y", "install", "nmap"], check=True)
    sleep(1.5)

def proxychains_install():
    su.run(["sudo", "apt", "-y", "install", "proxychains4"], check=True)
    sleep(1.5)

def sqlmap_install():
    su.run(["sudo", "apt", "-y", "install", "sqlmap"], check=True)
    sleep(1.5)

def steghide_install():
    su.run(["sudo", "apt", "-y", "install", "steghide"], check=True)
    sleep(1.5)

def tor_install():
    su.run(["sudo", "apt", "-y", "install", "tor"], check=True)
    sleep(1.5)

def wfuzz_install():
    su.run(["sudo", "apt", "-y", "install", "wfuzz"], check=True)
    sleep(1.5)

def wireshark_install():
    su.run(["sudo", "apt", "-y", "install", "wireshark"], check=True)
    sleep(1.5)