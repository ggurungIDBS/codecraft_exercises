from codecraft_exercises.rover import Rover


def test_rover_initialization():
    rover = Rover(4, 7, 'North')
    assert rover.x == 4
    assert rover.y == 7
    assert rover.direction == 'North'


def test_turn_right_from_north():
    rover = Rover(0, 0, 'North')
    rover.turn_right()
    assert rover.direction == 'East'


def test_turn_right_from_east():
    rover = Rover(0, 0, 'East')
    rover.turn_right()
    assert rover.direction == 'South'


def test_turn_right_from_south():
    rover = Rover(0, 0, 'South')
    rover.turn_right()
    assert rover.direction == 'West'


def test_turn_right_from_west():
    rover = Rover(0, 0, 'West')
    rover.turn_right()
    assert rover.direction == 'North'


def test_turn_left_from_west():
    rover = Rover(0, 0, 'West')
    rover.turn_left()
    assert rover.direction == 'South'


def test_turn_left_from_south():
    rover = Rover(0, 0, 'South')
    rover.turn_left()
    assert rover.direction == 'East'


def test_turn_left_from_east():
    rover = Rover(0, 0, 'East')
    rover.turn_left()
    assert rover.direction == 'North'


def test_turn_left_from_north():
    rover = Rover(0, 0, 'North')
    rover.turn_left()
    assert rover.direction == 'West'
