#!/usr/bin/env python3

def main():
    for dice1 in range(1, 7):
        # print(f"dice1 {dice1}")
        for dice2 in range(1, 7):
            # print(f"dice2 {dice2}")
            if dice1 + dice2 == 5:
                print(f"({dice1}, {dice2})")

if __name__ == "__main__":
    main()
