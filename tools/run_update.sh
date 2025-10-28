#!/bin/bash

set -e

LOGFILE="/var/log/system_update.log"

update() {
    sudo apt-get update -y | tee -a "$LOGFILE"
    sudo apt-get upgrade -y | tee -a "$LOGFILE"
}

if update; then
    echo "[+] System update completed successfully [+]"
else
    echo "[-] System Update Failed [-]"
    exit 1
fi