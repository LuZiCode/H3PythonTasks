#!/usr/bin/env python3

def detect_ranges(lst):
    # First, sort the list to ensure numbers are in ascending order
    sorted_lst = sorted(lst)
    
    # Result list to store numbers and intervals
    result = []
    
    # Start iterating through the sorted list
    i = 0
    while i < len(sorted_lst):
        # Start of a potential range
        start = sorted_lst[i]
        
        # While we have a consecutive sequence, keep incrementing i
        while i + 1 < len(sorted_lst) and sorted_lst[i] + 1 == sorted_lst[i + 1]:
            i += 1
        
        # End of a potential range (one past the end, consistent with Python's range)
        end = sorted_lst[i] + 1
        
        # If start != end - 1, we have a range
        if start != sorted_lst[i]:
            result.append((start, end))
        else:
            # If not a range, just append the number
            result.append(start)
        
        # Move to the next number
        i += 1
    
    return result

def main():
    print(detect_ranges([2,5,4,8,12,6,7,10,13]))

if __name__ == "__main__":
    main()
