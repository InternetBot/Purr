from wordlist import print_separator

def verify_wordlist(word_list):
    '''
    Checking if wordlist is empty if it is, sets this as default
    '''
    if not word_list:
        print("⚠️ No wordlist provided! Using default: /usr/share/wordlists/")
        return "/usr/share/wordlists/dirbuster/directory-list-2.3-small.txt "

    #to do add drop down for user to get more options of default wordlist
    #test word list /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt 


    return word_list



