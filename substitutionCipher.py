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
    
    plainText = "".join(i for i in list(pt))
    terms = plainText.split()


    print("Encrypting the provided text....")
    cipherText = ""

    for i in terms: 
        temp = [] 
        i = i.replace('.', '')

        for j in i:
            if ord(j)>96:
                temp.append(key[ord(j)-ord('a')])
            else:
                temp.append(key[ord(j)-ord('A')])
        
        cipherText += "".join(i for i in temp)
    
    fp = open(output_file, "w") 
    fp.write(cipherText)
    print("\nEncryption Successful.. \nOutput now saved in the file..")
 

# Decrypt
def decrypt(cipher_file, key_file): 
    filesize = os.path.getsize(cipher_file)
    if filesize == 0:
        print("No cipher file present.... Retry...")
        return

    filesize = os.path.getsize(key_file)
    if filesize == 0:
        print("No key file present.... Retry...")
        return

    ct = open(cipher_file, "r")
    cipherText = list(ct)[0] 

    kt = open(key_file, "r")
    key = list("".join(i for i in list(kt)))

    print("Decrypting the provided text....")
    plainText = ""

    for i in cipherText:
        plainText += chr(ord('A') + key.index(i))
    print("Your decrypted text is : ", plainText)
    

def substitution_cipher():    
    while(True):
        print("\t\t\t\t\t\t==========================================================")
        print("\t\t\t\t\t\t\t\tSUBSTITUION CIPHERS")
        print("\t\t\t\t\t\t==========================================================")
        print ("""
        1.Encryption
        2.Decryption
        3.Exit/Quit
        """)
        ch = input("Please choose one of the above methods: \n >> ")

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
            print("\nDecryption for Substitution Cipher")

            print("Enter cipher text file name : ", end="")
            cipher_file = input() 

            print("Enter Key File name : ", end="")
            key_file = input() 

            decrypt(cipher_file, key_file)


        elif(ch == "3"):
            print("\nExiting...")
            exit(0)

        else:
            print("\nInvalid Input.. Retry..")