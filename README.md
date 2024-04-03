# COMP4900E_Project

* To launch:
    * File should be executed on command line as follows
        * python3 ./ExecutionScript.py <"mode"> <"String">
        * Note: <"mode"> clarifies if you want to use rsa/kyber/dilithium - mandatory
        * Note: <"String"> is a placeholder to be replaced by a string. Multiword strings should be quoted - needed for RSA and Dilithium

Tuesday March 12, Notes:
* Changes by Nikhail: 
    * ExecutionScript.py deals with the control flow

    * TestEncryptionAlg.py is meant to run Pytest to ensure output

    * EncryptionAlg.py encrypts and decrypts user command line input

    * .github/workflows/main.yml is a yml script meant for github actions. Allows program to run at the click of a button

    * Necessary installs listed below:
        * pip3 install pycryptodome
        * pip3 install -U pytest

Thursday March 14, Notes:
* Changes by Nikhail:
    * TestEncryptionAlg.py has been changed to use the Python PQCrypto (Post-Quantum Crypto) library
        * Preliminary attempt to implement Kyber/Dilithium in Python

    * ExecutionScript.py now accepts modes and/or a string when launched - refer to launch instructions above

    * KyberDilithiumEncryptionAlg.py leverages an implementation of a kyber/dilithium library - [pqcrypto](https://github.com/kpdemetriou/pqcrypto)
        * Includes general description of operations

    * RSAExampleEncryptionAlg.py - renamed version of EncryptionAlg.py

    * main.yml is broken for now - don't expect it to work until it's refactored
        * Follow up - Works again

    * Necessary installs listed below:
        * pip3 install pqcrypto
            * Note: pqcrypto needs to be built on your local system as described in the .yml file for the lib to work. Just pip installing won't work

April 2, Notes:
* Changes by Nikhail:
    * Made changes in ./Example folder