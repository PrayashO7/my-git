import os
from objects import read_object

def print_log():
    """Traverses the commit history backwards starting from HEAD and prints it."""
    head_path = os.path.join('.mygit', 'HEAD')
    if not os.path.exists(head_path):
        print("fatal: Not a valid object name HEAD")
        return

    # 1. Find the starting commit SHA-1 from HEAD
    with open(head_path, 'r') as f:
        head_ref = f.read().strip()
    
    current_commit_sha1 = None
    if head_ref.startswith("ref: "):
        ref_path = os.path.join('.mygit', head_ref.split(' ')[1])
        if os.path.exists(ref_path):
            with open(ref_path, 'r') as f:
                current_commit_sha1 = f.read().strip()
    else:
        current_commit_sha1 = head_ref

    if not current_commit_sha1:
        print("fatal: your current branch does not have any commits yet")
        return

    # 2. Walk backwards through parents
    while current_commit_sha1:
        try:
            type_str, content = read_object(current_commit_sha1)
        except FileNotFoundError:
            break
            
        if type_str != "commit":
            break

        commit_text = content.decode('utf-8')
        lines = commit_text.split('\n')
        
        # Parse the commit file metadata
        metadata = {}
        message_lines = []
        is_message = False
        
        for line in lines:
            if is_message:
                message_lines.append(line)
            elif line == "":
                is_message = True # Empty line marks the beginning of the message
            else:
                key, val = line.split(' ', 1)
                metadata[key] = val

        # Print the formatted commit log block
        print(f"\033[33mcommit {current_commit_sha1}\033[0m") # Yellow color for hash
        if 'author' in metadata:
            print(f"Author: {metadata['author']}")
        print("\n" + "".join([f"    {msg}\n" for msg in message_lines if msg.strip()]))
        print("-" * 40)

        # Move to the parent commit hash for the next loop iteration
        current_commit_sha1 = metadata.get('parent')
