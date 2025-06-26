strings = ["a", "b", "c"]
integers = [1, 2, 3]

strings.extend(integers)
print(strings)  # ['a', 'b', 'c', 1, 2, 3]

floats = [1.1, 2.2, 3.3]
strings.extend(floats)
print(strings)  # ['a', 'b', 'c', 1, 2, 3, 1.1, 2.2, 3.3]
