"""
Task 4 — Debugging
original code:

numbers = [1, 2, 3, 4, 5] 
for i in range(len(numbers)): 
    numbers.remove(numbers[i]) 
print(numbers)

why bug occures?
-When an element is removed the remaining elements shift left but the loop index 
 keeps increasing.
 This causes some elements to be skipped and leads to an IndexError

"""
#corrected code - using list.pop operation
numbers = [1, 2, 3, 4, 5]

while numbers:
    numbers.pop()

print(numbers)

"""
using pop(), it removes element one at a time from the end and takes time complexity of O(n)
"""