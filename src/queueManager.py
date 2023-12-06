#
# Manager for the queue of tasks to be executed by the minions
# Inherit from multiprocessing.BaseManager
# Author : Arthur Vigouroux
# Date : 22/11/2023
#

import multiprocessing


class QueueManager(multiprocessing.managers.BaseManager):
    task_queue = None
    result_queue = None

    def __init__(self):
        super().__init__()

    def add_task(self, task):
        pass

    def get_result(self):
        pass
