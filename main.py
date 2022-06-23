from module.option import command
from module.core import scan, print_test

def main():
    url = command()
    result = scan(url)
    print_test()
    print(result)

if __name__ == "__main__":
    main()