import os
import sys

progName = sys.argv[0]
iFileName = sys.argv[1]
oFileName = sys.argv[2]


def err(msg):
    os.write(2, f"{progName}: {msg}\n".encode());
    sys.exit(1)

def dict_add(key, input_dict):
    if key in input_dict:
        input_dict[key] += 1
    else:
        input_dict.update({key: 1})
    return input_dict

try:
    iFileFd = os.open(iFileName, os.O_RDONLY)
except:
    err(f"can't open file <{iFileName}>")

try:
    oFileFd = os.open(oFileName, os.O_WRONLY)
except:
    err(f"can't open file <{oFileName}>")

input_dict = {}
input_read = ""
instant_read = ""

while True:
    if (instant_read := os.read(iFileFd, 1).decode()):
        if instant_read == " " or instant_read == "," or instant_read =="\n" or instant_read == ".":
            input_dict = dict_add(input_read, input_dict)
            input_read = ""
        else:
            input_read = input_read + instant_read.lower()

    else:
        break

    

for key in input_dict:
    os.write(oFileFd, (key + " : " + str(input_dict[key]) + "\n").encode())

