import hashlib
import itertools

def hash_file(filename, hash_value, choice_type):
    if choice_type == "wordlist":
        with open(filename, 'r') as f:
            for line in f.readlines():
                line = line.strip()
                hashed_line = hashlib.md5(line.encode()).hexdigest()
                if hashed_line == hash_value:
                    return print(f"Hash found: {line}")
    else:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for i in range(12):
            for combination in itertools.product(alphabet, repeat=i):
                word = ''.join(combination)
                hashed_line = hashlib.md5(word.encode()).hexdigest()
                if hashed_line == hash_value:
                    return print(f"Hash found: {word}")

    return print("Hash not found")


while True:
    print("""Choice your method for bruteforce :
    1) Attack wordlist
    2) Bruteforce algorithm
    3) Exit
    """)

    choice = int(input("Choice number : "))

    if choice == 1:
        choice_type = "wordlist"
    elif choice == 2:
        choice_type = "bruteforce"
    elif choice == 3:
        print("You have choice quit program !")
        break
    else:
        print("Choice invalid")
        continue

    hash_value = "7952d364913cee56a6b2ec50d1194869"  # klepik
    hash_file('wordlist.txt', hash_value, choice_type)
