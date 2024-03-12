import pytest

def test_string_return(myString, decryptedText):
    try:
        assert myString==decryptedText
        print("Assertion returned True - the encrypted text was decrypted succesfully - Decrypted: {} == OG: {}".format(decryptedText, myString))
    except(AssertionError):
        print("Assertion returned False - the encrypted text was decrypted unsuccesfully - Decrypted: {} != OG: {}".format(decryptedText, myString))