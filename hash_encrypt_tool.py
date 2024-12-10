import hashlib
from cryptography.fernet import Fernet

# Função para gerar hash de uma string
def generate_hash(data, algorithm='sha256'):
    hash_function = getattr(hashlib, algorithm)
    hash_object = hash_function(data.encode())
    return hash_object.hexdigest()

# Função para gerar hash de um arquivo
def file_hash(file_path, algorithm='sha256'):
    hash_function = getattr(hashlib, algorithm)
    with open(file_path, 'rb') as file:
        file_data = file.read()
        hash_object = hash_function(file_data)
    return hash_object.hexdigest()

# Função para criptografia com AES
def generate_key():
    return Fernet.generate_key()

def encrypt_message(key, message):
    fernet = Fernet(key)
    return fernet.encrypt(message.encode())

def decrypt_message(key, encrypted_message):
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_message).decode()

# Função para salvar resultados em um arquivo
def save_results(filename, data):
    with open(filename, 'w') as file:
        file.write(data)
    print(f"Resultados salvos em {filename}")

# Função para validar hashes
def validate_hash(data, provided_hash, algorithm='sha256'):
    generated_hash = generate_hash(data, algorithm)
    return generated_hash == provided_hash

# Menu interativo
if __name__ == "__main__":
    while True:
        print("\n=== Ferramenta de Hash e Criptografia ===")
        print("1. Gerar hash de uma string")
        print("2. Gerar hash de um arquivo")
        print("3. Validar hash")
        print("4. Criptografar mensagem (AES)")
        print("5. Descriptografar mensagem (AES)")
        print("6. Sair")
        
        choice = input("Escolha uma opção: ")

        if choice == "1":
            data = input("Digite a string: ")
            algorithm = input("Escolha o algoritmo (md5, sha1, sha256, sha512): ").lower()
            hash_result = generate_hash(data, algorithm)
            print(f"Hash ({algorithm}): {hash_result}")
            save_results("string_hash_result.txt", f"Hash ({algorithm}): {hash_result}")

        elif choice == "2":
            file_path = input("Digite o caminho do arquivo: ")
            algorithm = input("Escolha o algoritmo (md5, sha1, sha256, sha512): ").lower()
            hash_result = file_hash(file_path, algorithm)
            print(f"Hash do Arquivo ({algorithm}): {hash_result}")
            save_results("file_hash_result.txt", f"Hash do Arquivo ({algorithm}): {hash_result}")

        elif choice == "3":
            data = input("Digite a string: ")
            provided_hash = input("Digite o hash fornecido: ")
            algorithm = input("Escolha o algoritmo (md5, sha1, sha256, sha512): ").lower()
            is_valid = validate_hash(data, provided_hash, algorithm)
            print("Hash válido!" if is_valid else "Hash inválido!")

        elif choice == "4":
            key = generate_key()
            print(f"Chave gerada (guarde-a): {key.decode()}")
            message = input("Digite a mensagem para criptografar: ")
            encrypted_message = encrypt_message(key, message)
            print(f"Mensagem Criptografada: {encrypted_message}")
            save_results("encrypted_message.txt", f"Chave: {key.decode()}\nMensagem Criptografada: {encrypted_message.decode()}")

        elif choice == "5":
            key = input("Digite a chave: ").encode()
            encrypted_message = input("Digite a mensagem criptografada: ").encode()
            try:
                decrypted_message = decrypt_message(key, encrypted_message)
                print(f"Mensagem Descriptografada: {decrypted_message}")
            except Exception as e:
                print("Erro ao descriptografar", e)

        elif choice == "6":
            print("Encerrando...")
            break

        else:
            print("Opção inválida. Tente novamente.")
