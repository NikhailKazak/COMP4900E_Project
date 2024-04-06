from pqcrypto.kem.kyber1024 import generate_keypair as generate_kyber_keypair, encrypt as kyber_encrypt, decrypt as kyber_decrypt
from pqcrypto.sign.dilithium4 import generate_keypair as generate_dilithium_keypair, sign as dilithium_sign, verify as dilithium_verify
import AES
import PQC

def initEx():
    step1()

def followUpEx():

    #Reads in value
    with open('kyberSec.txt', 'rb+') as f:
        kSecKey = f.read()
        kSec=kSecKey
        f.truncate(0)

    #Reads in value
    with open('dilithiumPub.txt', 'rb+') as f:
        dPubKey = f.read()
        dPub=dPubKey
        f.truncate(0)

    #Reads in value
    with open('sigEncAESKey.txt', 'rb+') as f:
        sigEncAESKey = f.read()
        sig=sigEncAESKey
        f.truncate(0)

    #Reads in value
    with open('nonSigEncAESKey.txt', 'rb+') as f:
        nonSigEncAESKey = f.read()
        encryptedSymKey=nonSigEncAESKey
        f.truncate(0)

    step7(dPub, encryptedSymKey, sig)

    plaintextSymKey = step8(kSec, encryptedSymKey)

    step9(plaintextSymKey)

########################################################################################################
########################################################################################################

def step1():
    pr1='''
    Step 1 - decryption Device: 
    Generate Kyber Keypair

    Note: Only public key should 
    be transmitted to other devices
    '''
    kPub, kSec = PQC.kyber_key_gen()
    print(pr1)

    #Writes kyber pub key to file
    with open('kyberPub.txt', 'ab') as f:
        f.write(kPub)

    #Writes kyber sec key to file
    with open('kyberSec.txt', 'ab') as f:
        f.write(kSec)

    return(kPub, kSec)

def step7(dPub, encryptedSymKey, sig):
    pr7='''
    Step 7 - decryption Device: 
    Verified signature on key prior to decrypting 
    '''
    PQC.verify_sig_key(dPub, encryptedSymKey, sig)
    print(pr7)

def step8(kSec, encryptedSymKey):
    pr8='''
    Step 8 - decryption Device: 
    Since signature is valid, decrypt sym. key
    '''
    plaintextSymKey = PQC.kyber_key_unecapsulate(kSec, encryptedSymKey)
    print(pr8)

    return(plaintextSymKey)

def step9(plaintextSymKey):
    pr9='''
    Step 9 - decryption Device: 
    Used keys to decrypt files
    '''
    AES.aes_call_decrypt(plaintextSymKey)
    print(pr9)