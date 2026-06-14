#test 1 röd
#def count_vowels(word):
#    return None

#test 1 grön
#def count_vowels(word):
#    return 0                #kommer alltid att bli grön för vi förväntar oss en nolla


def count_vowels(word):
    vowels = "aeiouyåäö"
    count = 0
    for letter in word.lower():
        if letter in vowels:
            count += 1
    return count

