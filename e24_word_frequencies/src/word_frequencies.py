#!/usr/bin/env python3

def word_frequencies(filename):
    exclude = """!"#$%&'()*,-./:;?@[]_"""
    word_dict = {}
    with open(filename, "r") as file:
        for line in file:
            words = line.split()
            for word in words:
                stripped_word = word.strip(exclude)
                if stripped_word in word_dict:
                    word_dict[stripped_word] += 1
                else:
                    word_dict[stripped_word] = 1
    return word_dict

def main():
    word_dict = word_frequencies("src/alice.txt")
    for key, value in word_dict.items():
        print(f'{key}\t{value}')

if __name__ == "__main__":
    main()
