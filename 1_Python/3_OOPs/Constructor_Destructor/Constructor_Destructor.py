class hello:

    # Constructor
    def __init__(self):
        print("Constructor Called")

    # Destructor
    def __del__(self):
        print("Destructor Called")

obj=hello()

del obj