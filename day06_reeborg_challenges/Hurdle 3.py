def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():    
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
def wall():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    

while not at_goal():
    if front_is_clear() :
        move()
    elif wall_in_front() :
        jump()
        


    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
