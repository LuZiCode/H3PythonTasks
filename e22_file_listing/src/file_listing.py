#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    result = []
    # Definer dit regulære udtryk
    pattern = r'(\d+)\s+([A-Z][a-z]{2})\s+(\d+)\s+(\d{2}):(\d{2})\s+(.+)'
    
    with open(filename, "r") as file:
        for line in file:
            match = re.search(pattern, line)
            if match:
                size = int(match.group(1))
                month = match.group(2)
                day = int(match.group(3))
                hour = int(match.group(4))
                minute = int(match.group(5))
                filename = match.group(6)
                result.append((size, month, day, hour, minute, filename))
                
    return result

def main():
    result = file_listing()
    for item in result:
        print(item)

if __name__ == "__main__":
    main()
