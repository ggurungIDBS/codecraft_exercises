class Rover:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.directions = ["North", "East", "South", "West"]

    def turn_right(self):
        current_index = self.directions.index(self.direction)
        print(current_index)
        self.direction = self.directions[(
            current_index + 1) % len(self.directions)]

    def turn_left(self):
        current_index = self.directions.index(self.direction)
        print(current_index)
        self.direction = self.directions[(
            current_index - 1) % len(self.directions)]
