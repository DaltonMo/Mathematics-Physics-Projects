import matplotlib.pyplot as plt
import numpy as np

def plot_parabola(a, b, c):
    """
    Plots a parabola based on the equation y = ax^2 + bx + c

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

    # Adding labels and title
    plt.title("Parabola Graph", fontsize=16)
    plt.xlabel("x", fontsize=14)
    plt.ylabel('y', fontsize=14)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend(fontsize=12)

    # Display the plot
    plt.show()

def main():
    """
    Main function to input coefficients and plot the parabola.
    """

    print("Welcome to the Parabolic Equation Graphing Program!")
    print("The equation has the form: y = ax^2 + bx + c")

    try:
        # Input coefficients
        a = float(input("Enter the coefficient a (x^2 term): "))
        b = float(input("Enter the coefficient b (x term): "))
        c = float(input("Enter the constant c: "))

        # Plot the parabola
        plot_parabola(a, b, c)
    except ValueError:
        print("Invalid input! Please enter numeric values for the coefficients.")


if __name__ == "__main__":
    main()