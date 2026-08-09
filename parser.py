import sys

all_text = []
to_parse = input("Please enter the word to parse: ")
location = input("Please input location of file to parse: ")
ammount = 0

try:
    with open(f"{location}", "r") as file:
        all_text = file.readlines()
#        print(all_text)
except FileNotFoundError:
    sys.exit("file not found, please make sure file exists or reach out to support ")
else:   
    for word in all_text:
        if word.strip()  == to_parse:
            ammount += 1
    print(f"the word \"{to_parse}\" was found {ammount} times ")