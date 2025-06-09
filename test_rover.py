from codecraft_exercises.rover import Rover


def test_rover_initialization():
    rover = Rover(4, 7, 'North')
    assert rover.x == 4
    assert rover.y == 7
    assert rover.direction == 'North'
