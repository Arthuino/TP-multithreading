from .queueClient import QueueClient

#
# Do the tasks of the queue
#
# Author : Arthur Vigouroux
# Date : 22/11/2023
#


class Minion(QueueClient):
    def __init__(self) -> None:
        super().__init__()
