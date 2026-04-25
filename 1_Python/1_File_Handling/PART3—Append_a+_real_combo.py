#  APPEND MODE

# 'a' = file me add karega (purana data safe)
with open("demo.txt", "a") as f:
    f.write("Line 3: Yeh append hua hai\n")

# a+ (append + read)
with open("demo.txt", "a+") as f:
    f.write("Line 4: a+ mode use kiya\n")

    f.seek(0)   #IMPORTANT
    print(f.read())

