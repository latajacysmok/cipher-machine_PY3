#a cipher is given which changes the vowels according to the key:
#key = {"a": "y", "e": "i", "i": "o", "o": "a", "y": "e"}
#The program has a cryptographic function and one that can decrypt the text.

def encryption(s):
    key = {"a": "y", "e": "i", "i": "o", "o": "a", "y": "e"}
    answer = key[letter] if letter in key.keys() else letter for letter in s]
    print("".join(answer))


def decrypt(w):
    key = {"a": "y", "e": "i", "i": "o", "o": "a", "y": "e"}
    answer = [list(key.keys())[list(key.values()).index(letter)] if letter in list(key.values()) 
		else letter for letter in w]
    print("".join(answer))
