#
# Manager for the queue of tasks to be executed by the minions
# Inherit from multiprocessing.BaseManager
# Author : Arthur Vigouroux
# Date : 22/11/2023
#
# address = ('', 50000)
# authkey = b'abracadabra'

from multiprocessing import Queue
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    def __init__(self, address, authkey):
        super().__init__(address=address, authkey=authkey)
        self.task_queue = Queue()
        self.result_queue = Queue()
        self.register("get_task_queue", callable=lambda: self.task_queue)
        self.register("get_result_queue", callable=lambda: self.result_queue)

    def launch_server(self):
        server = self.get_server()
        server.serve_forever()

    def get_task_queue(self) -> Queue:
        return self.task_queue

    def get_result_queue(self) -> Queue:
        return self.result_queue


if __name__ == "__main__":
    manager = QueueManager(address=("", 50000), authkey=b"abracadabra")
    print("Launch Manager")
    manager.launch_server()
