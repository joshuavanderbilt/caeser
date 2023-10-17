# Caeser Cipher Utility by Joshua.
# This program allows you to encrypt or decrypt text using the Caeser Cipher.

def caeser(message,decrypt): # Add an argument which controls whether to decrypt or encrypt.
    ciphertext =""
    for x in message:
      number = ord(x) # Convert the letter to a numeric value.
      if number != 32: # Only encrypt or decrypt the letter if it is NOT a space.
        number = number - ord('A') # Subtract the unicode for A.
        if decrypt == 1: # If the argument is set to 1, it decrypts. Otherwise, it encrypts.
            number = number - 4 # Decrypt by subtracting by four.
        else:
            number = number + 4 # Encrypt by adding four.
        number = number % 26 # Find the remainder.
        number = number + ord('A') # Add back the unicode for A.
      letter = chr(number) # Convert the numeric value back to a letter.
      ciphertext = ciphertext + letter # Append to the text.
    return(ciphertext) # Return the text.
      

print("Caeser Cipher Utility.")
while True:
  todo = input("Type e to encrypt, or d to decrypt:")
  if todo == "e" or todo == "d":
    break
  else:
    print("Please type e or d.")
while True:
  message = input("Type or paste the text to manipulate:")
  if message.isupper and message.isalpha():
    break
  else:
    print("Please use capital letters and spaces only.")

if todo == "e":
    print("Your encrypted text is:",caeser(message,0))
if todo == "d":
    print("Your decrypted text is:",caeser(message,1))