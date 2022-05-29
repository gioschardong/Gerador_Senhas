import string
from random import random, choice

valores = string.ascii_letters  # todas as letras maiusculas e minusculas
valores += string.digits  # Numeros de 0 a 9
valores += string.punctuation  # Caracteres especiais

tamanho = 8
senha = ""

for i in range(tamanho):
    senha += choice(valores)

print(senha)
