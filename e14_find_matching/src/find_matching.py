#!/usr/bin/env python3

def find_matching(L, pattern):
    matching = []
    for index, value in enumerate(L):
        print("index", index)
        print("value", value)
        if pattern in value:
            matching.append(index)
    return matching

def main():
    print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))

if __name__ == "__main__":
    main()
