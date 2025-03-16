#not worth running just do it locally 
##if u really dont want to run the suggested command you can try this not a 100% guaratee test rest still need to do more testing under certain conditions


## to do use subprocess to add this to wordlist

sudo apt update -y
sudo apt install --reinstall wordlists -y
if [ $? -eq 0 ]; then
    echo "✅ Wordlists successfully reinstalled!"
else
    echo "❌ Wordlists installation failed!"
    exit 1
fi