# PART 3: finally block

try:
    f = open("demo.txt", "r")
    print("File open ho gayi")

except FileNotFoundError:
    print("File nahi mili")

finally:
    print("Ye hamesha chalega (cleanup ke liye)")