#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    pattern = r'\s*(\d+)\s+(\d+)\s+(\d+)\s+(.+)'
    result = []
    with open(filename, "r") as file:
        next(file)
        for line in file:
            match = re.match(pattern, line)
            if match:
                red, green, blue, name = match.groups()
                string = '{}\t{}\t{}\t{}'.format(red, green, blue, name)
                result.append(string)
    return result


def main():
    result = red_green_blue()
    for item in result:
        print(item)    

if __name__ == "__main__":
    main()
