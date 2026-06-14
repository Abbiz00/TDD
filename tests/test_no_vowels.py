from my_app.no_vowels_app import count_vowels


#def test_no_vowels():
#    assert count_vowels("qwrt") == 0


#test 1
def test_no_vowels_1():
    assert count_vowels("") == 0
    assert count_vowels("qwrt") == 0
    assert count_vowels("Tt") == 0
    assert count_vowels("123 123") == 0

def test_no_vowels_2(): # vokaler och dubbletter
    assert count_vowels("aeiouyåäö") == 9
    assert count_vowels("aaaaaaaaaa") == 10

def test_no_vowels_3(): # vokaler med stora bokstäver
    assert count_vowels("AEIOUÅÄÖ") == 8
    assert count_vowels("ÅÄÖ") == 3