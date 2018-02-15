def encryption(s):
    klucz = {"a": "y", "e": "i", "i": "o", "o": "a", "y": "e"}
    answer = [klucz[letter] if letter in klucz.keys() else letter for letter in s]
    print("".join(answer))

encryption("to jest moj tekst")

def decrypt(w):
    klucz = {"a": "y", "e": "i", "i": "o", "o": "a", "y": "e"}
    answer = [list(klucz.keys())[list(klucz.values()).index(letter)] if letter in list(klucz.values()) else letter for letter in w]
    print("".join(answer))

decrypt("noi zypomnoj a dakumintycjo")