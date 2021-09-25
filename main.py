from doubleTranspositionCipher import transposition_cipher
from substitutionCipher import substitution_cipher
from oneTimePad import one_time_pad
from aesECB import aes_ecb


if __name__ == "__main__":
    while (True):
        print("\t\t\t\t\t\t==========================================================")
        print("\t\t\t\t\t\t\t\tDIGITAL ASSIGNMENT 2")
        print("\t\t\t\t\t\t\t\tBHAVYA GOEL")
        print("\t\t\t\t\t\t\t\t19BCE0378")
        print("\t\t\t\t\t\t==========================================================")
        print ("""
        1. DOUBLE TRANSPOSITION CIPHER
        2. SUBSTITUTION CIPHER
        3. ONE TIME PAD 
        4. AES using ECB Mode 
        5. EXIT
        """)
        ans=input("Please choose one of the above encryption methods: \n >> ")

        if(ans == "1"):
            transposition_cipher()
        elif(ans == "2"):
            substitution_cipher()
        elif(ans == "3"):
            one_time_pad()
        elif(ans == "4"):
            aes_ecb()
        elif(ans == "5"):
            print("Exiting....")
            exit(0)
        else:
            print("Invalid Input...")
        