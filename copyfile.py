import sys

try:
    with open(f"{sys.argv[1]}") as file:
        global all_lines
        all_lines = file.readlines()
except FileNotFoundError:
    sys.exit("Sorry file you want to copy is not found ")
except IndexError:
    sys.exit("error, no files mentioned, did you perheps forgot to specify files to copy? ")
except:
    sys.exit("Woops unexpected error has happened please contact our support group ")


for file_name in sys.argv[2:]:
    with open(f"{file_name}", "w") as file2:
        for i in all_lines:
            file2.write(f"{i}")