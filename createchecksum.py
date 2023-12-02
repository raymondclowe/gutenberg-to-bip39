# Create the checksum word

import mnemonic
import sys
 
m = mnemonic.Mnemonic('english')

with open('bip19-english.txt', "r", encoding='UTF-8') as f:
    bip39_word_list = f.read().split()


# get 11, 17 or 23 words from argument
try:
    partial_words = sys.argv[1]
except:
    print('useage: python createchecksum.py "11, 17, 21 or 23 words"')


print (partial_words)
# partial_words = "alert record income curve mercy tree heavy loan hen recycle mean"

i = 1
for word in bip39_word_list:
    if m.check(partial_words + " " + word):
        print(f'{i}: {word}')
        
