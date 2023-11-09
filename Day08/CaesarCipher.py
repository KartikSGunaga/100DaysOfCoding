alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
if(shift > 26):
    shift %= 26

def encryptOrDecrypt(text):
    encodedMessage = ""
    for letter in text:
        for position in range(len(alphabet)):
            if(letter == alphabet[position]):
                if(shift + position > 26):
                    pos = 26 - position + shift
                    encodedMessage += alphabet[pos]
                else:
                    pos = position + shift
                    encodedMessage += alphabet[pos]
    return encodedMessage

if(direction == "encode"):
    print(f"Your encoded message is: {encryptOrDecrypt(text)}")
elif(direction == "decode"):
    print(f"Your decoded message is: {encryptOrDecrypt(text)}")
else:
    print("Invalid entry")


