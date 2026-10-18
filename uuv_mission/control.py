class Controller:

    # Initialize the controller with proportional and derivative gains
    def __init__(self):
        self.Kp = 0.15
        self.Kd = 0.6
        self.err_prev = 0

    # Compute the control action based on the reference and current output
    def control(self, reference, y):
        error = reference - y
        action = self.Kp * error + self.Kd * (error - self.err_prev)
        self.err_prev = error
        return action

    # Reset the error to zero for a new control session
    def reset(self):
        self.err_prev = 0
