import hashlib

while True:
    # Receber uma string via input
    string = input("Digite uma string para gerar o hash: ")

    # Gerar o hash da string por meio do algoritmo SHA-1
    hash_object = hashlib.sha1(string.encode())

    # Imprimir o hash em tela, utilizando o método hexdigest
    hash_hex = hash_object.hexdigest()
    print(f"Hash da string '{string}': {hash_hex}\n")

    # Retornar ao passo 1
