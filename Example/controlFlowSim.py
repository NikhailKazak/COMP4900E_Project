from pqcrypto.kem.kyber1024 import generate_keypair as generate_kyber_keypair, encrypt as kyber_encrypt, decrypt as kyber_decrypt
from pqcrypto.sign.dilithium4 import generate_keypair as generate_dilithium_keypair, sign as dilithium_sign, verify as dilithium_verify
import AES
import PQC

if __name__ == "__main__":
    
    '''
    Step 1: Generate Kyber Keypair - on device doing decryption
    Note: Only public key should be viewable by other devices
    '''
    kPub, kSec = PQC.kyber_key_gen()

    ''' 
    Step 2: Generate an sym. key to be used with AES and creates 
    and encrypted version of it - on device doing encryption
    '''
    encryptedSymKey, symKey=PQC.kyber_key_encapsulation(kPub)
    aesSymKey=symKey

    '''
    Step 3: Use Sym. key to encrypt files in directory - on device doing encryption
    '''
    AES.aes_call_encrypt(aesSymKey)

    '''
    Step 4: Generate Dilithium Keypair - on device doing encryption
    Note: Only public key should be viewable by other devices
    '''
    dPub, dSec = PQC.dilithium_key_gen()

    '''
    Step 5: Sign the encrypted key - on the device doing the encryption
    '''
    sig = PQC.dilithim_sign_encrypted_key(encryptedSymKey, dSec)

    '''
    Step 6: File transfer of (1) Dilithium Public key, (2) signed encrypted key and non-signed encrypted version of key, (3) the 
    encrypted files to device doing decryption  
    '''

    '''
    -----------------
    '''

    '''
    Step 7: Verify signature on key prior to decrypting - on device doing decryption
    '''
    PQC.verify_sig_key(dPub, encryptedSymKey, sig)

    '''
    Step 8: If sig is valid, decrypt sym. key - on device doing decryption
    '''
    plaintextSymKey = PQC.kyber_key_unecapsulate(kSec, encryptedSymKey)

    '''
    Step 9: Use keys to unencrypt files - on device doing decryption
    '''
    AES.aes_call_decrypt(plaintextSymKey)