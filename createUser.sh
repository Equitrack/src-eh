#!/bin/bash

# Variable
nameUser="Alexander"

# Create directory
sudo mkdir /home/$nameUser

# Create user and define directory
sudo useradd -d /home/$nameUser -s /bin/bash $nameUser

