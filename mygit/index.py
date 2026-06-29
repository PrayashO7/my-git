import os

INDEX_PATH = os.path.join('.mygit', 'index')

def read_index():
    """Reads the index file and returns a dictionary of {path: sha1}."""
    index = {}
    if not os.path.exists(INDEX_PATH):
        return index
        
    with open(INDEX_PATH, 'r') as f:
        lines = f.read().splitlines()
        
    for line in lines:
        if line.strip():
            sha1, path = line.split(' ', 1)
            index[path] = sha1
            
    return index

def write_index(index):
    """Writes the index dictionary back to the index file."""
    with open(INDEX_PATH, 'w') as f:
        for path, sha1 in sorted(index.items()):
            f.write(f"{sha1} {path}\n")

def add_file(file_path):
    """Stages a single file by hashing it and updating the index."""
    if not os.path.exists(file_path):
        print(f"fatal: pathspec '{file_path}' did not match any files")
        return

    with open(file_path, 'rb') as f:
        data = f.read()
        
    # 1. Hash and write the file content as a blob
    from objects import hash_object
    sha1 = hash_object(data, type_str="blob")
    
    # 2. Update the index mapping
    index = read_index()
    index[file_path] = sha1
    write_index(index)
    
    print(f"Staged {file_path}")
