from wordlist import print_separator

def verify_wordlist(word_list):
    '''
    Checking if wordlist is empty if it is, sets this as default
    '''
    if not word_list:
        print("⚠️ No wordlist provided! Using default: /usr/share/wordlists/")
        return "/usr/share/wordlists"

    return word_list



