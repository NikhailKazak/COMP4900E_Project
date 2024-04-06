from pqcrypto.kem.kyber1024 import generate_keypair as generate_kyber_keypair, encrypt as kyber_encrypt, decrypt as kyber_decrypt
from pqcrypto.sign.dilithium4 import generate_keypair as generate_dilithium_keypair, sign as dilithium_sign, verify as dilithium_verify

########################################################################################################
########################################################################################################

def kyber_key_gen():
    #Generate the public/secret keypair
    kyberPubKey, kyberSecKey = generate_kyber_keypair()

    #Return
    return (kyberPubKey, kyberSecKey)

def kyber_key_encapsulation(pubKey):
    #Uses public key to encrypt a randomly generated sym key -> results  in ciphertext
    ciphertext, symKey = kyber_encrypt(pubKey)

    #Return
    return ciphertext, symKey

def kyber_key_unecapsulate(kSec, encryptedSymKey):
    #Unecrypts sym key
    plaintextKey = kyber_decrypt(kSec, encryptedSymKey)

    #Return
    return plaintextKey

########################################################################################################
########################################################################################################

def dilithium_key_gen():
    #Generate the public/secret keypair
    dilithiumPubKey, dilithiumSecKey = generate_dilithium_keypair()

    #Return
    return (dilithiumPubKey, dilithiumSecKey)

def dilithim_sign_encrypted_key(encryptedSymKey, dSec):
    #Signs encryptedSymKey
    sig = dilithium_sign(dSec, encryptedSymKey)
    
    #Return
    return sig

def verify_sig_key(dPub, encryptedSymKey, sig):
    #Verifies the signing
    assert dilithium_verify(dPub, encryptedSymKey, sig)