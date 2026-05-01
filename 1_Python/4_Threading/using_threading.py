import requests
import time
import threading

url = "https://raw.githubusercontent.com/Itz-Me-Sumit/Data-Science/main/1_Python/2_Exception_Handling/PART3—finally.py"

def download(url, path, thread_name):
    try:
        print(f"[{thread_name}] Starting download...")

        response = requests.get(url, stream=True, timeout=10)
        response.raise_for_status()

        with open(path, "wb") as file:
            for chunk in response.iter_content(8192):
                if chunk:
                    file.write(chunk)

        print(f"[{thread_name}] Finished downloading {path}")

    except Exception as e:
        print(f"[{thread_name}] Error: {e}")


t1 = threading.Thread(target=download, args=(url, "d.py", "Thread-1"))
t2 = threading.Thread(target=download, args=(url, "e.py", "Thread-2"))
t3 = threading.Thread(target=download, args=(url, "f.py", "Thread-3"))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("Main Program Done")