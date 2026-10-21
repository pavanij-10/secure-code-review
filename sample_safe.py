
import subprocess
import os

def show_message():
    message = os.environ.get("APP_MESSAGE", "Hello!")
    subprocess.run(
        ["echo", message],
        check=True,
        shell=False
    )

if __name__ == "__main__":
    show_message()
