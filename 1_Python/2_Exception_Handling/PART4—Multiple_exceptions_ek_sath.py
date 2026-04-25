# PART 4: Multiple exceptions

try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print(a / b)

except (ValueError, ZeroDivisionError):
    print("Input ya division me error hai")
