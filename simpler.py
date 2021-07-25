
def ExtractAlpha(InputString):
    from string import ascii_letters
    return "".join([ch for ch in InputString if ch in (ascii_letters)])

bip39_word_list = []
document_word_list = []

with open('bip19-english.txt', "r", encoding='UTF-8') as f:
    bip39_word_list = f.read().split()

with open('document.txt', "r", encoding='UTF-8') as f:
    document_word_list = f.read().split()

flags_list = []
clean_word_list = []
for word in document_word_list:
    clean_word_list.append(ExtractAlpha(word.lower()))
    flags_list.append(clean_word_list[-1] in bip39_word_list)



# print(document_word_list)
# print(clean_word_list)
# print(flags_list)
# print(sum(flags_list))

outputted = 0
i = 0
words11 = ""
while outputted < 11:
    s = document_word_list[i]
    if flags_list[i]:        
        words11 = words11 + " " + clean_word_list[i]
        outputted = outputted + 1
        s = "*" + s + "*"

    print(s, end =" ")

    i = i + 1 

print("\n")
# Now find the 12th word

import mnemonic
 
m = mnemonic.Mnemonic('english')

words11 = words11[1:]
checksum_words = []

for word in bip39_word_list:
    tested = words11 + ' ' + word
    if m.check(tested):
        checksum_words.append(word)

print(checksum_words)