#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    # Kvadratiske ligninger er af formen: ax² + bx + c = 0
    # a, b og c er kendte værdier. a må ikke være 0.

    # Diskriminanten er en særlig værdi beregnet ud fra koefficienterne
    # i den kvadratiske ligning (a, b og c). Den er givet ved formelen: b² - 4ac.
    # Diskriminanten fortæller os, om rødderne er reelle eller komplekse tal,
    # og om de er forskellige eller ens.
    d = b**2 - 4*a*c

    # Hvis diskriminanten er negativ, har vores kvadratiske ligning komplekse rødder,
    # hvilket ikke er dækket i grundlæggende matematik, så i dette tilfælde returnerer vi en besked.
    if d < 0:
        return "Komplekse rødder"

    # Hvis diskriminanten ikke er negativ, fortsætter vi med at beregne de to rødder.
    # Den kvadratiske formel er: x = (-b ± sqrt(d)) / (2a)
    # Denne formel beregner de to værdier af x, der gør ax² + bx + c = 0 sandt.

    # Beregn den første rod: x = (-b + sqrt(d)) / (2a)
    # Dette er "plus" delen af "±" i formelen.
    x1 = (-b + math.sqrt(d)) / (2 * a)

    # Beregn den anden rod: x = (-b - sqrt(d)) / (2a)
    # Dette er "minus" delen af "±" i formelen.
    x2 = (-b - math.sqrt(d)) / (2 * a)

    # Returner begge rødder som et tupel (et par af værdier).
    return (x1, x2)


def main():
    print(solve_quadratic(1, -3, 2))  # Udskriver rødderne af ligningen x² - 3x + 2 = 0
    print(solve_quadratic(1, 2, 1))   # Udskriver rødderne af ligningen x² + 2x + 1 = 0

if __name__ == "__main__":
    main()
