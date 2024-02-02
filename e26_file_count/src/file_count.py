#!/usr/bin/env python3

import sys

def file_count(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            line_count = content.count('\n') + 1
            word_count = len(content.split())
            char_count = len(content)
            return line_count, word_count, char_count
    except FileNotFoundError:
        print("File not found", FileNotFoundError)

def main():
    # print(f'Line\tWord\tCharacter\tFilename')
    for cnt in range(1, len(sys.argv)):
        filename = sys.argv[cnt]
        line_count, word_count, char_count = file_count(filename)
        print(f'{line_count}\t{word_count}\t{char_count}\t{filename}')

if __name__ == "__main__":
    main()