# FILE CREATE + WRITE

# 'w' mode = file create karega (agar exist nahi hai)
# aur agar file pehle se hai → pura data delete karke naya likhega

with open("demo.txt", "w") as f:
    f.write("Line 1: Hello Bhai\n")
    f.write("Line 2: File handling seekh rahe hain\n")

print("File create ho gayi aur data likh diya")