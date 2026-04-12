"""
Sorting Alogirthms

Bubble Sort --> O(n^2)--> dompares neigbors, bubbles larges to end to sort
for eg how bubbles in water float up

--> in bubble sort the largest numbers bubbles up to the end of the list; like bubbles 
float to the top of water.

It works by comparing two neighbors at a time and swapping them if they're in the wrong order

"""

def bubble_sort(items):
    n = len(items)
    for i in range(n):
        for j in range(n -1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    return items
    
if __name__ == "__main__":
    numbers = [5, 3, 8, 1, 4]
    print(bubble_sort(numbers))