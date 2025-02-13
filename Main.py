import os
import hashlib

def hash_file(filename):
    h = hashlib.md5()
    with open(filename, 'rb') as file:
        while chunk := file.read(8192):
            h.update(chunk)
    return h.hexdigest()

def find_duplicates(folder):
    hashes = {}
    for dirpath, _, filenames in os.walk(folder):
        #print(filenames)
        #print(dirpath)
        for f in filenames:
            full_path = os.path.join(dirpath, f)
            file_hash = hash_file(full_path)
            #print(full_path)
            #print(file_hash)
            if file_hash in hashes:
                print(f'duplicates were found: {full_path}') == {hashes[file_hash]}
                delete = input(f'¿Do you want delete duplicated files {full_path}? (s/n): ').strip().lower()
                if delete == 's':
                    os.remove(full_path)
                    print(f'File {full_path} deleted.')
                else:
                    print(f'Files {full_path} not deleted.')
            else:
                hashes[file_hash] = full_path

find_duplicates('files')