from wordlist import print_separator
from wordlist import verify_checker
from wordlist import download_word

def main_screen():
    '''
    main screen when you run command 
    '''
    print_separator ("🐱 Welcome to Purr 🐾")

    #need to sanitize user input for http https or neither 
    target_input = input("🎯 Enter your target IP address or URL: ")
    print(f"\n✅ Target set to: {target_input}")

    word_list = input(" 📂 Enter your wordlist directory: ")
    print(f"\n✅ Wordlist set to: {word_list}")

    print_separator("🔍 Preparing for Fuzzing...")


# specify wordlist to run or install wordlist with 
# 0 to add wordlist 
# to install wordlist 

if __name__ == "__main__":
    main_screen()
