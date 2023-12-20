#
# Queue client
# Author : Arthur Vigouroux
# Date : 22/11/2023
#

from multiprocessing import Queue

from queueManager import QueueManager


class QueueClient:
    task_queue = Queue()
    result_queue = Queue()

    def __init__(self) -> None:
        self.manager = QueueManager(address=("", 50000), authkey=b"abracadabra")
        self.manager.connect()
        self.task_queue = self.manager.get_task_queue()
        self.result_queue = self.manager.get_result_queue()
