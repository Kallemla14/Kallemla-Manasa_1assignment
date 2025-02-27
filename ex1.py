print("Welcome to the Python Program!")


    # Getting input from the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
x = int(input("Enter a number for checking conditions: "))

# Arithmetic operators
sum_result = a + b
diff_result = a - b
product_result = a * b
division_result = a / b if b != 0 else "Undefined (division by zero)"
mod_result = a % b if b != 0 else "Undefined (modulo by zero)"
exp_result = a ** b

# Display arithmetic results
print(f"Sum: {sum_result}, Difference: {diff_result}, Product: {product_result}")
print(f"Division: {division_result}, Modulus: {mod_result}, Exponentiation: {exp_result}")

# Comparison operators
if a == b:
    print(f"{a} is equal to {b}")2
    
elif a != b:
    print(f"{a} is not equal to {b}")

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is less than {b}")
else:
    print(f"{a} is equal to {b}")

# Logical operators
if a > 0 and b > 0:
    print("Both numbers are positive.")
elif a < 0 or b < 0:
    print("At least one number is negative.")
else:
    print("Both numbers are zero.")

# Assignment operator
a += 5  # a = a + 5
print(f"After assignment operation, a is now: {a}")

# Bitwise operators
bitwise_and = a & b
bitwise_or = a | b
bitwise_xor = a ^ b

print(f"Bitwise AND: {bitwise_and}, Bitwise OR: {bitwise_or}, Bitwise XOR: {bitwise_xor}")

# Nested if to check the number x
if x != 0:
    if x % 2 == 0:
        print(f"{x} is even.")
    else:
        print(f"{x} is odd.")
else:
    print("The number is zero.")
