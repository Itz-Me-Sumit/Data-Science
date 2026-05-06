# Deserialization -> converting json into python data structure

import json

with open("info.json" , "r") as f:
    data = json.load(f)
    print(type(data))
    print(data)