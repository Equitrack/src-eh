#!/bin/bash

# Variable
nameUser="Alexander"

# Create user and directory
sudo useradd -m $nameUser

# Add user to sudo
sudo usermod -aG wheel $nameUser

# Delelte user
# sudo userdel -r $nameUser
