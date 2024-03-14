import pytest
from pqcrypto.kem.kyber1024 import generate_keypair as generate_kyber_keypair, encrypt as kyber_encrypt, decrypt as kyber_decrypt
from pqcrypto.sign.dilithium4 import generate_keypair as generate_dilithium_keypair, sign as dilithium_sign, verify as dilithium_verify

'''
Tests whether or not the string was 
decrypted as intended for RSA
'''
def test_rsa_string_return(myString, decryptedText):
    try:
        assert myString==decryptedText
        print("Assertion returned True - the encrypted text was decrypted succesfully - Decrypted: {} == OG: {}".format(decryptedText, myString))
    except(AssertionError):
        print("Assertion returned False - the encrypted text was decrypted unsuccesfully - Decrypted: {} != OG: {}".format(decryptedText, myString))

'''

'''
def test_kyber_return(ret):
    try:
        assert ret[0]==ret[1]
        print("Assertion returned True Kyber shared secret is consistent before and after encryption/decryption \n Values:\n {}=={}".format(ret[0],ret[1]))
    except(AssertionError):
        print("Assertion returned False Kyber shared secret is NOT consistent before and after encryption/decryption \n Values:\n {}=={}".format(ret[0],ret[1]))

'''

'''
def test_dilithium_return(ret):
    try:
        #Public Key is used to verify the signature against the message
        assert dilithium_verify(ret[0], ret[1], ret[2])
        print("Assertion returned True Dilithium signature has been verified")
    except(AssertionError):
        print("Assertion returned False Dilithium signature cannot be verified")
