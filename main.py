import typing as ty
import sys

def emojify(text : str) -> str:
    return text

def main() -> int:
    print(emojify(sys.argv[1]))
    return 0

if __name__ == "__main__":
    if len(sys.argv) == 2:
        exit(main())
    else:
        print("this program require exacly one argument")
        exit(1)
