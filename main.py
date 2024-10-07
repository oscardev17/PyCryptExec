from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()

def encrypt_file(filename):
    key = load_key()
    f = Fernet(key)
    
    with open(filename, "rb") as file:
        file_data = file.read()
    
    encrypted_data = f.encrypt(file_data)
    
    with open(filename, "wb") as file:
        file.write(encrypted_data)
    print(f"{filename} a été chiffré avec succès.")

def decrypt_and_execute(filename):
    key = load_key()
    f = Fernet(key)
    
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    
    decrypted_data = f.decrypt(encrypted_data)
    
    exec(decrypted_data)
    print(f"{filename} a été déchiffré et exécuté avec succès.")

def menu():
    os.system('cls')
    print("==== Menu de Chiffrement/Déchiffrement ====")
    print("1. Chiffrer un fichier")
    print("2. Déchiffrer et exécuter un fichier")
    print("3. Quitter")
    print("===========================================")

if __name__ == "__main__":
    try:
        load_key()
    except FileNotFoundError:
        print("Clé introuvable. Génération d'une nouvelle clé...")
        generate_key()

    while True:
        menu()
        choice = input("Choisissez une option (1/2/3) : ")

        if choice == "1":
            filename = input("Entrez le nom du fichier à chiffrer : ")
            encrypt_file(filename)

        elif choice == "2":
            filename = input("Entrez le nom du fichier à déchiffrer et exécuter : ")
            decrypt_and_execute(filename)

        elif choice == "3":
            print("Quitter le programme.")
            break

        else:
            print("Option invalide, veuillez réessayer.")
