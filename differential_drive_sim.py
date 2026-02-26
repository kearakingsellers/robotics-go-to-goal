import numpy as np
import matplotlib.pyplot as plt

def simulate(k):
    dt = 0.1
    x, y, theta = 0.0, 0.0, 0.0
    goal_x, goal_y = 5.0, 5.0

    trajectory_x = []
    trajectory_y = []

    for _ in range(300):

        dx = goal_x - x
        dy = goal_y - y
        distance = np.sqrt(dx**2 + dy**2)

        if distance < 0.1:
            break

        desired_theta = np.arctan2(dy, dx)

        # Angle error
        angle_error = desired_theta - theta

        # Normalize angle to [-pi, pi]
        angle_error = np.arctan2(np.sin(angle_error), np.cos(angle_error))

        # Proportional controller
        v = k * distance
        w = k * angle_error

        # Robot motion update
        x += v * np.cos(theta) * dt
        y += v * np.sin(theta) * dt
        theta += w * dt

        trajectory_x.append(x)
        trajectory_y.append(y)

    return trajectory_x, trajectory_y


# ===============================
# Run simulations for different gains
# ===============================

gains = [0.5, 1.0, 2.0]

plt.figure()

for k in gains:
    tx, ty = simulate(k)
    plt.plot(tx, ty, label=f"k = {k}")

# Plot goal point
plt.scatter(5, 5)
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.title("Go-To-Goal with Different Gains")
plt.legend()
plt.grid()

# Save image
plt.savefig("gain_comparison.png")

plt.show()