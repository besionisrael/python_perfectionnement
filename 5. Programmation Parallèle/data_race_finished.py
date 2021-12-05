#!/usr/bin/env python3
""" Two shoppers adding items to a shared notepad """

import threading

book_count = 0

def shopper():
    global book_count
    for i in range(10_000_000):
        book_count += 1

if __name__ == '__main__':
    barron = threading.Thread(target=shopper)
    olivia = threading.Thread(target=shopper)
    barron.start()
    olivia.start()
    barron.join()
    olivia.join()
    print('Nous devons acheter', book_count, 'crayons.')
