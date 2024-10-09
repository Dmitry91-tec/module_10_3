import threading
from threading import Thread, Lock
import random
from time import sleep

class Bank:
    lock=Lock()

    def __init__(self,balance=0):
        self.balance=balance

    def deposit(self):
        for _ in range(100):
            i=random.randrange(50,500)
            self.balance+=i
            print(f'Пополнениe: {i}, баланс {self.balance}')
            if self.balance>=500 and self.lock.locked()==True:
                self.lock.release()
                print(f'Пополнениe: {i}, баланс {self.balance}')
            sleep(0.001)
        return
    def take(self):
        for _ in range(100):
            i=random.randrange(50,500)
            print(f'Запрос на {i}')
            if i<=self.balance:
                self.balance -= i
                print(f'Снятие:{i}. Баланс:{self.balance}')
            if i>=self.balance:
                print(f'Запрос отклонен, недостаточно средств')
                self.lock.acquire()
        return

bk=Bank()
th1=threading.Thread(target=Bank.deposit, args=(bk,))
th2=threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')