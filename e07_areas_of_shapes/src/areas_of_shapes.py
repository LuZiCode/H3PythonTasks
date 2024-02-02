#!/usr/bin/env python3

import math


def main():
    while True:
        shape = input("Choose a shape: (triangle, rectangle, circle): ")
        if shape in ["triangle", "rectangle", "circle"]:
            shape_calculate = shapeCalculate(shape)
            print(f"The area is {shape_calculate:.6f}")
        elif shape == "":
            break
        else:
            print("Unknown shape!")

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid Input")

def shapeCalculate(shape):
    if shape == "triangle":
        base = get_float("Give base of triangle: ")
        height = get_float("Give height of triangle: ")
        area = (base * height) / 2
    elif shape == "rectangle":
        width = get_float("Give width of the rectangle: ")
        height = get_float("Give height of the rectangle: ")
        area = width * height
    elif shape == "circle":
        radius = get_float("Give radius of the circle: ")
        area = math.pi * radius ** 2
    return area

if __name__ == "__main__":
    main()
