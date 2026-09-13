first_value = int(input())
second_value = int(input())
third_value = int(input())

packed_tuple = (first_value, second_value, third_value)

first, second, third = packed_tuple

print("packed tuple: ", packed_tuple)
print(f"Unpacked values: first:{first}, Second: {second}, Third: {third}")
"""
Output:
        5
        6
        4
        packed tuple:  (5, 6, 4)
        Unpacked values: first:5, Second: 6, Third: 4
"""