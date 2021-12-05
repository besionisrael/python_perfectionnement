#!/usr/bin/env python3
""" Two shoppers adding items to a shared notepad """

import threading
import time

book_count = 0
pencil = threading.Lock()

def shopper():
    global book_count
    pencil.acquire()
    for i in range(10_000_000):
        book_count += 1
    pencil.release()

if __name__ == '__main__':
    barron = threading.Thread(target=shopper)
    olivia = threading.Thread(target=shopper)
    barron.start()
    olivia.start()
    barron.join()
    olivia.join()
    print('Nous devons acheter', book_count, 'livres.')
