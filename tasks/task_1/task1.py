

#input from user
numbers = list(map(int, input("Enter integers separated by space: ").split()))

#removing duplicates and sort
unique_sorted = sorted(set(numbers))

maximum = max(numbers)
minimum = min(numbers)
average = sum(numbers) / len(numbers)

#frequency
frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

#dictionary
result = {
    "Maximum Value": maximum,
    "Minimum Value": minimum,
    "Average Value": round(average, 2),
    "Frequency": frequency
}

#output
print("\n--- Final Output ---")

print("Unique Sorted List:")
print(unique_sorted)

print("\nStatistics:")
for key, value in result.items():
    print(f"{key}: {value}")