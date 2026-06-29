import hashlib
from mygit.index import stage_file

def create_blob(filename):
    with open(filename, "rb") as f:
        data = f.read()

    sha = hashlib.sha1(data).hexdigest()

    with open(f".git/objects/{sha}", "wb") as obj:
        obj.write(data)

    stage_file(filename, sha)

    print("Blob created:", sha)
