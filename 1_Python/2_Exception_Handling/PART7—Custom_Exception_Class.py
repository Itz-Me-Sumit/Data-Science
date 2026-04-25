# PART 7: Custom exception class

class MyError(Exception):
    pass

try:
    raise MyError("Mera khud ka error")

except MyError as e:
    print("Custom error:", e)