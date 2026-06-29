import argparse
import sys
import os
import repository
import index

def cmd_init(args):
    repository.repo_init()

def cmd_add(args):
    if not os.path.exists('.mygit'):
        print("fatal: not a mygit repository (or any of the parent directories)")
        sys.exit(1)
        
    for path in args.path:
        index.add_file(path)

def main():
    parser = argparse.ArgumentParser(description="MyGit - A Git implementation from scratch")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # Init Command
    subparsers.add_parser('init', help='Initialize a new, empty repository')
    
    # Add Command
    parser_add = subparsers.add_parser('add', help='Add file contents to the index')
    parser_add.add_argument('path', nargs='+', help='Files to add')
    
    args = parser.parse_args()
    
    if args.command == 'init':
        cmd_init(args)
    elif args.command == 'add':
        cmd_add(args)

if __name__ == '__main__':
    main()
