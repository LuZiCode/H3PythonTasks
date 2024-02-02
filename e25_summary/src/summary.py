#!/usr/bin/env python3

import sys
import statistics

def summary(filename):
    data = []
    try:
        with open(filename, "r") as file:
            for line in file:
                try:
                    data.append(float(line))
                except ValueError:
                    continue
    except FileNotFoundError:
        print(f'File not found {filename}')
    print(data)
    sum_of_data = sum(data)
    average = statistics.mean(data)
    stddev = statistics.stdev(data)
    return (sum_of_data,average,stddev)

def main():
    for cnt in range(1, len(sys.argv)):
        filename = sys.argv[cnt]
        sum_of_data, average, stddev = summary(filename)
        print(f"File: {filename} Sum: {sum_of_data:.6f} Average: {average:.6f} Stddev: {stddev:.6f}")
if __name__ == "__main__":
    main()
