"""
            ************** * Solution 2 * **************

    Idée: -Une seule modification par rapport à la solution naive:
            Modifier l'ordre dans lequel le philosophe N-1 prend ses fourchettes.

            @author: Ahmed Rafik El-Mehdi BAAHMED
"""

from threading import *
import time

p = []                              # list of philosophers
n = 5                               # number of philosophers / forks

f = [Lock() for i in range(n)]      # list of forks

def philosopher(i):
    if (((i + 1) % n) == 0) :
        while True:
            print("p"+str(i)+" is thinking")
            print("p"+str(i)+" wants to take fork"+str((i+1)%n))
            f[(i+1)%n].acquire()
            try:
                print("p" + str(i) + " took fork" + str((i + 1) % n))
                print("p" + str(i) + " wants to take fork" + str(i))
                f[i].acquire()
                try:
                    print("p" + str(i) + " took fork" + str(i))
                    print("p" + str(i) + " is eating")
                    time.sleep(0.5)
                finally:
                    f[i].release()
                    print("p" + str(i) + " droped fork" + str(i))
            finally:
                f[(i+1)%n].release()
                print("p" + str(i) + " droped fork" + str((i + 1) % n))
                print("p" + str(i) + " finished thinking and eating")
    else:
        while True:
            print("p"+str(i)+" is thinking")
            print("p"+str(i)+" wants to take fork"+str(i))
            f[i].acquire()
            try:
                print("p" + str(i) + " took fork" + str(i))
                print("p" + str(i) + " wants to take fork" + str((i + 1) % n))
                f[(i+1)%n].acquire()
                try:
                    print("p" + str(i) + " took fork" + str((i + 1) % n))
                    print("p" + str(i) + " is eating")
                    time.sleep(0.5)
                finally:
                    f[(i+1)%n].release()
                    print("p" + str(i) + " droped fork" + str((i + 1) % n))
            finally:
                f[i].release()
                print("p" + str(i) + " droped fork" + str(i))
                print("p" + str(i) + " finished thinking and eating")


if __name__ == "__main__":
    for i in range(n):
        p.append(Thread(target=philosopher, args=[i]))
        print("starting of p"+str(i))
        p[i].start()