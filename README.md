# COMP4900E_Project

* To launch:
    * Launch from controlFlowSimLauncher.py
        * python3 ./controlFlowSimLauncher.py


* Brief Description:
    * Necessary installs listed below:
        * pip3 install pycryptodome
        * pip3 install -U pytest
        * pip3 install pqcrypto
            * Note: [pqcrypto](https://github.com/kpdemetriou/pqcrypto) needs to be built on your local system as outlined in the .yml file for the lib to work. Just pip installing won't make it work 
    * Process outline
        * Note, though the controlFlowSimLauncher.py can work on 1 device, the assumption made throughout the project is as follows:
            * Because we want to simulate a real life application, for PQC signing / security of the boot process we assume the use of a PC, another device (in our case a Raspberry Pi 4B hereon refered to as an RPI) and a QNX VM. 
                * The PC - the decryption device - generates the kyber keypair. Because the public key by definition is known to the world it may be refered to by other devices. 
                * The RPI - the encryption device - uses the kyber public key to encrypt the AES symmetric key after it has been used to encrypt the files necessary for boot of the QNX vm. Additionally the encrypted sym. key is signed, providing evidence of integrity.
                * A file transfer occurs to send certain data (dilithium pub. key, the encrypted files, the signed encrypted sym.key, the non-signed encrypted sym. key) to the PC - the decryption device. At which point the signature is verified, validating the integrity of the encrypted sym. key. Then, the sym. key is decrypted with the kyber private key and used to decrypted the files.
                * Once decrypted, the boot folder is moved to the approriate directory for the QNX vm to boot.
                * And that's it!
    * Files / directories:
        * controlFlowSimLauncher.py runs the control flow outlined above -> More clearly reflected in controlFlowDecDevice.py & controlFlowEncDevice.py respectively

        * AES.py is meant to encrypt and decrypt all files from the QNX /boot directory using AES in CFB mode

        * PQC.py is meant to generate kyber / dilithium keypairs, encrypt / decrypt keys, and sign / verify signatures 

        * /decrypted is where decrypted files go to after the encrypted file variants are decrypted -> assists with the test

        * /encrypted is where encrypted files go to after being encrypted -> assists with identifying what is / isn't encrypted

        * testDecryption reads through the intial set of files and compares them against their decrypted variants, ensuring decryption occured approriately -> NOTE: only works on standard file encodings

        * .github/workflows/main.yml is a yml script meant for github actions. Allows program to run at the click of a button
