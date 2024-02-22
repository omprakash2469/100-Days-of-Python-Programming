from random import choice


def random_string(len):
    """ Get randome text by the given length """
    characters = "abcdefghijklmnopqrstuvwxyz"
    return ''.join(choice(characters) for i in range(len))


def encode_string(string):
    """
    Encode the given string in the defined format
    """
    if len(string) < 3:
        # Reverse the string if the length of the string is less than 3
        print(f"Your encrypted word is: {string[::-1]}")
        return string[::-1]
    else:
        # Encrypt the text
        encoded_string = random_string(3) + string[1:] + string[:1] + random_string(3)
        print(f"Your encrypted string is: {encoded_string}")
        return encode_string


def decode_string(string):
    """
    Decode the given string in the defined format
    """
    if len(string) < 3:
        print(f"Your decrypted text is: {string[::-1]}")
        return string[::-1]
    else:
        # Decrypt the text
        decode_string = string[3:-3]
        decoded_string = decode_string[len(decode_string) - 1] + decode_string[:-1]

        print(f"Your decrypted text is: {decoded_string}")
        return decoded_string


code = input("Enter your text: ")
print("\nWhat you want to do with the text? \n 1: Encryption\n 2: Decryption \n")
action = int(input("Select your method: "))


if action == 1:
    encode_string(code)
elif action == 2:
    decode_string(code)
else:
    print("Please select a valid method for action")

