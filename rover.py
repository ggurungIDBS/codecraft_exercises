class Rover:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def turn_right(self):
        directions = ["North", "East", "South", "West"]
        current_index = directions.index(self.direction)
        print(current_index)
        self.direction = directions[(current_index + 1) % len(directions)]
