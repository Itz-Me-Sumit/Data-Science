# PART 6: raise keyword

def check_age(age):
    if age < 18:
        raise Exception("Underage hai")
    print("Allowed")

try:
    check_age(15)

except Exception as e:
    print("Error:", e)