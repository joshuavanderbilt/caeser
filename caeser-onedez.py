# Caeser Cipher Utility by Joshua rewritten version by onedez on CheesCcord.
# This program allows you to encrypt or decrypt text using the Caeser Cipher.

from sys import argv

if len(argv) != 3:
  print("incorrect number of arguments",
        f"expected 2 arguments, but got {len(argv) - 1} arguments",
        f"usage: {argv[0]} (e or d for encrypt or decrypt respectively) (input message)"
  )
  exit(1)


encrypting = True
message = argv[2].upper()
  
if argv[1] == 'd':
  encrypting = False
elif argv[1] != 'e':
  print(f"expected 'e' or 'd' for argument 1, got \"{argv[1]}\" instead")
  exit(1)


output = ""

for letter in message:
  if not letter.isalpha():
    output = output + letter
    continue
  
  letter_ord = ord(letter)
  
  if letter_ord == ord(' '):
    output = output + ' '
    continue
   
  letter_ord -= ord('A')
  
  letter_ord += 4 if encrypting else -4
  letter_ord %= 26
  
  letter_ord += ord('A')
  
  output = output + chr(letter_ord)
 
print(output)
