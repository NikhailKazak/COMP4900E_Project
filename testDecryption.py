import os

"""
Global paths/vars
"""

folder_path = "./boot/sys"
output_folder_encrypted = "./encrypted"
output_folder_decrypted = "./decrypted"

#Get a list of all files in the directories
folder_files = os.listdir(folder_path)
decrypted_files = os.listdir(output_folder_decrypted)

########################################################################################################
########################################################################################################

def test_decryption_read_dir_prior_to_encrypt():
    #Checks that the number of files prior to and after decryption are equal
    if len(folder_files) != len(decrypted_files):
        print("Error: Number of files in directories is not equal.")
    else:
        #Goes through each directory's files and compares the content (verifies its the same before/after decryption)
        for filename in folder_files:
            file_path_folder = os.path.join(folder_path, filename)
            file_path_decrypted = os.path.join(output_folder_decrypted, filename)
            
            with open(file_path_folder, 'r') as file_folder, open(file_path_decrypted, 'r') as file_decrypted:
                try:
                    lines_folder = file_folder.readlines()
                    lines_decrypted = file_decrypted.readlines()

                    #Compare the contents line by line
                    try:
                        assert (lines_folder == lines_decrypted)
                        print(f"File '{filename}' contents are equal.")
                    except(AssertionError):
                        print(f"File '{filename}' contents are not equal.")

                except(UnicodeDecodeError):
                    print(f"File '{filename}' encoded in non-readable way.")
                    
    print("Comparison completed.")

if __name__ == "__main__":
    test_decryption_read_dir_prior_to_encrypt()