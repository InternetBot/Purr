from wordlist import print_separator
from wordlist import verify_checker
from wordlist import download_word
from dirfuzz import directory_fuzzing
from verifywordlist import verify_wordlist

def main_screen():
    '''
    main screen when you run command 
    '''
    print_separator ("🐱 Welcome to Purr 🐾")

    #need to sanitize user input for http https or neither 
    target_input = input("🎯 Enter your target IP address or URL: ")
    print(f"\n✅ Target set to: {target_input}")

    word_list = input(" 📂 Enter your wordlist directory: ")
    wordlist = verify_wordlist(word_list)
    print(f"\n✅ Wordlist set to: {word_list}")

    print_separator("🔍 Preparing for Fuzzing...")

    return target_input, word_list

def options_screen(target_input, word_list):
    '''
    Display options for selecting opteions
    '''
    print_separator(" 🔽 Select an Option 🔽 ")
    print("1️⃣ Directory Fuzzing")
    print("2️⃣ Subdomain Fuzzing")
    print("0️⃣ Exit")

    option_input = input("\n🔷 Enter your choice: ")

    if option_input == "1":
        directory_fuzzing(target_input, word_list)
    if option_input == "2":
        # do nothing havent written code yet
        print("Coming soon")
    if option_input == "0":
        #exit
        exit()
    else:
        print("❌ Invalid choice! Please select a valid option.")
        options_screen(target_input, word_list)




# specify wordlist to run or install wordlist with 
# 0 to add wordlist 
# to install wordlist 

if __name__ == "__main__":
    
    # idk this made me a lil confused google said so 
    target_input, word_list = main_screen()
    options_screen(target_input, word_list)
