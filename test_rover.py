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


def test_move_forward_north():
    rover = Rover(0, 0, 'North')
    rover.move_forward()
    assert rover.x == 0
    assert rover.y == 1
    assert rover.direction == 'North'


def test_movee_forward_east():
    rover = Rover(1, 5, 'East')
    rover.move_forward()
    assert rover.x == 2
    assert rover.y == 5
    assert rover.direction == 'East'


def test_movee_forward_south():
    rover = Rover(4, 5, 'South')
    rover.move_forward()
    assert rover.x == 4
    assert rover.y == 4
    assert rover.direction == 'South'


def test_movee_forward_west():
    rover = Rover(7, 5, 'West')
    rover.move_forward()
    assert rover.x == 6
    assert rover.y == 5
    assert rover.direction == 'West'


def test_move_backward_north():
    rover = Rover(5, 5, "North")
    rover.move_backward()
    assert rover.x == 5
    assert rover.y == 4
    assert rover.direction == 'North'


def test_move_backward_east():
    rover = Rover(7, 9, "East")
    rover.move_backward()
    assert rover.x == 6
    assert rover.y == 9
    assert rover.direction == 'East'


def test_move_backward_south():
    rover = Rover(4, 3, "South")
    rover.move_backward()
    assert rover.x == 4
    assert rover.y == 4
    assert rover.direction == 'South'


def test_move_backward_west():
    rover = Rover(5, 5, "West")
    rover.move_backward()
    assert rover.x == 6
    assert rover.y == 5
    assert rover.direction == 'West'
