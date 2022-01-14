import imp
from multiprocessing.connection import answer_challenge
from urllib import request, response
from bs4 import BeautifulSoup as bs
import requests
# --------------------------------------------------------
from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
from time import sleep

Welcome_message = """

------------------------------------------------------------
|             Welcome to Geek Download Manager!            |
|                      Release 1.0                         | 
|                                                          |
|                      Continue(1)                         |
|                        Quit(2)                           |
| This project is open-source! You can visit my repository |
| ---> https://github.com/Rootbruh/geek-download-manager   |
------------------------------------------------------------
"""

print(Welcome_message)
answer = input(">>> ")

if answer == "1":

    print("Please enter the required parameters to use this program.")

    url = input("Download address of the file you will download: ")
    file_type = input("File extension of the file you will download: ")


    def soup(url):
        return bs(requests.get(url).text, 'html.parser')


    for link in soup(url).find_all('a'):
        file_link = link.get('href')

        if file_type in file_link:
            file_name = file_link.split('/')[-1]


            with open(file_name, 'wb') as file:
                response = requests.get(file_link)
                file.write(response.content)
    if bool(file_name) == True:

        # Loading animation starting here
        class Loader:
            def __init__(self, desc="Loading...", end="Done!", timeout=0.1):
                """
                A loader-like context manager

                Args:
                    desc (str, optional): The loader's description. Defaults to "Loading...".
                    end (str, optional): Final print. Defaults to "Done!".
                    timeout (float, optional): Sleep time between prints. Defaults to 0.1.
                """
                self.desc = desc
                self.end = end
                self.timeout = timeout

                self._thread = Thread(target=self._animate, daemon=True)
                self.steps = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
                self.done = False

            def start(self):
                self._thread.start()
                return self

            def _animate(self):
                for c in cycle(self.steps):
                    if self.done:
                        break
                    print(f"\r{self.desc} {c}", flush=True, end="")
                    sleep(self.timeout)

            def __enter__(self):
                self.start()

            def stop(self):
                self.done = True
                cols = get_terminal_size((80, 20)).columns
                print("\r" + " " * cols, end="", flush=True)
                print(f"\r{self.end}", flush=True)

            def __exit__(self, exc_type, exc_value, tb):
                # handle exceptions with those variables ^
                self.stop()


        if __name__ == "__main__":
            with Loader("Downloading..."):
                for i in range(10):
                    sleep(0.25)

            loader = Loader("Not long now...", "That was fast!", 0.05).start()
            for i in range(10):
                sleep(0.25)
            loader.stop()
        # Loading animation finished here


elif answer == "2":
    print("Exiting...See you later.")

else:
    print("Wrong command.")
