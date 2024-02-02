#!/usr/bin/env python3

def sum_equation(List):
    sum_value = sum(List)
    if not List:
        return "0 = 0"
    result = " + ".join(str(digit) for digit in List)
    return f"{result} = {sum_value}"

def main():
    print(sum_equation([1,5,7,0]))

if __name__ == "__main__":
    main()
