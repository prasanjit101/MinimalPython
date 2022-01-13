import os
import hashlib

def hashFile(filename):
    BLOCKSIZE = 65536
    # For large files, if we read it all together it can lead to memory overflow, So we take a blocksize to read at a time
    hasher = hashlib.md5()
    with open(filename, 'rb') as file:
        buf = file.read(BLOCKSIZE) # Reads the particular blocksize from file
        while(len(buf) > 0):
            hasher.update(buf)
            buf = file.read(BLOCKSIZE)
    return hasher.hexdigest()


if __name__ == "__main__":
    hashMap = {}#hash:filename

    # stores deleted files names
    deletedFiles = []
    file_list = [f for f in os.listdir() if os.path.isfile(f)]
    for f in file_list:
        key = hashFile(f)
        # If key already exists, it deletes the file
        if key in hashMap.keys():
            deletedFiles.append(f)
            os.remove(f)
        else:
            hashMap[key] = f
    if len(deletedFiles) == 0:
        print('Deleted Files')
        for i in deletedFiles:
            print(i)
    else:
        print('No duplicate files found')
