#
# Add task to the queue
#
# Author : Arthur Vigouroux
# Date : 22/11/2023
#


from queueClient import QueueClient
from task import Task


class Boss(QueueClient):
    def __init__(self):
        super().__init__()

    def add_task(self, task):
        self.task_queue.put(task)


if __name__ == "__main__":
    boss = Boss()
    boss.add_task(Task(1, 5))
