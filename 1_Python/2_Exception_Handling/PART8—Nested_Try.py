# PART 9: Nested try

try:
    try:
        num = int(input("Enter number: "))
        print(10 / num)
    except ZeroDivisionError:
        print("Inner: 0 se divide nahi hota")

except ValueError:
    print("Outer: number input hai")