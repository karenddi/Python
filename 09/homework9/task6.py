import io

def opening_file(filename):
    try:

        with open(filename, "r") as fopen:
            lines = fopen.readlines()
            print(lines)

    except FileNotFoundError as err:
        print(err, "There is no such file, check it again!")



def reading_opened_file(file):
    try:
        with open(file, "w") as fopen:
            lines = fopen.read()
            print(lines)
    except FileNotFoundError as err:
        print(err, "There is no such file, check it again!")
    except io.UnsupportedOperation as err2:
        print(err2, "Wrong mode, you cannot read files in mode w!")

def x_mode(file):
    try:
        with open(file, "x") as fout:
            lines = fout.write()
    except FileExistsError as err:
        print(err, "WARNING: File already exists!")
    except TypeError as er:
        print(er)
