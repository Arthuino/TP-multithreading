#
# Manager for the queue of tasks to be executed by the minions
# Inherit from multiprocessing.BaseManager
# Author : Arthur Vigouroux
# Date : 22/11/2023
#
# address = ('', 50000)
# authkey = b'abracadabra'

import multiprocessing as mp
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):  # type: ignore
    def __init__(self, address, authkey):
        super().__init__()
        self.task_queue = mp.Queue()
        self.result_queue = mp.Queue()
        self.register("get_task_queue", callable=lambda: self.task_queue)
        # self.register('get_result_queue', callable=lambda: self.result_queue)
        BaseManager(address=("", 50000), authkey=b"abracadabra")

    def launch_server(self):
        server = self.get_server()
        server.serve_forever()


if __name__ == "__main__":
    manager = QueueManager(address=("", 50000), authkey=b"abracadabra")
    print("Launch Manager")
    manager.launch_server()
