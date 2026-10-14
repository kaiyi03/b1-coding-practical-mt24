class Controller:
    def __init__(self):
        self.Kp = 0.15
        self.Kd = 0.6
        self.err_prev = 0

    def control(self, reference, y):
        error = + reference - y
        action = self.Kp * error + self.Kd * (error - self.err_prev)
        self.err_prev = error
        return action
