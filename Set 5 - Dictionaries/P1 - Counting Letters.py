
def lettercount(instring):
    letter_freqs = {}
    for x in instring:
        if x not in letter_freqs:
            letter_freqs[x] = 0
        letter_freqs[x] += 1
    return letter_freqs
    
print(lettercount("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."))
