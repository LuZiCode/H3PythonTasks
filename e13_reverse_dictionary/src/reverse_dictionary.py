#!/usr/bin/env python3

def reverse_dictionary(d):
    reversed_d = {}
    for key, values in d.items():
        for value in values:
            if value not in reversed_d:
                reversed_d[value] = [key]
            else:
                reversed_d[value].append(key)
    return reversed_d
                
        
    return {}

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))

if __name__ == "__main__":
    main()
