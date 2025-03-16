from wordlist import print_separator
from wordlist import verify_checker
from wordlist import download_word

def main_screen():
    '''
    main screen when you run command 
    '''
    print_separator ("🐱 Welcome to Purr 🐾")
    target_input = input("🎯 Enter your target IP address or URL: ")
    print(f"\n✅ Target set to: {target_input}")
    print_separator("🔍 Preparing for Fuzzing...")

if __name__ == "__main__":
    main_screen()
