def larget_and_smallest(nums):
    largest = nums[0]
    smallest = nums[0]
    for num in nums[1:]:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    return largest, smallest // return tuple([largest, smallest])

def main():
    largest, smallest = larget_and_smallest([1, 2, 3, 4, 5])
    print(largest)
    print(smallest)

if __name__ == "__main__":
    main()