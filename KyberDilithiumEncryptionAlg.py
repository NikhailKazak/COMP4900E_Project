from pqcrypto.kem.kyber1024 import generate_keypair as generate_kyber_keypair, encrypt as kyber_encrypt, decrypt as kyber_decrypt
from pqcrypto.sign.dilithium4 import generate_keypair as generate_dilithium_keypair, sign as dilithium_sign, verify as dilithium_verify

def kyber_key_encapsulation():
    #Generate the public/secret keypair
    kyberPubKey, kyberSecKey = generate_kyber_keypair()

    #Uses public key to encrypt a randomly generated shared secret -> results  in ciphertext
    ciphertext, shared_secret = kyber_encrypt(kyberPubKey)

    #ciphertext can securely be sent to one party

    #Decrypt ciphertext to obtain shared_secret
    shrd_scrt = kyber_decrypt(kyberSecKey, ciphertext)
    '''
    shrd_scrt can be used as a session key for symmetric cryptography of X/Y/Z between parties
    or can be used to derive message auth codes (MACs), Cryptographic checksums...
    '''
    # Return for testing
    return([shared_secret, shrd_scrt])

def msg_dilithium_signing(msg):
    #Generate public/secret keypair
    dilithiumPubKey, dilithiumSecKey = generate_dilithium_keypair()

    #Encode msg into bytes
    encodedMsg = str.encode(msg)

    #Encrypts/signs (using the private key and lattice-based cryptographic algorithms) a hash/digest unique to the msg
    sig = dilithium_sign(dilithiumSecKey, encodedMsg)

    #Return for testing Public Key is used to verify the signature against the message
    return([dilithiumPubKey, encodedMsg, sig])
