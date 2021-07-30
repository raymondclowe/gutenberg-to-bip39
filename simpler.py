
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

outputted_seed = 0
outputted_total = 0
i = 0
words11 = ""
while outputted_seed < 11:
    s = document_word_list[i]
    if flags_list[i]:        
        words11 = words11 + " " + clean_word_list[i]
        outputted_seed = outputted_seed + 1
        s = "*" + s + "*"

    print(s, end =" ")
    outputted_total = outputted_total + 1

    i = i + 1 

# Now find the 12th word

import mnemonic
 
m = mnemonic.Mnemonic('english')

words11 = words11[1:]
checksum_words = []

for word in bip39_word_list:
    tested = words11 + ' ' + word
    if m.check(tested):
        if word in clean_word_list:
            word_position = clean_word_list.index(word)
            if word_position > outputted_total :
                checksum_words.append((word,word_position))

checksum_words.sort(key=lambda tup: tup[1])
 
word12 = checksum_words[0][0]

done_sentence = False
last_word_outputted = False
while not done_sentence:
    s = document_word_list[i]
    if clean_word_list[i] == word12:  
        last_word_outputted = True

        s = "*" + s + "*"

    print(s, end =" ")

    if last_word_outputted:
        if '.' in document_word_list[i]:
            done_sentence = True

    i = i + 1 

