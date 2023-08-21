import random
import copy

class Hat():
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.contents = [k for k, v in self.kwargs.items() for i in range(v)]

    def draw(self, balls):
        randomBalls = list()
        contents = list(self.contents)
        if balls < len(contents):
            for _ in range(balls):
                r = random.randint(-len(contents), 0)
                randomBalls.append(contents.pop(r))
            return randomBalls
        else:
            return self.contents

def experiment(hat=Hat(), expected_balls={}, num_balls_drawn=0, num_experiments=2000):
    z = 0
    for x in range(num_experiments):
        A = hat.draw(num_balls_drawn)
        B = [k for k, v in expected_balls.items() for i in range(v)]
        if all(elem in A for elem in B):
            z += 1
    return f'{z/num_experiments*100:.2f}%'