import matplotlib.pyplot as plt
import numpy as np

def plot_sine_cosine(amplitude, frequency, phase):
    """
        Plots sine and cosine waves based on user-defined parameters.

        Parameters:
            amplitude (float): Amplitude of the waves
            frequency (float): Frequency of the waves
            phase (float): Phase shift of the sine wave (in radians)
        """

    # Define the range for x values
    x = np.linspace(0, 2 * np.pi, 500)
    sine_wave = amplitude * np.sin(frequency * x + phase)
    cosine_wave = amplitude * np.cos(frequency * x)

    # Plot the waves
    plt.figure(figsize=(10,6))
    plt.plot(x, sine_wave, label=f"Sine Wave: {amplitude}sin({frequency}x + {phase})")
    plt.plot(x, cosine_wave, label=f"Cosine Wave: {amplitude}cos({frequency}x)")
    plt.axhline(0, color='black', linewidth=0.5, linestyle='--') # x-axis
    plt.axvline(0, color='black', linewidth=0.5, linestyle='--')

    # Adding labels and title
    plt.title("Sine and Cosine Waves")
    plt.xlabel("x (radians)", fontsize=14)
    plt.ylabel("Amplitude", fontsize=14)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend(fontsize=12)

    # Display the plot
    plt.show()

def main():
    """
    Main function to input coefficients and calculate roots.
    """
    print("Welcome to the Sine and Cosine Wave Plotter!")

    try:
        # Inputs
        amplitude = float(input("Enter the amplitude of the waves: "))
        frequency = float(input("Enter the frequency of the waves: "))
        phase = float(input("Enter the phase shift (in radians) for the sine wave: "))

        # Calculate roots
        plot_sine_cosine(amplitude, frequency, phase)
    except ValueError:
        print("Invalid input! Please enter numeric values for the coefficients.")


if __name__ == "__main__":
    main()