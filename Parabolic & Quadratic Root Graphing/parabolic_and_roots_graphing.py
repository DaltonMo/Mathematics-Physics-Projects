import matplotlib.pyplot as plt
import numpy as np
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


def plot_parabola_and_roots(a, b, c):
    """
    Plots a parabola and its roots (if real).

    Parameters:
        a (float): Coefficient of x^2
        b (float): Coefficient of x
        c (float): Constant term
    """

    # Define the range for x values
    x = np.linspace(-10, 10, 500)

    # Calculate y values based on the parabola equation
    y = a * x**2 + b * x + c

    # Plot the parabola
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f"y = {a}x² + {b}x + {c}")
    plt.axhline(0, color='black', linewidth=0.5, linestyle='--') # x-axis
    plt.axvline(0, color='black', linewidth=0.5, linestyle='--') # y-axis

    roots = quadratic_roots(a, b, c)
    if isinstance(roots, tuple) and isinstance(roots[0], (int, float)):
        plt.plot(roots[0], 0, 'ko', label=f"Root 1: {roots[0]:.2f}")
        plt.plot(roots[1], 0, 'ko', label=f"Root 2: {roots[1]:.2f}")

    # Adding labels and title
    plt.title("Parabola and Roots", fontsize=16)
    plt.xlabel("x", fontsize=14)
    plt.ylabel('y', fontsize=14)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend(fontsize=12)

    # Display the plot
    plt.show()

def main():
    """
    Main function to input coefficients, calculate roots, and plot the parabola.
    """
    print("Welcome to the Parabolic Equation Graphing Program!")
    print("The equation has the form: y = ax^2 + bx + c")

    try:
        # Input coefficients
        a = float(input("Enter the coefficient a (x^2 term): "))
        b = float(input("Enter the coefficient b (x term): "))
        c = float(input("Enter the constant c: "))

        # Plot parabola and roots
        plot_parabola_and_roots(a, b, c)
    except ValueError:
        print("Invalid input! Please enter numeric values for the coefficients.")

if __name__ == "__main__":
    main()
