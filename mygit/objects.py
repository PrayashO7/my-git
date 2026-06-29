import os
import hashlib
import zlib

def hash_object(data, type_str="blob", write=True):
    """Hashes data, creates a Git object header, and optionally writes it to disk."""
    # Git prefixes content with: "type size\0"
    header = f"{type_str} {len(data)}".encode('utf-8')
    full_content = header + b'\x00' + data
    
    # Calculate SHA-1 hash
    sha1 = hashlib.sha1(full_content).hexdigest()
    
    if write:
        # Path: .mygit/objects/first_2_chars/remaining_38_chars
        obj_dir = os.path.join('.mygit', 'objects', sha1[:2])
        obj_path = os.path.join(obj_dir, sha1[2:])
        
        if not os.path.exists(obj_dir):
            os.makedirs(obj_dir)
            
        # Compress using zlib before saving
        compressed_data = zlib.compress(full_content)
        with open(obj_path, 'wb') as f:
            f.write(compressed_data)
            
    return sha1

def read_object(sha1):
    """Reads a Git object by its SHA-1 hash and returns (type, content)."""
    obj_path = os.path.join('.mygit', 'objects', sha1[:2], sha1[2:])
    if not os.path.exists(obj_path):
        raise FileNotFoundError(f"Object {sha1} not found.")
        
    with open(obj_path, 'rb') as f:
        raw_data = zlib.decompress(f.read())
        
    # Split header and content at the null byte
    header, content = raw_data.split(b'\x00', 1)
    type_str, size = header.decode('utf-8').split(' ')
    
    return type_str, content
