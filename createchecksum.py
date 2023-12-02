# Create the checksum word

import mnemonic
import sys
 
m = mnemonic.Mnemonic('english')

with open('bip19-english.txt', "r", encoding='UTF-8') as f:
    bip39_word_list = f.read().split()


# get 11, 17 or 23 words from argument
partial_words = sys.argv[1]
print (partial_words)
# partial_words = "alert record income curve mercy tree heavy loan hen recycle mean"

for word in bip39_word_list:
    if m.check(partial_words + " " + word):
        print(word)
        
