#
# Do the tasks of the queue
#
# Author : Arthur Vigouroux
# Date : 22/11/2023
#
from queueClient import QueueClient


class Minion(QueueClient):
    def __init__(self) -> None:
        super().__init__()

    def do_tasks(self):
        while True:
            task = self.task_queue.get()
            if task is None:
                break
            x = task.work()
            print(x)
            self.result_queue.put(x)


if __name__ == "__main__":
    minion = Minion()
    minion.do_tasks()
