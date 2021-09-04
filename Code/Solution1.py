"""
            ************** * Solution 1 (naive) * **************

    Idée: -Chaque philosophe est représenté par un Thread.
          -Chaque fourchette est représentée par un sémaphore initialisé à 1 (mutex: Lock()).

    Problème: Interblocage possible si tous les philosophes prennent la fourchette de gauche,
    personne ne pourra prendre la fourchette a sa droite


            @author: Ahmed Rafik El-Mehdi BAAHMED
"""

from threading import *
import time

p = []                              # list of philosophers
n = 5                               # number of philosophers / forks

f = [Lock() for i in range(n)]      # list of forks

def philosopher(i):
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