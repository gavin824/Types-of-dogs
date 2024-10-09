"""
module docstring: main.py
========================

this is the main module of the read/write to file project.
"""

__author__ = "Gavin Chappell"
__version__ = "0.1"
__license__ = "none"
__date__ = "october 7, 2024"

user_submission = input("Cat")

def read_file(file_name) -> None:
    """
    reads a text file and prints it to the console.
    """

    with open(file_name, "r") as f:
        for line in f:
            print(line, end="")

def new_file(file_name) -> None:
    """
    creates new file and writes data to it. or overwrites an exsisting file.
    """
    with open(file_name, "w") as f:
        f.write("Maine Coon")

def append_file(file_name, data) -> None:
    """
    appends data to an existing file.
    """
    with open(file_name, "r") as f:
        lines = f.readlines()


    with open(file_name, "a") as f:
        last_line = lines[-1].strip()
        if lines and last_line != "":
        f.write("\n")
        f.write(data)

def main():
    """
    main entry point of the application.
    """

    append_file("cats.txt", user_submission)

if __name__ == "__main__":
    """
    start the program.
    """

    main()
