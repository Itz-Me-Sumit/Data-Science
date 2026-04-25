# PART 2: Specific exceptions

try:
    num = int(input("Enter number: "))
    result = 10 / num

except ValueError:
    print("Number dalna tha bhai")

except ZeroDivisionError:
    print("0 se divide nahi hota")

else:
    print("Result:", result)
