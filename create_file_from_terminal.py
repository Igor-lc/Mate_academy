from os import path, makedirs, chdir
from datetime import datetime as dt
from sys import argv

filename = None  # responsible for creating a file
dirs = None  # responsible for creating catalogs
f_dir = input("Enter a filename and directory as here '-f filename.txt -d DirOne dirTwo': ")
argv.extend(f_dir.split())
# parser for command-line arguments
# or you can use argparse: https://docs.python.org/3/library/argparse.html
for idx, arg in enumerate(argv[:-1]):
    next_arg = argv[idx + 1]
    if arg == "-f":
        filename = next_arg
    if arg == "-d":
        dirs = next_arg + "/"
        continue
    if dirs and arg != "-f" and next_arg != "-f":
        dirs += next_arg + "/"

if filename:
    try:
        if dirs:
            makedirs(dirs) if not path.exists(dirs) else False  # https://docs.python.org/3/library/os.path.html#os.path.exists
            chdir(dirs)
        with open(filename, "a", encoding="utf-8") as f:
            data, i = '', 1
            while True:
                line = input("Enter content line: ")
                if line == "stop":
                    now = dt.now().strftime('%Y-%m-%d %H:%M:%S') + '\n'
                    print(now + data, file=f)
                    break
                data += str(i) + ' ' + line + '\n'
                i += 1
    except (PermissionError, NotADirectoryError):
        print("File system limitation. Please use a different name or use: my_task.txt or my_task.py")
