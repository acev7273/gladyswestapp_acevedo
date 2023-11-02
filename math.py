import math

class Location:
    def __init__(self):
        self.current_position = None
        self.destination_position = None

    def set_current_position(self, x, y):
        if self.is_valid_position(x, y):
            self.current_position = (x, y)
        else:
            print("Invalid position. (x, y) values must be integers between 0 and 99.")

    def set_destination_position(self, x, y):
        if self.is_valid_position(x, y):
            self.destination_position = (x, y)
        else:
            print("Invalid position. (x, y) values must be integers between 0 and 99.")

    def calculate_distance(self):
        if self.current_position is None or self.destination_position is None:
            return "Current and destination positions must be set."
        else:
            x1, y1 = self.current_position
            x2, y2 = self.destination_position
            distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            return f"Distance: {distance:.2f}"

    def is_valid_position(self, x, y):
        return 0 <= x <= 99 and 0 <= y <= 99 and x.is_integer() and y.is_integer()


