arr = [4,3,2,4,4,3,1,6,7,4,1,3,8,4,6,1]

unique_numbers = [] # preserve the order of first occurence
seen = set()

for number in arr:
    if number not in seen:
        unique_numbers.append(number)
        seen.add(number)

print(unique_numbers)

sorted_unique_numbers = sorted(unique_numbers)
print(sorted_unique_numbers)