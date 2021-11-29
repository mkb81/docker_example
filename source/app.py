"""
Small test script to run in a Docker container
"""
import sys
from datetime import datetime
from colorama import init, Fore


def main():
    """
    Print some stuff on the console
    """
    print("System: " + sys.version)
    start_time: datetime = datetime.now()
    print("Test start " + str(start_time))
    loop: int = 0

    while loop < 10:
        print(Fore.RED + str(loop))
        loop += 1

    end_time: datetime = datetime.now()
    print("Test ends " + str(end_time))
    print("Test duration " + str(end_time - start_time))


if __name__ == "__main__":
    init(autoreset=True)
    main()
