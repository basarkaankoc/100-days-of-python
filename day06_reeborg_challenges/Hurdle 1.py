def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():    
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

number_of_hurdles = 0

while number_of_hurdles <= 5:
    jump()
    number_of_hurdles += 1

    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
