#!/usr/bin/env python3

def positive_list(full_list):
    return list(filter(lambda x: x > 0, full_list))

def main():
    print(positive_list([2, -2, 0, 1, -7]))

if __name__ == "__main__":
    main()
