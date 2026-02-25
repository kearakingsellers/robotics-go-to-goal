import numpy as np
import matplotlib.pyplot as plt


class DifferentialDriveRobot:
    def __init__(self, x=0.0, y=0.0, theta=0.0):
        # State
        self.x = x
        self.y = y
        self.theta = theta

        # Trajectory storage
        self.x_history = [x]
        self.y_history = [y]

    def normalize_angle(self, angle):
        return np.arctan2(np.sin(angle), np.cos(angle))

    def update(self, v, omega, dt):
        # Kinematic equations
        self.x += v * np.cos(self.theta) * dt
        self.y += v * np.sin(self.theta) * dt
        self.theta += omega * dt
        self.theta = self.normalize_angle(self.theta)

        # Store trajectory
        self.x_history.append(self.x)
        self.y_history.append(self.y)

    def go_to_goal(self, goal_x, goal_y, k=2.0, v=1.0, dt=0.1, tolerance=0.1):
        while True:
            dx = goal_x - self.x
            dy = goal_y - self.y

            distance = np.sqrt(dx**2 + dy**2)
            if distance < tolerance:
                break

            desired_theta = np.arctan2(dy, dx)
            error = self.normalize_angle(desired_theta - self.theta)

            omega = k * error
            self.update(v, omega, dt)


def plot_trajectory(robot, goal_x, goal_y):
    plt.figure()
    plt.plot(robot.x_history, robot.y_history)
    plt.scatter(robot.x_history[0], robot.y_history[0])
    plt.scatter(goal_x, goal_y)
    plt.title("Differential Drive Robot - Go To Goal")
    plt.xlabel("X Position")
    plt.ylabel("Y Position")
    plt.axis("equal")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    robot = DifferentialDriveRobot(0, 0, 0)
    goal_x = 5
    goal_y = 5

    robot.go_to_goal(goal_x, goal_y)
    plot_trajectory(robot, goal_x, goal_y)