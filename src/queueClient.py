#
# Queue client
# Author : Arthur Vigouroux
# Date : 22/11/2023
#

from queueManager import QueueManager


class QueueClient:
    def __init__(self) -> None:
        self.manager = QueueManager(address=("", 50000), authkey=b"abracadabra")
        self.manager.connect()
        self.task_queue = self.manager.get_task_queue()  # type: ignore
        self.result_queue = self.manager.get_result_queue()  # type: ignore
