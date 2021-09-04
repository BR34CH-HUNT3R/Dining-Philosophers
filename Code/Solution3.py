"""
            ************** * Solution 3 * **************

    Idée: -Si seulement quatre philosophes sont autorisés à s'asseoir, l’interblocage ne peut pas se produire.
          -Chaque philosophe est représenté par un Thread.
          -Chaque fourchette est représentée par un sémaphore initialisé à 1 (mutex: Lock()).
          -Un sémaphore(4) pour représenter les chaises.

            @author: Ahmed Rafik El-Mehdi BAAHMED
"""

from threading import *
import time

p = []                           # list of philosophers
n = 5                            # number of philosophers / forks

f = [Lock() for i in range(n)]   # list of forks
c = Semaphore(4)                 # chairs

def philosopher(i):
    while True:
        print("p"+str(i)+" is thinking")
        print("p" + str(i) + " wants to sit on a chair")
        c.acquire()
        try:
            print("p" + str(i) + " sat on a chair")
            print("p" + str(i) + " wants to take fork" + str(i))
            f[i].acquire()
            try:
                print("p" + str(i) + " took fork" + str(i))
                print("p" + str(i) + " wants to take fork" + str((i + 1) % n))
                f[(i + 1) % n].acquire()
                try:
                    print("p" + str(i) + " took fork" + str((i + 1) % n))
                    print("p" + str(i) + " is eating")
                    time.sleep(0.5)
                finally:
                    f[(i + 1) % n].release()
                    print("p" + str(i) + " droped fork" + str((i + 1) % n))
            finally:
                f[i].release()
                print("p" + str(i) + " droped fork" + str(i))
                print("p" + str(i) + " finished thinking and eating")
        finally:
            c.release()
            print("p" + str(i) + " released the chair")


if __name__ == "__main__":
    for i in range(n):
        p.append(Thread(target=philosopher, args=[i]))
        print("starting of p"+str(i))
        p[i].start()