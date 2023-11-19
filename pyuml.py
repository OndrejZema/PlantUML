#!/usr/bin/python3

import sys
import requests 
import os

def convert_plantuml(file_name:str):
    with open(file_name, mode="r", encoding="utf-8") as f:    
        uml_text = f.read()

        uml_hex = uml_text.encode("utf-8").hex()

        res = requests.get(f"http://plantuml.com/plantuml/png/~h{uml_hex}")

        with open(".".join(file_name.split(".")[:-1]) + ".png", mode="wb") as bf:
            bf.write(res.content)


def main(file_name):
    if(file_name == "."):
        files = os.listdir(os.getcwd())
        for f in files:
            if os.path.isfile(f):
                if f.endswith(".plantuml"):
                    convert_plantuml(f)
    else:
        if os.path.exists(file_name) and os.path.isfile(file_name):
            convert_plantuml(file_name)


if __name__ == "__main__":
    print(os.getcwd())
    if(len(sys.argv) < 1):
        print("Required file name")
        exit()
    main(sys.argv[1])
