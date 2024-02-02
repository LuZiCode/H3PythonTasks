#!/usr/bin/env python3


def main():
    for i in range(1, 11):
        triple_value = triple(i)
        square_value = square(i)
        if square_value > triple_value:
            break
        print(f"triple({i})=={triple_value} square({i})=={square_value}")


def triple(number):
    return number*3

def square(number):
    return number*number

if __name__ == "__main__":
    main()
