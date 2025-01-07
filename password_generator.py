# Password generator, användare får välja hur många bokstäver/siffror/symboler
import random

bokstav = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n" "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z",
           "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "Z"]
symboler = ["!", "#", "¤", "%", "&", "/", "=", "?", "@", "£", "$", "€"]
siffror = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

genererade_losenord = []

def generate_pw():
    while True:
        try:
            length_bokstav = int(input("Hur många bokstäver vill du ha i ditt lösenord? (ANGE SIFFRA): "))
            if length_bokstav < 0:
                print("Antalet bokstäver kan inte vara negativt. Försök igen.")
                continue
            break
        except ValueError:
            print("Vänligen ange ett giltigt heltal.")
    
    while True:
        try:
            length_symbol = int(input("Hur många symboler vill du ha i ditt lösenord? (ANGE SIFFRA): "))
            if length_symbol < 0:
                print("Antalet symboler kan inte vara negativt. Försök igen.")
                continue
            break
        except ValueError:
            print("Vänligen ange ett giltigt heltal.")
    
    while True:
        try:
            length_nummer = int(input("Hur många nummer vill du ha i ditt lösenord? (ANGE SIFFRA): "))
            if length_nummer < 0:
                print("Antalet siffror kan inte vara negativt. Försök igen.")
                continue
            break
        except ValueError:
            print("Vänligen ange ett giltigt heltal.")

    pw_bokstav = 0
    pw_symbol = 0
    pw_siffra = 0

    password = ""
    while len(password) < length_bokstav + length_symbol + length_nummer:
        if pw_bokstav < length_bokstav:
            password += random.choice(bokstav)
            pw_bokstav += 1
        elif pw_symbol < length_symbol:
            password += random.choice(symboler)
            pw_symbol += 1
        elif pw_siffra < length_nummer:
            password += random.choice(siffror)
            pw_siffra += 1
    
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    genererade_losenord.append(password)
    print(f"\nGenererat lösenord: {password}\n")

while True:
    generate_pw()
    val = input("Vill du generera ett annat lösenord? Y/N: ").strip().upper()
    if val != "Y":
        print("\nTack för att du använde denna generatorn!\n")
        print("\nLista över genererade lösenord:")
        for index, pw in enumerate(genererade_losenord, start=1):
            print(f"{index}: {pw}")
        break