def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    while right_is_clear() == False:
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear() == True:
        move()
    turn_left()   
while at_goal() != True:
    while front_is_clear() == True:
        move()
        if at_goal() == True:
            break
    while wall_in_front() == True:
        jump()    
    
    


