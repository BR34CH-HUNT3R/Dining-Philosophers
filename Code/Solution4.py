"""
            ************** * Solution 4 * **************

    Idée: -Chaque philosophe est représenté par un Thread.
          -Chaque philosophe aura trois états possibles: { PENSE || A_FAIM || MANGE }.
          -Un sémaphore est attribué à chaque philosophe.
          -Lorsqu'il a faim, un philosophe ne peut manger que si ses deux voisins ne mangent pas, sinon attend.
          -Lorsqu'il termine de manger, le philosophe réveille ses voisins et se remet à penser.
          -Un philosophe qui veut prendre les fourchettes (donc manger) déclare qu'il a faim.

            @author: Ahmed Rafik El-Mehdi BAAHMED
"""

from threading import *
import time

p = []                                              # list of philosophers
n = 5                                               # number of philosophers / forks

philo = [Semaphore(0) for i in range(n)]                # list of philosopher semaphores
mutex = Lock()
state = ['PENSE','PENSE','PENSE','PENSE','PENSE']   # state of philosophers { PENSE || A_FAIM || MANGE }

def eat_test(i):
    if (state[i] == 'A_FAIM' and state[(i + 1) % n] != 'MANGE' and state[(i - 1 + n) % n] != 'MANGE'):
        state[i] = 'MANGE'
        philo[i].release()


def take_forks(i):
    mutex.acquire()
    state[i] = 'A_FAIM'
    eat_test(i)
    mutex.release()
    philo[i].acquire()

def drop_forks(i):
    mutex.acquire()
    state[i] = 'PENSE'
    eat_test((i + 1) % n)
    eat_test((i - 1 + n) % n)
    mutex.release()

def philosopher(i):
    while True:
        print("p"+str(i)+" is thinking")
        print("p"+str(i)+" is hungry and wants to eat")
        print(state)
        take_forks(i)
        print("p" + str(i) + " is eating")
        print(state)
        time.sleep(0.5)
        drop_forks(i)
        print("p" + str(i) + " finished eating and thinks")

if __name__ == "__main__":
    for i in range(n):
        p.append(Thread(target=philosopher, args=[i]))
        print("starting of p"+str(i))
        p[i].start()