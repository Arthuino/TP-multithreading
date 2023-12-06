#
# Class Task
#
# Author: Arthur Vigouroux
# Date: 22/11/2023
#
#
import numpy as np


class Task:
    def __init__(self, identifier, size):
        self.identifier = identifier
        self.size = size
        # create random matrix a
        self.a = np.random.rand(size, size)
        # create random vector b
        self.b = np.random.rand(size, 1)
        self.x = None

    def work(self):
        self.x = np.linalg.solve(self.a, self.b)


if __name__ == "__main__":
    print("identifier: 1, size: 10")
    t = Task(1, 10)
    print("matrix a : \n", t.a)
    print("vector b : \n", t.b)
    t.work()
    print("vector x : \n", t.x)


# Laws of Robotics
# First Law - A robot may not injure a human being or, through inaction, allow a human being to come to harm.
# Second Law - A robot must obey the orders given it by human beings except where such orders would conflict with the First Law.
# Third Law - A robot must protect its own existence as long as such protection does not conflict with the First or Second Law.
#
# Isaac Asimov
