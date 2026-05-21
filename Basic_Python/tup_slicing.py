
# Creating a tuple
numbers = (10, 20, 30, 40, 50, 60, 70)

# 1. Slice from index 1 to 4 (index 4 not included)
print(numbers[1:4])   # Output: (20, 30, 40)

# 2. Slice from beginning to index 3
print(numbers[:3])    # Output: (10, 20, 30)

# 3. Slice from index 2 to end
print(numbers[2:])    # Output: (30, 40, 50, 60, 70)

# 4. Slice the whole tuple
print(numbers[:])     # Output: (10, 20, 30, 40, 50, 60, 70)

# 5. Negative slicing
print(numbers[-4:-1]) # Output: (40, 50, 60)

# 6. Slice with a step value
print(numbers[::2])   # Output: (10, 30, 50, 70)

# 7. Reverse the tuple
print(numbers[::-1])  # Output: (70, 60, 50, 40, 30, 20, 10)