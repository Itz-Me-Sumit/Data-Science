# FILE READ

with open("demo.txt", "r") as f:
    content = f.read()   # pura file ek baar me read
    print(content)

with open("demo.txt", "r") as f:
    print(f.readline())   # sirf 1 line

with open("demo.txt", "r") as f:
    print(f.readlines())  # list me sab lines

with open("demo.txt", "r") as f:
    print(f.read(5))   # first 5 characters
    print(f.read(5))   # next 5 characters (pointer aage badh gaya)

# seek() kya karta hai?
with open("demo.txt", "r") as f:
    f.seek(0)   # pointer ko start pe le aata hai
    print(f.read())