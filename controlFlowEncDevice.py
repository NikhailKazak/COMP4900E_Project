from pqcrypto.kem.kyber1024 import generate_keypair as generate_kyber_keypair, encrypt as kyber_encrypt, decrypt as kyber_decrypt
from pqcrypto.sign.dilithium4 import generate_keypair as generate_dilithium_keypair, sign as dilithium_sign, verify as dilithium_verify
import AES
import PQC
import time
import psutil

def initEx():
    startTime = time.time()
    kPub, encryptedSymKey, aesSymKey = step2()
    print("Time to execute Step 2:",time.time()-startTime)

    startTime = time.time()
    step3(aesSymKey)
    print("Time to execute Step 3:",time.time()-startTime,"and cpu usage is",psutil.cpu_percent(),"%")

    startTime = time.time()
    dPub, dSec = step4()

    sig = step5(encryptedSymKey, dSec)
    print("Time to execute Step 4 and 5:",time.time()-startTime)

    pr6='''
    Step 6:
    File transfer of:
    (1) Dilithium Public key,
    (2) signed encrypted key and non-signed encrypted version of key,
    (3) the encrypted files to device doing decryption
    '''
    print(pr6)

    #Writes dilithium pub key to file
    with open('dilithiumPub.txt', 'ab') as f:
        f.write(dPub)

    #Writes signed & encrypted AES key to file
    with open('sigEncAESKey.txt', 'ab') as f:
        f.write(sig)

    #Writes non-signed encrypted AES key to file
    with open('nonSigEncAESKey.txt', 'ab') as f:
        f.write(encryptedSymKey)
########################################################################################################
########################################################################################################

def step2():
    pr2='''
    Step 2 - Encryption Device:
    Generate a sym. key to be used
    with AES and create an encrypted
    version of it
    '''
    #Reads in value
    with open('kyberPub.txt', 'rb+') as f:
        kPubKey = f.read()
        kPub=kPubKey
        f.truncate(0)

    encryptedSymKey, symKey=PQC.kyber_key_encapsulation(kPub)
    aesSymKey=symKey
    print(pr2)

    return(kPub, encryptedSymKey, aesSymKey)

def step3(aesSymKey):
    pr3='''
    Step 3 - Encryption Device:
    Use Sym. key to encrypt files
    in directory
    '''
    AES.aes_call_encrypt(aesSymKey)
    print(pr3)

def step4():
    pr4='''
    Step 4 - Encryption Device:
    Generate Dilithium Keypair

    Note: Only public key should be
    viewable by other devices
    '''
    dPub, dSec = PQC.dilithium_key_gen()
    print(pr4)

    return(dPub, dSec)

def step5(encryptedSymKey, dSec):
    pr5='''
    Step 5 - Encryption Device:
    Sign the encrypted key
    '''
    sig = PQC.dilithim_sign_encrypted_key(encryptedSymKey, dSec)
    print(pr5)

    return(sig)
