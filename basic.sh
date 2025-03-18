sudo apt update && sudo apt upgrade -y

## get locate installed 
sudo apt install -y mlocate
sudo updatedb
locate dirbuster 

## get whereis installed 
sudo apt install -y util-linux
whereis dirbuster

## default stuff
sudo apt install -y ffuf wordlists
ls /usr/share/wordlists/dirbuster/
sudo apt install --reinstall wordlists -y
sudo apt install -y python3 python3-pip
python3 main.py

## more logic behind this to come 
## just listing commmands that are in my head rn 