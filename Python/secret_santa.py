
from array import array
#from cgi import test
from collections import namedtuple
from operator import length_hint
import random
import numpy as np

year = "2023"

link = "https://secret-santa-viktor-gustav.vercel.app/"

Person = namedtuple('Person', ['name', 'family', 'given_to'])

#                                                  2021      2022
people = [  Person("Johan",   "Knutsson",       {"Gustav",  "Oscar"     }), 
            Person("Oscar",   "Knutsson",       {"Carina",  "Hakan"     }), 
            Person("Samuel",  "Knutsson",       {"Hakan",   "Matilda"   }),
            Person("Carina",  "Knutsson",       {"Viktor",  "Linda"     }), 
            Person("Anders",  "Knutsson",       {"Samuel",  "Carina"    }), 
            Person("Viktor",  "Abrahamsson",    {"Oscar",   "Anders"    }),
            Person("Gustav",  "Abrahamsson",    {"Linda",   "Viktor"    }), 
            Person("Linda",   "Abrahamsson",    {"Anders",  "Gustav"    }), 
            Person("Hakan",   "Abrahamsson",    {"Johan",   "Samuel"    })]
           # Person("Matilda", "Knutsson",       {"Oscar",   "Johan"     })]

random.shuffle(people)

family_bias = 0.2

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

   num_same_fam = 0
   num_people = 0

   original_list = people_list.copy()
   people_list2 = people_list.copy()

   random.shuffle(original_list)
   random.shuffle(people_list2)

   showDecrypted = True

   for person in original_list:
      for target_person in people_list2:
         # Don't give to yourself, or to the people you have given to
         if person.name == target_person.name or target_person.name in person.given_to:
            continue
         
         # # Introduce family bias if desired not met
         # if person.family == target_person.family:
         #    if random.random() < family_bias or num_same_fam >= 2:
         #       continue
         #    else:
         #       num_same_fam += 1

         # Count the people giving to people in their family
         if person.family == target_person.family:
            num_same_fam += 1

         encrypted_recipient = encrypt(target_person.name)
         #print(person.name + " --> " + encrypted_recipient + " | Last year: " + person.given_to + showDecrypted * (" | Decrypted: " + decrypt(encrypted_recipient)))
         people_list2.remove(target_person)

         num_people += 1

         print("Hej " + person.name + "!\n\n" + 
                "Nu ska du få reda på vem du ska ge i julklappsleken " + year + ".\n" +
                "Du ska gå in på: " + link + " och mata in koden som kommer i nästa meddelande.\n" +
                "Om du får den du fick förra året eller om andra problem uppstår har du hittat en bug, säg till då!\n\n" +
                "God jul!\n\n\n" +
                 encrypted_recipient + "\n\n\n\n")

         break

   return num_same_fam, num_people


# Generate secret santa with a tolerance "[min, max]" of the number of people who give to their own family members
def generate(min, max):
   num_same = 0
   num_people = 0
   while (num_same < min or num_same > max or num_people != len(people)):
      print("------------------------------------------------------------------------")
      num_same, num_people = generate_secret_santas(people)

   #print("Found a 'num_same' = " + str(num_same))
   print("Number of people = " + str(num_people))

generate(2, 3)


#generate_secret_santas(people)


# # Testing
num_same = []
# for i in range(1,100):
#    num_same.append(generate_secret_santas(people))

# print(num_same)
# print("Mean: " + str(np.mean(num_same)))
# print("3-sigma: " + str(3 * np.std(num_same)))



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




