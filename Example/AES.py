import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from pqcrypto.kem.kyber1024 import generate_keypair as generate_kyber_keypair, encrypt as kyber_encrypt, decrypt as kyber_decrypt
from pqcrypto.sign.dilithium4 import generate_keypair as generate_dilithium_keypair, sign as dilithium_sign, verify as dilithium_verify


"""
Global paths/vars
"""

folder_path = "./binExampleFolder/"
output_folder_encrypted = "./encrypted/"
output_folder_decrypted = "./decrypted/"

########################################################################################################
########################################################################################################

def aes_call_encrypt(key):
    #Encrypts files in the bin folder
    for filename in os.listdir(folder_path):
        input_file = os.path.join(folder_path, filename)
        if os.path.isfile(input_file): #and not (input_file.endswith("_encrypted.txt") or input_file.endswith("_decrypted.txt")):
            output_file_encrypted = os.path.join(output_folder_encrypted, filename + "_encrypted")
            aes_proceed_encrypt_file(key, input_file, output_file_encrypted)

def aes_proceed_encrypt_file(key, input_file, output_file_encrypted):
    iv = get_random_bytes(16)  #Generates a new IV for each file
    cipher = AES.new(key, AES.MODE_CFB, iv)

    with open(input_file, "rb") as file, open(output_file_encrypted, "wb") as eF1:
        eF1.write(iv)  #Writes the IV to the output file
        while True:
            chunk = file.read(4096)  #Reads 4KB at a time
            if not chunk:
                break
            encrypted_chunk = cipher.encrypt(chunk)
            eF1.write(encrypted_chunk)

########################################################################################################
########################################################################################################

def aes_call_decrypt(key):
    #Decrypts encrypted files in the folder
    for filename in os.listdir(output_folder_encrypted):
        input_file_encrypted = os.path.join(output_folder_encrypted, filename)
        output_file_decrypted = os.path.join(output_folder_decrypted, filename.replace("_encrypted", ""))
        aes_proceed_decrypt_file(key, input_file_encrypted, output_file_decrypted)

def aes_proceed_decrypt_file(key, input_file_encrypted, output_file_decrypted):
    with open(input_file_encrypted, "rb") as file:
        iv = file.read(16)  #Reads the IV from the encrypted file
        cipher = AES.new(key, AES.MODE_CFB, iv)
        with open(output_file_decrypted, "wb") as decrypted_file:
            while True:
                chunk = file.read(4096)  #Read 4KB at a time
                if not chunk:
                    break
                decrypted_chunk = cipher.decrypt(chunk)
                decrypted_file.write(decrypted_chunk)