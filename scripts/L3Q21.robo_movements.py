'''
Question A robot moves in a plane starting from the original point (0,0). 
The robot can move toward UP, DOWN, LEFT and RIGHT 
with a given steps. 
The trace of robot movement is shown as the following: 
UP 5 DOWN 3 LEFT 3 RIGHT 2­ 
The numbers after the direction are steps. 
Please write a program to compute the distance from current position 
after a sequence of movement and original point. 
If the distance is a float, then just print the nearest integer. 
Example: If the following tuples are given as input to the program: 
UP 5 DOWN 3 LEFT 3 RIGHT 2 
Then, the output of the program should be: 2
'''

'''
EXAMPLE broken down:
Consider x-axis and y-axis:
(0,0) UP 5 (0,5)
(0,5) DOWN 3 (0,2)
(0,2) LEFT 3 (-3,2)
(-3,2) RIGHT 2 (-1,2)

Distance from initial (round(sqrt(i*i+j*j))) = 2
'''
import math
def roboplay(steps):
    ''' Steps of robot'''
    steps = steps.split(' ')
    x_axis = 0
    y_axis = 0
    for i, step in enumerate(steps):
        if step == 'UP':
            y_axis += int(steps[i+1])
            print(x_axis, y_axis, sep = ',')
        elif step  == 'DOWN':
            y_axis -= int(steps[i+1])
            print(x_axis, y_axis, sep = ',')
        elif step == 'RIGHT':
            x_axis += int(steps[i+1])
            print(x_axis, y_axis, sep = ',')
        elif step == 'LEFT':
            x_axis -= int(steps[i+1])
            print(x_axis, y_axis, sep = ',')
    
    dist = round(math.sqrt(x_axis*x_axis + y_axis*y_axis))
    return f'Distance travelled by our robot is : {dist}'

if __name__=='__main__':
    steps = input('Enter the steps for our robo game: ')
    print(roboplay(steps))
