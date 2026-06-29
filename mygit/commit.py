import os
import time
import hashlib

def create_commit(message):
    if not os.path.exists(".git/index"):
        print("Nothing to commit.")
        return

    with open(".git/index", "r") as index:
        staged = index.read()

    content = f"""message: {message}
time: {time.ctime()}

{staged}
"""

    sha = hashlib.sha1(content.encode()).hexdigest()

    with open(f".git/objects/{sha}", "w") as obj:
        obj.write(content)

    with open(".git/HEAD", "w") as head:
        head.write(sha)

    print("Commit created:", sha)
