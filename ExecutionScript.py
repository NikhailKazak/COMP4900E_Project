import sys
import EncryptionAlg
import TestEncryptionAlg

if __name__ == "__main__":
    myString=sys.argv[1]

    print("String before encryption: ", myString)

    decryptedText=EncryptionAlg.encrypt_decrypt_msg(myString)

    TestEncryptionAlg.test_string_return(myString, decryptedText)