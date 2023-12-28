# Effectue plusieurs séries de mesures de temps d'execution
import time

import matplotlib.pyplot as plt
import numpy as np
from boss import Boss
from task import Task


def createMatrices(size):
    a = np.random.rand(size, size)
    b = np.random.rand(size, 1)
    return a, b


def testOneTask(boss, a, b):
    start_time = time.time()
    boss.add_task(Task(a, b))
    boss.get__and_check_result()
    end_time = time.time()
    return end_time - start_time


def testMatrixSize(boss, nbtest, size):
    return [testOneTask(boss, *createMatrices(size)) for _ in range(nbtest)]


def printRes(res, size):
    print("taille " + str(size) + " : " + str(res))
    print("moyenne : ", np.mean(res))


if __name__ == "__main__":
    boss = Boss()
    a, b = createMatrices(100)

    allres = list()
    allsizes = [
        100,
        300,
        500,
        800,
        1000,
        1500,
        2000,
        2500,
        3000,
        3500,
        4000,
        5000,
        6000,
        7000,
        8000,
        9000,
        10000,
    ]

    for size in allsizes:
        res = testMatrixSize(boss, 5, size)
        printRes(res, size)
        allres.append(np.mean(res))

    # Plot results
    plt.figure()
    plt.plot(allsizes, allres)
    plt.xlabel("Matrix size")
    plt.ylabel("Execution time (s)")
    plt.show()
