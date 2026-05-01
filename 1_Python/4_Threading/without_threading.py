import requests
import time

url = "https://raw.githubusercontent.com/Itz-Me-Sumit/Data-Science/main/1_Python/2_Exception_Handling/PART3—finally.py"

def download(url , path):
    try:
        response = requests.get(url , stream=True , timeout=10)
        response.raise_for_status()
        with open(path , "wb") as file: # wb => write in binary
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        print("File Downloaded Successfully")
    except Exception as e:
        print(f"Error in downloading {e}")

t1 = time.time()
download(url , "a.py")
download(url , "b.py")
download(url , "c.py")
t2 = time.time()
print(f"Time Taken(seconds) : {t2-t1}")