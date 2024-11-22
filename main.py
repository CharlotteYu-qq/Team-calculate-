import addition
import subtraction
import multiplication
import squareroot

print("Using addition")
x = addition.add_two_numbers(1, 2)
print("1 + 2 = " + str(x))

print("Using subtraction")
x = subtraction.subtract_two_numbers(1, 2)
print("1 - 2 = " + str(x))

print("Using multiply_two_numbers")
x = multiplication.multiply_two_numbers(1, 2)
print("1 * 2 = " + str(x))

print("Using calculate_square_root")
x = squareroot.calculate_square_root(2)
print("square root of 2 = " + str(x))