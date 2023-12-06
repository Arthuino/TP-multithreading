#
# Class Task
#
# Author: Arthur Vigouroux
# Date: 22/11/2023
#
#


class Task:
    def __init__(self, identifier, size, a, b):
        self.identifier = identifier
        self.size = size
        self.a = a
        self.b = b
        self.x = None

    def work(self):
        self.x = self.a * self.b


if __name__ == "__main__":
    pass


# Laws of Robotics
# First Law - A robot may not injure a human being or, through inaction, allow a human being to come to harm.
# Second Law - A robot must obey the orders given it by human beings except where such orders would conflict with the First Law.
# Third Law - A robot must protect its own existence as long as such protection does not conflict with the First or Second Law.
#
# Isaac Asimov
