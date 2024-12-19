import math


def quadratic_roots(a, b, c):
    """
    Calculate the roots of a quadratic equation: ax^2 + bx + c = 0

    Parameters:
        a (float): Coefficient of x^2
        b (float): Coefficient of x
        c (float): Constant term

    Returns:
        tuple: A tuple containing the roots (real or complex)
    """

    if a == 0:
        return "Not a quadratic equation. 'a' cannot be 0."

    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        # Two distinct real roots
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        # One real root
        root = -b / (2 * a)
        return root, root
    else:
        # Complex roots
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2


def main():
    """
    Main function to input coefficients and calculate roots.
    """
    print("Welcome to the Quadratic Roots Calculator!")
    print("The equation has the form: ax^2 + bx + c = 0")

    try:
        # Input coefficients
        a = float(input("Enter the coefficient a (x^2 term): "))
        b = float(input("Enter the coefficient b (x term): "))
        c = float(input("Enter the constant c: "))

        # Calculate roots
        roots = quadratic_roots(a, b, c)
        print("The roots of the quadratic equation are:", roots)
    except ValueError:
        print("Invalid input! Please enter numeric values for the coefficients.")


if __name__ == "__main__":
    main()