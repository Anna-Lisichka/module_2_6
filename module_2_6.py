def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        a = i.lower()
        b = root_word.lower()
        if b in a or a in b:
            same_words.append(i)
 
    return same_words

result = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
print(result)

result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result2)