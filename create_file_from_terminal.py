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



'''323. Create file from terminal

Create an app create_file.py that takes directory path, file name, file content from the terminal and creates file. There should be flags -d or -f:

If only -d flag passed, means all items after this flag are parts of the path.
python create_file.py -d dir1 dir2 - creates directory dir1/dir2 inside current directory.

If only -f flag passed, means first item is the file name.
python create_file.py -f file.txt

After pressing Enter it creates file file.txt and then terminal should ask you to input content lines until you input "stop":

Enter content line: Line1 content
Enter content line: Line2 content
Enter content line: Line3 content
Enter content line: stop
This creates file file.txt inside current directory with content:

2022-02-01 14:41:10
1 Line1 content
2 Line2 content
3 Line3 content
App should add current timestamp at the top and number lines. If file.txt already exists it should add content below:

python create_file.py -f file.txt

Enter content line: Another line1 content
Enter content line: Another line2 content
Enter content line: Another line3 content
Enter content line: stop
2022-02-01 14:41:10
1 Line1 content
2 Line2 content
3 Line3 content

2022-02-01 14:46:01
1 Another line1 content
2 Another line2 content
3 Another line3 content
If both -d and -f flags passed, app creates directory and file with content inside this directory.
python create_file.py -d dir1 dir2 -f file.txt

Enter content line: Line1 content
Enter content line: Line2 content
Enter content line: Line3 content
Enter content line: stop
Creates directory dir1/dir2 inside current directory and creates file file.txt inside that directory with content:

dir1/dir2/file.txt: 

2022-02-01 14:46:01
1 Line1 content
2 Line2 content
3 Line3 content
It would be relevant to use:

sys.argv to read arguments from the terminal
os.makedirs to create directories
.strftime() method for datetime.now() to make timestamp more beautiful.'''
