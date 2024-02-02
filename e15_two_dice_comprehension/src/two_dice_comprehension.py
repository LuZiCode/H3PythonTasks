#!/usr/bin/env python3

def main():
    matching_pairs = [(dice1, dice2) for dice1 in range(1, 7) for dice2 in range(1, 7) if dice1 + dice2 == 5]
    for pair in matching_pairs:
        print(pair)

if __name__ == "__main__":
    main()
