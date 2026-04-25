# PART 5: Exception as e

try:
    x = int("hello")

except Exception as e:
    print("Actual error:", e)