import typing as ty
import sys

def emojify(text : str) -> str:
    output : str = ""
    for i in text:
        output += chr(0x0001f600 + ord(i))
    return output

def main() -> int:
    print(emojify(sys.argv[1]))
    return 0

if __name__ == "__main__":
    if len(sys.argv) == 2:
        exit(main())
    else:
        print("this program require exacly one argument")
        exit(1)
