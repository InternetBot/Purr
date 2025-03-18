import subprocess
import os

# god i suck at naming this whole code  installs the wordlist 

def print_separator(title):
    '''
    for decoration 
    '''
    print("\n" + "="*60)
    print(title)
    print("="*60 + "\n")


def verify_checker():
    '''
    This verifies if the wordlist directory and files exist.
    '''
    user_wordlist_dir = "/usr/share/wordlists"

    print_separator("🔎 Verifying Wordlist Directory...")


    # Check if wordlists directory exists
    if os.path.isdir(user_wordlist_dir):
        print("✅ Wordlist directory exists 😀")
        print("="*60 + "\n")
        return True
    else:
        print("🟥 Wordlist directory not found 🧐")
        print("="*60 + "\n")
        return False


def download_word():
    '''
    This downloads the wordlist if it doesn't exist
    '''
    print_separator("📥 Downloading Wordlists, Please Be Patient...")

    # First install attempt, idk i have to run sudo reinstall to get it reinstalled on my device this logic is so flowed i hate my self 
    download_wordlist = subprocess.run(
        ["sudo", "apt", "install", "wordlists", "-y", "-v"],
        capture_output=True,
        text=True
    )

    print("🔵 Full installation output:\n", download_wordlist.stdout)
    print("="*60 + "\n")

    if download_wordlist.returncode == 0:
        print("✅ Successfully downloaded Wordlist 😀")
        print("Verifying the directory exists...")

        # If the directory is still missing, try reinstalling
        if not verify_checker():
            print_separator("⚠️ Directory still missing, trying to reinstall wordlists...")

            reinstall_wordlist = subprocess.run(
                #now this should work but idk why it's not questioning if this should even be done in python or bash
                #now for whatever reason if u rm -rf your wordlist this wont work 
                #idk why i tried fixing it cause thats what i did to test it but didnt work
                #i need to come up with a more appropriate solution to do this
                ["sudo", "apt", "install", "--reinstall", "wordlists", "-y", "-v"],
                capture_output=True,
                text=True
            )

            print("🔵 Full reinstall output:\n", reinstall_wordlist.stdout)
            print("="*60 + "\n")

            # Final verification
            if verify_checker():
                print("✅ Wordlist successfully installed after reinstall.")
            else:
                #reminder to create a bash script that automatically executes that 
                print("❌ Wordlist installation failed even after reinstall. Run manually!")
                print("command  => sudo apt install --reinstall wordlists ")
    else:
        print("❌ Failed to download Wordlist 😱")
        print("🔴 Error:", download_wordlist.stderr)
        print("="*60 + "\n")

print_separator("🚀 Wordlist Installation Script Started")

# for testing putpose

# if not verify_checker():
#     download_word()
