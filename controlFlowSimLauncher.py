import controlFlowDecDevice as CFDDev
import controlFlowEncDevice as CFEDev

if __name__ == "__main__":
    #Generates Kyber keys
    CFDDev.initEx()

    #Encrypts and signs files
    CFEDev.initEx()

    #Decrypts files
    CFDDev.followUpEx()