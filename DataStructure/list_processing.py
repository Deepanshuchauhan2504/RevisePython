
def analyze_numbers(numbers):

    # Handle an empty list
    if not numbers:
        print("The list is empty.")
        return

    # Basic calculations
    minimum = min(numbers)
    maximum = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)

    # Separate even and odd numbers
    even_numbers = []
    odd_numbers = []

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

    # Find second-largest DISTINCT value
    unique_numbers = set(numbers)

    if len(unique_numbers) >= 2:
        sorted_numbers = sorted(unique_numbers, reverse=True)
        second_largest = sorted_numbers[1]
    else:
        second_largest = None

    # Display report
    print("----- NUMBER REPORT -----")
    print("Minimum:", minimum)
    print("Maximum:", maximum)
    print("Sum:", total)
    print("Average:", average)
    print("Even numbers:", even_numbers)
    print("Odd numbers:", odd_numbers)

    if second_largest is not None:
        print("Second-largest distinct value:", second_largest)
    else:
        print("Second-largest distinct value: Not available")


# Example
numbers = [10, 5, 20, 8, 20, 3, 10, 7]

analyze_numbers(numbers)
