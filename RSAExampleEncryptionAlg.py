from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

'''
Function to generate keys used to
encrypt and decrypt the user provided msg
'''
def encrypt_decrypt_msg(msg):
    #Generates keys
    key = RSA.generate(2048)
    privateKey = key.export_key('PEM')
    publicKey = key.publickey().export_key('PEM')

    #For later use with pytest - verifying keys with other txt???
    with open("priv_key.pem", "wb") as f:
        f.write(privateKey)

    #For later use with pytest - verifying keys with other txt???
    with open("pub_key.pem", "wb") as f:
        f.write(publicKey)

    #Needed for RSA encryption - turns datatype to bytes
    encodedStr = str.encode(msg)

    #Encrypts the msg
    rsaPublicKey=RSA.import_key(publicKey)
    rsaPubKey=PKCS1_OAEP.new(rsaPublicKey)
    encryptedMsg=rsaPubKey.encrypt(encodedStr)
    print("This is the encrypted text: {}".format(encryptedMsg))

    #Decrypts the msg
    rsaPrivateKey=RSA.import_key(privateKey)
    rsaPrivKey=PKCS1_OAEP.new(rsaPrivateKey)
    decryptedMsg=rsaPrivKey.decrypt(encryptedMsg)
    decryptedMsg=decryptedMsg.decode('utf-8')
    
    return(decryptedMsg)