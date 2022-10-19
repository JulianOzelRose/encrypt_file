"""
File:           encrypt_file.py
Description:    Encrypts a single line of plaintext from a textfile using a Caesar cipher, then writes the encrypted result to another textfile.
"""

inputFile = open("./input_file.txt", 'r')
outputFile = open("./output_file.txt", 'w')

distance = int(input("Enter distance value: "))

cipherTxt = ""
plainTxt = ""

while True:
    line = inputFile.readline()
    if line == "":
        break

    for i in range(len(line)):
        char = line[i]
        if char.isupper():
            cipherTxt += chr((ord(char) + distance - 65) % 26 + 65)
        else:
            cipherTxt += chr((ord(char) + distance - 97) % 26 + 97)

inputFile.close()

try:
    outputFile.seek(0)
    print("Encrypting...")
    outputFile.truncate(0)
    outputFile.write(cipherTxt)
    outputFile.close()
    print("Encryption successful.")
except:
    print("ERROR: Could not write to file.")
