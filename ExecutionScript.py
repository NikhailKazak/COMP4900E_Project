import sys
import RSAExampleEncryptionAlg
import KyberDilithiumEncryptionAlg
import TestEncryptionAlg

if __name__ == "__main__":
    
    #Takes command line arg - remember to use quotes if multiword string 
    mode=sys.argv[1]
    
    
    if(mode.lower()=="rsa"):
        #Calls RSA func from imported file
        myString=sys.argv[2]
        
        print("String before encryption: ", myString)
        decryptedText=RSAExampleEncryptionAlg.encrypt_decrypt_msg(myString)

        TestEncryptionAlg.test_rsa_string_return(myString, decryptedText)

    elif(mode.lower()=="kyber"):
        #Calls Kyber func from imported file
        kyberRet=KyberDilithiumEncryptionAlg.kyber_key_encapsulation()

        #Calls the test function for Kyber
        TestEncryptionAlg.test_kyber_return(kyberRet)

    elif(mode.lower()=="dilithium"):
        #Calls Dilithium func from imported file
        myString=sys.argv[2]

        print("String before encryption: ", myString)
        dilithiumRet=KyberDilithiumEncryptionAlg.msg_dilithium_signing(myString)

        #Calls the test function for Dilithium
        TestEncryptionAlg.test_dilithium_return(dilithiumRet)

