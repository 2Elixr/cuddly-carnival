import hashlib
from itertools import permutations
def hash_finder(original_hash):
    wordfile = open("C:/Users/KskYm/Downloads/PRO-C229-Project/PRO-C229-Project/words.txt","r")
    wordfile = list(wordfile)

    anagram = "i move lads"
    words = anagram.count(' ')
    words += 1

    char_list = list(set(anagram))

    if ' ' in char_list:
        char_list.remove(' ')

    finals = []
    for i in wordfile:
        flag = False
        temp_word = i.replace('\n', '')
        temp_char = list(set(temp_word))
        for i in temp_char:
            if i not in char_list:
                flag = True
                break
        if flag == False:
            finals.append(temp_word)

    print(len(finals))

    for elem in permutations(finals, words):
        element = " ".join(elem)
        if len(element) != len(anagram):
            continue
        
        m = hashlib.md5()
        m.update(element.encode('utf-8'))
        word_hash = m.hexdigest()

        if word_hash == original_hash:
            return element

hash = 'ac3751fa101668c6de2002356d9a032b'
answer = hash_finder(hash)
print(f"Amazing!  The word corresponding to the given hash is '{answer}'")
