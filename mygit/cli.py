import sys
from mygit.repository import init
from mygit.objects import create_blob

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>")
        return

    command = sys.argv[1]

    if command == "init":
        init()

    elif command == "add":
        if len(sys.argv) < 3:
            print("Usage: python main.py add <file>")
            return

        create_blob(sys.argv[2])

    else:
        print("Unknown command:", command)
