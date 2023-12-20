#
# Class Task
#
# Author: Arthur Vigouroux
# Date: 22/11/2023
#
#
import json

import numpy as np


class Task:
    def __init__(self, a_, b_, identifier=1, x_=None):
        self.identifier = identifier

        self.a = a_
        self.b = b_

        self.x = x_

    def work(self):
        self.x = np.linalg.solve(self.a, self.b)
        return self.x

    def to_json(self) -> str:
        """
        create a json string from the task
        Have to be a custom json encoder to serialize numpy array
        """

        class TaskEncoder(json.JSONEncoder):
            def default(self, obj):
                if isinstance(obj, np.ndarray):
                    return obj.tolist()
                return json.JSONEncoder.default(self, obj)

        return TaskEncoder().encode(self.__dict__)

    @classmethod
    def from_json(cls, text: str):
        data = json.loads(text)
        return cls(
            np.array(data["a"]),
            np.array(data["b"]),
            data["identifier"],
            np.array(data["x"]),
        )

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Task):
            return False
        else:
            return np.array_equal(self.a, __value.a) and np.array_equal(self.b, __value.b) and np.array_equal(self.x, __value.x)  # type: ignore

    def __str__(self) -> str:
        return str(
            "Task "
            + str(self.identifier)
            + " : \n"
            + "a : \n"
            + str(self.a)
            + "\nb : \n"
            + str(self.b)
            + "\nx : \n"
            + str(self.x)
            + "\n"
        )


if __name__ == "__main__":
    print("=== Test work ===")
    size = 5
    a = np.random.rand(size, size)
    b = np.random.rand(size, 1)

    task = Task(a, b)
    x = task.work()
    print("check : ", np.allclose(a @ x, b))

    print("=== Test serialization ===")
    task = Task(a, b)
    print(task)
    s_json = task.to_json()
    task2 = Task.from_json(s_json)
    print(task2)

    print("check is equal : ", task == task2)


# Laws of Robotics
# First Law - A robot may not injure a human being or, through inaction, allow a human being to come to harm.
# Second Law - A robot must obey the orders given it by human beings except where such orders would conflict with the First Law.
# Third Law - A robot must protect its own existence as long as such protection does not conflict with the First or Second Law.
#
# Isaac Asimov
