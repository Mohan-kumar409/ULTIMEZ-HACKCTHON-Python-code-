def pizz_party(x):
    large_pizzas = x // 8
    x %= 8
    medium_pizzas = x // 6
    x %= 6
    regular_pizzas = x // 4
    x %=4
    small_pizzas = x // 1
    x %= 1
    total_slices = (large_pizzas * 8) + (medium_pizzas * 6) + (regular_pizzas * 4) + (small_pizzas * 1)
    return large_pizzas, medium_pizzas, regular_pizzas, small_pizzas, total_slices

x = 19
large, medium, regular, small, total_slices = pizz_party(x)
print(f"If there are {x} individuals:")
print(f"1. we will have {large} Large pizza")
print(f"2. we will have {medium} Medium pizza")
print(f"3. we will have {regular} Regular pizza")
print(f"4. we will have {small} Small pizza")
print(f"Total slices needed: {total_slices}")
