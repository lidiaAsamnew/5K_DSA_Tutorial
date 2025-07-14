def xor_swap(a: int, b: int) -> tuple[int, int]:
    a ^= b
    b ^= a
    a ^= b
    return a, b

# Usage:
x, y = 5, 9
x, y = xor_swap(x, y)
print(x, y)  # Output: 9 5
