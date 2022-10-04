
from array import array
from cgi import test
from collections import namedtuple
from operator import length_hint
import random

year = "2022"

link = "https://secret-santa-viktor-gustav.vercel.app/"

Person = namedtuple('Person', ['name', 'gave_to_last_year'])

people = [  Person("Johan", "Gustav"), Person("Oscar", "Carina"), Person("Samuel", "Hakan"),
            Person("Carina", "Viktor"), Person("Anders", "Samuel"), Person("Viktor", "Oscar"),
            Person("Gustav", "Linda"), Person("Linda", "Anders"), Person("Hakan", "Johan"), 
            Person("Matilda", "Oscar")]

random.shuffle(people)

coded_length = 15

key_and_length_offset = 100

def encrypt(name, key=0):
   if key == 0:
      key = random.randrange(5,10)
   output = []
   out_name = ""
   output.append(key + key_and_length_offset)
   length = len(name)
   output.append(length + key_and_length_offset)
   for l in name:
      output.append(ord(l) + key)

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

def generate_secret_santas(people_list):
   original_list = people_list.copy()

   random.shuffle(original_list)
   random.shuffle(people_list)

   showDecrypted = True

   for person in original_list:
      for target_person in people_list:
         if person.name == target_person.name or person.gave_to_last_year == target_person.name:
            continue
         encrypted_recipient = encrypt(target_person.name)
         #print(person.name + " --> " + encrypted_recipient + " | Last year: " + person.gave_to_last_year + showDecrypted * (" | Decrypted: " + decrypt(encrypted_recipient)))
         people_list.remove(target_person)

         print("Hej " + person.name + "!\n\n" + 
                "Nu ska du få reda på vem du ska ge i julklappsleken " + year + ".\n" +
                "Du ska gå in på: " + link + " och mata in koden som kommer i nästa meddelande.\n" +
                "Om du får den du fick förra året eller om andra problem uppstår har du hittat en bug, säg till då!\n\n" +
                "God jul!\n\n\n" +
                 encrypted_recipient + "\n\n\n\n")

         break
         
generate_secret_santas(people)



# print("Enter 0 to encrypt message")
# print("Enter 1 to decrypt message")

# mode = input("Input: ")

# while(mode != "1" and mode != "0"):
#     mode = input("Invalid input. Please enter either a '1' or a '0': ")

# mode_name = ""

# if mode == "0":
#     mode_name = "encrypt"
# elif mode == "1":
#     mode_name = "decrypt"

# message = input("Please enter the message to " + mode_name + ": ")

# if mode == "0":
#     print(encrypt(message, random.randrange(5,10)))
# elif mode == "1":
#     print(decrypt(message))
# else: 
#     print("ERROR")


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




