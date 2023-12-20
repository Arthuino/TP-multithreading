import unittest

import numpy as np
from task import Task


class TaskTestCase(unittest.TestCase):
    def test_eq(self):
        a1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        b1 = [[10], [11], [12]]
        task1 = Task(a1, b1)

        a2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        b2 = [[10], [11], [12]]
        task2 = Task(a2, b2)

        self.assertTrue(task1 == task2)

    def test_to_json(self):
        a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        b = np.array([[10], [11], [12]])
        task = Task(a, b)
        expected_json = '{"identifier": 1, "a": [[1, 2, 3], [4, 5, 6], [7, 8, 9]], "b": [[10], [11], [12]], "x": null}'
        self.assertEqual(task.to_json(), expected_json)

    def test_from_json(self):
        json_str = '{"identifier": 1,"a": [[1, 2, 3], [4, 5, 6], [7, 8, 9]], "b": [[10], [11], [12]], "x": null}'
        expected_a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        expected_b = np.array([[10], [11], [12]])
        task = Task.from_json(json_str)
        self.assertTrue(task.identifier == 1)
        self.assertTrue(np.array_equal(task.a, expected_a))
        self.assertTrue(np.array_equal(task.b, expected_b))

    def test_serialization(self):
        a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        b = [[10], [11], [12]]
        task = Task(a, b)
        self.assertEqual(Task.from_json(task.to_json()), task)


if __name__ == "__main__":
    unittest.main()
