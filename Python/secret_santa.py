
from array import array
from cgi import test
from operator import length_hint
import random

people = {"Johan", "Oskar", "Samuel", "Carina", "Anders", "Viktor", "Gustav", "Linda", "Hakan"}

coded_length = 15

key_and_length_offset = 100

def encrypt(name, key=0):
    output = []
    out_name = ""
    output.append(key + key_and_length_offset)
    length = len(name)
    output.append(length + key_and_length_offset)
    for l in name:
        output.append(ord(l) + key)
        print(ord(l))

    while(len(output) < coded_length):
        output.append(random.randint(90, 121))

    for l in output:
        out_name += chr(l)
    return out_name

def decrypt(name):
    name_array = []
    for l in name:
        name_array.append(ord(l))
    out_name = ""
    key = name_array[0] - key_and_length_offset
    length = name_array[1] - key_and_length_offset
    iteration = -1
    skip_first = 2
    for l in name_array:
        iteration += 1
        if iteration < skip_first:
            continue
        if iteration - skip_first >= length:
            return out_name
        out_name += chr(l - key)

print("Enter 0 to encrypt message")
print("Enter 1 to decrypt message")

mode = input("Input: ")

while(mode != "1" and mode != "0"):
    mode = input("Invalid input. Please enter either a '1' or a '0': ")

mode_name = ""

if mode == "0":
    mode_name = "encrypt"
elif mode == "1":
    mode_name = "decrypt"

message = input("Please enter the message to " + mode_name + ": ")

if mode == "0":
    print(encrypt(message, random.randrange(5,10)))
elif mode == "1":
    print(decrypt(message))
else: 
    print("ERROR")




# for person in people:
#     test_name = person
#     test_key = random.randrange(5,10)
#     test_encrypted = encrypt(test_name, test_key)
#     test_decrypted = decrypt(test_encrypted)

#     print("Encrypted " + test_name + ": " + str(test_encrypted))

#     print("Decrypted: " + str(test_decrypted))

#     print("\n")


# print("\n" + decrypt("ijHfwnsfrpja^jp"))

#for person in people:
    #encrypt(person)
    #print("\n")




