import os
import hashlib

def hash_file(filename):
    h = hashlib.md5()
    with open(filename, 'rb') as file:
        while chunk := file.read(8192):
            h.update(chunk)
    return h.hexdigest()

archivo = 'files/texto.txt'

print(hash_file(archivo))