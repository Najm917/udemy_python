# import word_list
# alphabet=word_list.alphabets

# type_your_messange=input("Enter your message: ")
# shift_word=int(input("Enter your shift word: "))
# direction=input("type 'encrypt' to encrypt and 'decrypt' to decrypt:\n")


# def encrypt (orginal_text,shift_amount):
#   chiper_text=""
#   for letter in orginal_text:
#     shifted_position=alphabet.index(letter)+shift_amount
#     shifted_position%= len(alphabet)
#     chiper_text+=alphabet[shifted_position]
    
#     print(f"Here is the encode result: {chiper_text}")
    
    
# def decrypt (orginal_text,shift_amount):
#   chiper_text=""
#   for letter in orginal_text:
#     shifted_position=alphabet.index(letter)-shift_amount
#     shifted_position%= len(alphabet)
#     chiper_text+=alphabet[shifted_position]
    
#     print(f"Here is the encode result: {chiper_text}")
    
# def ceaser (orginal_text,shift_amount,encode_to_decode):
#     chiper_text=""
#     for letter in orginal_text:
#       shifted_position=alphabet.index(letter)-shift_amount
#       shifted_position%= len(alphabet)
#       chiper_text+=alphabet[shifted_position]
      
#       print(f"Here is the encode result: {chiper_text}")
  
    
# # encrypt(orginal_text=type_your_messange,shift_amount=shift_word)
# decrypt(orginal_text=type_your_messange,shift_amount=shift_word)

import word_list

alphabet = word_list.alphabets

message_input = input("Enter your message to encrypt:\n").lower()
shift_word = int(input("Enter your shift number:\n"))

def caesar(text, shift, direction):
    # Left shifts backward (-), Right shifts forward (+)
    if direction == "left":
        shift = -shift

    result = ""
    for letter in text:
        if letter in alphabet:
            shifted_position = (alphabet.index(letter) + shift) % len(alphabet)
            result += alphabet[shifted_position]
        else:
            result += letter

    return result

# Step 1: Encrypt the original message (defaults to standard forward shift)
encrypted_result = caesar(text=message_input, shift=shift_word, direction="right")
print(f"\nEncrypted message: {encrypted_result}")

# Step 2: Ask if the user wants to decrypt
choice = input("\nDo you want to decrypt a message? Type 'Y' for yes or 'N' for no: ").strip().upper()

if choice == "Y":
    # Ask which specific message to decrypt
    msg_to_decrypt = input("\nEnter the message you want to decrypt: ").lower()
    
    # Ask for direction (left or right)
    shift_dir = input("Enter direction ('left' or 'right'): ").strip().lower()
    
    # Ask for the shift amount
    decrypt_shift = int(input("How many numbers to shift?: "))
    
    decrypted_result = caesar(text=msg_to_decrypt, shift=decrypt_shift, direction=shift_dir)
    print(f"\nDecrypted message: {decrypted_result}")
else:
    print("Process ended.")