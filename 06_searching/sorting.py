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
        for j in range(n - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    return items


def selection_sort(items):
    """Find smallest item, put it at front, repeat. O(n^2)"""
    n = len(items)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if items[j] < items[min_idx]:
                min_idx = j
        # swap AFTER finding min
        items[i], items[min_idx] = items[min_idx], items[i]
    return items


def insertion_sort(items):
    """Pick each item, insert it in correct position. O(n^2)"""
    for i in range(1, len(items)):
        current = items[i]
        j = i - 1
        while j >= 0 and items[j] > current:
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = current
    return items

def merge_sort(items):
    """Split in half, sort each half, merge-->O(n log n)"""
    if len(items) <= 1:
        return items
    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])
    return merge(left, right)

def merge(left, right):
    """Merge two sorted lists into one."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

if __name__ == "__main__":
    print(bubble_sort([5, 3, 8, 1, 4]))
    print(selection_sort([5, 3, 8, 1, 4]))
    print(insertion_sort([5, 3, 8, 1, 4]))
    print(merge_sort([5, 3, 8, 1, 4]))
