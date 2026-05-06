# serialization -> Process to convert Python data into JSON format

import json

L = [1,2,3,4]
with open("Sample.json" , "w") as f:
    json.dump(L , f)

D = {
    "Sumit": {
        "age":21,
        "Education":"Under Graduate",
        "dist":"Begusarai"
    },
    "Shivam":{
        "age":13,
        "Education":"Class 8",
        "dist":"Mokama"
    },
    "Shivang":{
        "age":10,
        "Education":4,
        "dist":"Buxar"
    }
}

with open("info.json","w") as f:
    json.dump(D,f)