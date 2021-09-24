# Encrypt
# Save PlainText or Message in PlainText.txt
# Key will be generated randomly and will be saved in key.txt
# You will be asked if you want to use Existing Key

import random
import os
from typing import KeysView

def encrypt(msg_file, keyOption, key_file, output_file):

    if not os.path.isfile(msg_file):
        with open(msg_file, 'w+') as fp:
            pass

    filesize = os.path.getsize(msg_file)
    if filesize == 0:
        print("Empty Plain text file...")
        print("Enter plain text : ", end="")
        plain = input() 
        p_write = open(msg_file, 'w+')
        p_write.write("".join(i for i in plain))
        print("Plain text written to file...")

    pt = open(msg_file, 'r+')
    print("Taking message/plain text from specified file...")

    if keyOption == 'Y' or keyOption == 'y':
        # Generating Random Keys 
        temp = [i for i in range(26)]
        key = []

        for i in range(26): 
            tmp = random.randint(0, len(temp)-1)
            key.append(chr(temp[tmp]+65))
            del temp[tmp] 
        
        print("Saving key in key_file...")
        fp = open(key_file, "w")
        fp.write("".join(i for i in key))
    
    else:
        # Using existing key 
        fp = open(key_file, "r")
        key = list("".join(i for i in list(fp)))

        if(len(key) != 26):
            print("INVALID KEY SIZE..EXITING..")
            exit(0)
    
    plainText = list(pt)[0]  
    terms = plainText.split()

    print("Encrypting the provided text....")
    cipherText = ""

    for i in terms: 
        temp = [] 
        for j in i:
            if ord(j)>96:
                temp.append(key[ord(j)-97])
            else:
                temp.append(key[ord(j)-65])
        
        cipherText += "".join(i for i in temp)
    
    fp = open(output_file, "w") 
    fp.write(cipherText)

    print("\n Encryption Successful.. \n Output now saved in the file..")





# Decrypt
if __name__ == "__main__":
    print("****** SUBSTITUTION CIPHER ******")
    
    while(True):
        print("\n\t 1. Encryption")
        print("\t 2. Decryption")
        print("\t 3. Exit")
        print("Enter your Choice : ")
        ch = input()

        if(ch == "1"):
            print("\nEncryption for Substitution Cipher")

            print("Enter plain text file name : ", end="")
            msg_file = input() 

            print("Generate Random key (Y/N) : ", end="")
            keyOption = input() 

            print("Enter Key File name : ", end="")
            key_file = input() 

            print("Enter output file name : ", end = "")
            output_file = input() 

            encrypt(msg_file, keyOption, key_file, output_file)

        elif (ch == "2"):
            print("\nEncryption for Substitution Cipher")

        elif(ch == "3"):
            print("\nExiting...")
            exit(0)

        else:
            print("\nInvalid Input.. Retry..")