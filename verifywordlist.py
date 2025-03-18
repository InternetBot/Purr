from wordlist import print_separator

def verify_wordlist(word_list):
    '''
    Checking if wordlist is empty if it is, sets this as default
    '''
    if not word_list.strip():
        print("⚠️ No wordlist provided! Using default: /usr/share/wordlists/")

        if usr_wordlist_option == "s":
            return "/usr/share/wordlists/dirbuster/directory-list-2.3-small.txt"
        elif usr_wordlist_option == "m":
            return "/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt"
        elif usr_wordlist_option == "l":
            return "/usr/share/wordlists/dirbuster/directory-list-1.0.txt"
        else:
            print("⚠️ Invalid choice, defaulting to small.")
            return"/usr/share/wordlists/dirbuster/directory-list-2.3-small.txt"
            
    #to do add drop down for user to get more options of default wordlist
    #test word list /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt 


    return word_list



