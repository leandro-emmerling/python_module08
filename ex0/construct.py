#!/usr/bin/env python3


from sys import prefix, base_prefix, executable
from os import environ, path
from site import getsitepackages


def check() -> bool:
    """Function to check if Programm runs in venv (True if it runs in venv)"""
    if prefix == base_prefix:
        return False
    return True


if __name__ == "__main__":
    if check() is False:
        print("\nMATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {executable}")
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # on Windows\n")
        print("Then run this program again.")
    else:
        print("\nMATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {executable}")
        print(f"Virtual Environment: "
              f"{path.basename(environ.get('VIRTUAL_ENV'))}")
        print(f"Environment Path: {environ.get('VIRTUAL_ENV')}\n")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")
        print("\nPackage installation path:")
        print(getsitepackages()[0])
