# Do not modify these lines
__winc_id__ = "78029e0e504a49e5b16482a7a23af58c"
__human_name__ = "modules"

# Add your code after this line

from os import name
from Zen import Zen_of_Py

Zen_of_Py()

# ___________________________________________________________


def wait(seconds: int):
    import time

    time.sleep(seconds)
    return


# ___________________________________________________________

import math


def my_sin(number: float):
    return math.sin(number)


# ___________________________________________________________


def iso_now():
    from datetime import datetime

    todaysdate = datetime.now().strftime("%Y-%m-%dT%H:%M")
    return todaysdate


# ___________________________________________________________
def platform():
    import sys

    os = sys.platform
    return os


# ___________________________________________________________


def supergreeting_wrapper(name: str):
    from greet import supergreeting

    x = supergreeting(name)
    return x


# ___________________________________________________________
def main():
    wait(1)
    print(my_sin(4))
    print(iso_now())
    print(platform())
    print(supergreeting_wrapper("Klaas"))


if __name__ == "__main__":
    main()
