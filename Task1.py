import math

# Weather modeling using quadratic solution in stages


# Stage 1: Hard-coded variables
print("Stage 1: Hard-coded variables")
a, b, c = 1, -3, 2  # Example coefficients
discriminant = b**2 - 4*a*c
if discriminant >= 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Roots: {root1}, {root2}")
else:
    print("No real roots.")

# Stage 2: Keyboard input
print("\nStage 2: Keyboard input")
try:
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        print(f"Roots: {root1}, {root2}")
    else:
        print("No real roots.")
except Exception as e:
    print("Invalid input.", e)

# Stage 3: Read from a file (single set of input)
print("\nStage 3: Read from file (single set)")
try:
    with open("quadratic_input.txt") as f:
        line = f.readline()
        a, b, c = map(float, line.strip().split())
        discriminant = b**2 - 4*a*c
        if discriminant >= 0:
            root1 = (-b + math.sqrt(discriminant)) / (2*a)
            root2 = (-b - math.sqrt(discriminant)) / (2*a)
            print(f"Roots: {root1}, {root2}")
        else:
            print("No real roots.")
except Exception as e:
    print("Error reading file.", e)

# Stage 4: Read from a file (multiple sets of inputs)
print("\nStage 4: Read from file (multiple sets)")
try:
    with open("quadratic_input.txt") as f:
        for idx, line in enumerate(f, 1):
            try:
                a, b, c = map(float, line.strip().split())
                discriminant = b**2 - 4*a*c
                if discriminant >= 0:
                    root1 = (-b + math.sqrt(discriminant)) / (2*a)
                    root2 = (-b - math.sqrt(discriminant)) / (2*a)
                    print(f"Set {idx}: Roots: {root1}, {root2}")
                else:
                    print(f"Set {idx}: No real roots.")
            except Exception as e:
                print(f"Set {idx}: Invalid input.", e)
except Exception as e:
    print("Error reading file.", e)