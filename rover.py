class Rover:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.directions = ["North", "East", "South", "West"]

    def turn_right(self):
        current_index = self.get_current_index()
        print(current_index)
        self.direction = self.directions[(
            current_index + 1) % len(self.directions)]

    def get_current_index(self):
        return self.directions.index(self.direction)

    def turn_left(self):
        current_index = self.get_current_index()
        print(current_index)
        self.direction = self.directions[(
            current_index - 1) % len(self.directions)]

    def move_forward(self):
        if self.direction == 'North':
            self.y += 1
