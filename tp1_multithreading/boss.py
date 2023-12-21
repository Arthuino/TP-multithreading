#
# Add task to the queue
#
# Author : Arthur Vigouroux
# Date : 22/11/2023
#


import numpy as np
from queueClient import QueueClient
from task import Task


class Boss(QueueClient):
    def __init__(self):
        super().__init__()

    def add_task(self, task):
        self.task_queue.put(task)

    def get__and_check_result(self):
        res = self.result_queue.get()
        print("Got result")
        x = res.x
        a = res.a
        b = res.b
        if np.allclose(a @ x, b):
            return x
        else:
            raise Exception("Wrong result")


if __name__ == "__main__":
    boss = Boss()
    size = 100
    a = np.random.rand(size, size)
    b = np.random.rand(size, 1)

    boss.add_task(Task(a, b))
    print("Added task")
    x = boss.get__and_check_result()
    print(x)
