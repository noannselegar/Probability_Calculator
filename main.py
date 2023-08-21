from probability import *

hat = Hat(red=6, black=3, blue=1)
print('The probability is', experiment(hat=hat, expected_balls={'red':2, 'black':1, 'blue':1}, num_balls_drawn=4))