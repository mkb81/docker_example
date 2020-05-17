"""
Small test script to run in a Docker container
"""


def main():
    """
    Print some stuff on the console
    """
    print("test start")
    a = 0
    while a < 10:
        print(a)
        a += 1

    print("Test end")


if __name__ == "__main__":
    main()
