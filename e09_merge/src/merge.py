#!/usr/bin/env python3

def merge(L1, L2):
    L = []
    i, j = 0, 0

    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            L.append(L1[i])
            i += 1
        else:
            L.append(L2[j])
            j += 1
    
    while i < len(L1):
        L.append(L1[i])
        i += 1
    while j < len(L2):
        L.append(L2[j])
        j += 1

    return L

def main():
    L1 = [1, 3, 5, 7]
    L2 = [2, 4, 6, 8]
    print("Merged list:", merge(L1, L2))

    L1 = [1, 2, 5, 10]
    L2 = [3, 4, 7, 8]
    print("Merged list:", merge(L1, L2))

    L1 = []
    L2 = [1, 2, 3]
    print("Merged list:", merge(L1, L2))
    
    
if __name__ == "__main__":
    main()
