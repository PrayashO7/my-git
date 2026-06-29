import argparse
import sys
import os
import repository
import index
import commit
import log # Added import

def cmd_init(args):
    repository.repo_init()

def cmd_add(args):
    if not os.path.exists('.mygit'):
        print("fatal: not a mygit repository")
        sys.exit(1)
    for path in args.path:
        index.add_file(path)

def cmd_commit(args):
    if not os.path.exists('.mygit'):
        print("fatal: not a mygit repository")
        sys.exit(1)
    commit.create_commit(args.message)

def cmd_log(args):
    if not os.path.exists('.mygit'):
        print("fatal: not a mygit repository")
        sys.exit(1)
    log.print_log() # Added handler

def main():
    parser = argparse.ArgumentParser(description="MyGit")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    subparsers.add_parser('init')
    
    parser_add = subparsers.add_parser('add')
    parser_add.add_argument('path', nargs='+')
    
    parser_commit = subparsers.add_parser('commit')
    parser_commit.add_argument('-m', '--message', required=True)
    
    # New Log Command Configuration
    subparsers.add_parser('log', help='Show commit history logs')
    
    args = parser.parse_args()
    
    if args.command == 'init':
        cmd_init(args)
    elif args.command == 'add':
        cmd_add(args)
    elif args.command == 'commit':
        cmd_commit(args)
    elif args.command == 'log':
        cmd_log(args)

if __name__ == '__main__':
    main()
