import nlpcloud


class NLPapp:

    def __init__(self):
        self.__database = {}
        self.__authMenu()

    # ---------------- AUTH MENU ----------------
    def __authMenu(self):
        while True:
            try:
                option = int(input("""
Hi, How would you like to Proceed?
1) Register
2) Login
3) Exit
Enter choice: """))

                if option == 1:
                    self.__register()
                elif option == 2:
                    self.__login()
                elif option == 3:
                    print("Goodbye 👋")
                    break
                else:
                    print("Invalid Input")
            except:
                print("Please enter a valid number!")

    # ---------------- MODEL SELECTION ----------------
    def __modelSelection(self):
        while True:
            try:
                model = int(input("""
Choose Your Model:
1) Name Entity Extraction
2) Language Detection
3) Sentiment Analysis
4) Logout
Enter choice: """))

                if model == 1:
                    self.__NER()
                elif model == 2:
                    self.__languageDetection()
                elif model == 3:
                    self.__sentimentAnalysis()
                elif model == 4:
                    print("Logged out successfully\n")
                    break
                else:
                    print("Invalid Input")
            except:
                print("Please enter a valid number!")

    # ---------------- REGISTER ----------------
    def __register(self):
        name = input("Name: ")
        email = input("Email: ")
        password = input("Password: ")

        if email in self.__database:
            print("Email already registered!")
        else:
            self.__database[email] = [name, password]
            print("Registration Successful ✅")

    # ---------------- LOGIN ----------------
    def __login(self):
        email = input("Email: ")
        password = input("Password: ")

        if email in self.__database:
            if password == self.__database[email][1]:
                print(f"Welcome {self.__database[email][0]} 🎉")
                self.__modelSelection()
            else:
                print("Invalid Password ❌")
        else:
            print("Invalid Email! Please register first.")

    # ---------------- NER ----------------
    def __NER(self):
        try:
            para = input("Enter The Paragraph: ")
            search = input("What You Would like to search: ")

            client = nlpcloud.Client(
                "gpt-oss-120b",
                "f9c1cf3887f9cdd0efb75d2b6bc8514118498117",
                gpu=True
            )

            response = client.entities(para, searched_entity=search)
            print("\nResult:", response)

        except Exception as e:
            print("Error aaya bhai:", e)

    # ---------------- LANGUAGE DETECTION ----------------
    def __languageDetection(self):
        try:
            text = input("Enter Text: ")

            client = nlpcloud.Client(
                "python-langdetect",
                "f9c1cf3887f9cdd0efb75d2b6bc8514118498117",
                gpu=False
            )

            res = client.lang_detection(text)
            print("\nDetected Language:", res)

        except Exception as e:
            print("Error aaya bhai:", e)

    # ---------------- SENTIMENT ----------------
    def __sentimentAnalysis(self):
        try:
            text = input("What's in your mind: ")

            client = nlpcloud.Client(
                "gpt-oss-120b",
                "f9c1cf3887f9cdd0efb75d2b6bc8514118498117",
                gpu=True
            )

            res = client.sentiment(text, target="NLP Cloud")
            print("\nSentiment:", res)

        except Exception as e:
            print("Error aaya bhai:", e)


# ---------------- RUN APP ----------------
if __name__ == "__main__":
    NLP = NLPapp()