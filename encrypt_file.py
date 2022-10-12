"""
File:           encrypt_file.py
Description:    Encrypts a single line of plaintext from a textfile using a Caesar cipher, then writes the encrypted result to another textfile.
"""

inputFile = open("./input_file.txt", 'r')
outputFile = open("./output_file.txt", 'w')

distance = int(input("Enter distance value: "))

cipherTxt = ""

while True:
    line = inputFile.readline()
    if line == "":
        break

    for ch in line:
        ordVal = ord(ch)
        cipherVal = ordVal + distance

        if cipherVal > ord('z'):
            cipherVal = ord('a') + distance - (ord('z') - ordVal + 1)
        if ch == " ":
            cipherTxt += "#"
        else:
            cipherTxt += chr(cipherVal)

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
