import sys
import EncryptionAlg
import TestEncryptionAlg

if __name__ == "__main__":
    
    #Takes command line arg - remember to use quotes if multiword string 
    myString=sys.argv[1]

    print("String before encryption: ", myString)

    #Calls func from imported file
    decryptedText=EncryptionAlg.encrypt_decrypt_msg(myString)

    #Calls func from imported file
    TestEncryptionAlg.test_string_return(myString, decryptedText)