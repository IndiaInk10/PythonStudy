
def get_frequency_of_given_alphabet(seq, alphabet):
    ret = 0
    for i in seq:
        if i == alphabet:
            ret += 1
    return ret

print('ret:', get_frequency_of_given_alphabet('No pain, no gain', 'n'))
print('ret:', get_frequency_of_given_alphabet('No pain, no gain', 'N'))

def get_frequency_of_each_word(seq, word):
    ret = 0
    for i in range(0, len(seq)):
        if seq[i] == word[0]:
            if seq[i:i + len(word)] == word:
                ret += 1
    return ret

print('ret:', get_frequency_of_each_word('To be or not to be that is the question', 'be'))
print('ret:', get_frequency_of_each_word('Apple Mango Orange Mango Apple Mango', 'Orange'))

print('To be or not to be that is the question'.count('be'))
print('Apple Mango Orange Mango Apple Mango'.count('Orange'))