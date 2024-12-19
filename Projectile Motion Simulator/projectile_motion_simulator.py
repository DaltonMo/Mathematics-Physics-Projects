import matplotlib.pyplot as plt
import numpy as np

def projectile_motion(initial_velocity, launch_angle, time_step=0.01):
    """
    Simulates and plots the projectile motion of an object.

    Parameters:
        initial_velocity (float): Initial velocity of the projectile in m/s
        launch_angle (float): Launch angle in degrees
        time_step (float): Time increment for simulation in seconds (default is 0.01)
    """

    # Constants
    g = 9.81 # Acceleration due to gravity (m/s^2)

    # Convert angle to radians
    launch_angle_rad = np.radians(launch_angle)

    # Calculate initial velocity components
    v_x = initial_velocity * np.cos(launch_angle_rad)
    v_y = initial_velocity * np.sin(launch_angle_rad)

    # Time of flight calculation
    time_of_flight = 2 * v_y / g

    # Time points
    t = np.arange(0, time_of_flight + time_step, time_step)

    # Calculate projectile motion
    x = v_x * t # Horizontal distance
    y = v_y * t - 0.5 * g * t**2 # Vertical distance

    # Filter to keep only points where y >= 0
    valid_points = y >= 0
    x = x[valid_points]
    y = y[valid_points]

    # Plot the trajectory
    plt.figure(figsize=(10,6))
    plt.plot(x, y, label=f"Initial Velocity: {initial_velocity} m/s, "
                         f"Angle: {launch_angle}°")
    plt.axhline(0, color='black', linewidth=0.5, linestyle='--') # Ground level

    # Adding labels and title
    plt.title("Projectile Motion", fontsize=16)
    plt.xlabel("Horizontal Distance (m)", fontsize=14)
    plt.ylabel("Vertical Distance (m)", fontsize=14)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend(fontsize=12)

    # Display the plot
    plt.show()

def main():
    """
       Main function to simulate and plot projectile motion based on user inputs.
    """

    print("Welcome to the Projectile Motion Simulator!")

    try:
        # User inputs
        initial_velocity = float(input("Enter the initial velocity (m/s): "))
        launch_angle = float(input("Enter the launch angle (degrees): "))

        # Simulate the plot
        projectile_motion(initial_velocity, launch_angle)
    except ValueError:
        print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    main()