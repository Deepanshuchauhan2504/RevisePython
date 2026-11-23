def binary_search(array, target):
    low = 0
    high = len(array) - 1
    while (low <= high):
        mid = low + (high - low) // 2
        if (array[mid] == target):
            return mid
        elif (array[mid] < target):
            low = mid + 1
        else:
            high = mid - 1

    return -1

def main():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = int(input("Enter a number to search in array:"))
    index = binary_search(array, target)
    if index == -1:
        print("Target not found")
    else:
        print(f"target element {10} is at index {index}")

if __name__ == "__main__":
    main()