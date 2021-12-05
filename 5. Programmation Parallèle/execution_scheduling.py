""" Two threads resolving exercises """

import threading
import time

chopping = True

def resolving_exercise():
    name = threading.current_thread().getName()
    vegetable_count = 0
    while chopping:
        print(name, 'a resolu un exercice!')
        vegetable_count += 1
    print(name, 'a resolu', vegetable_count, 'exercices.')

if __name__ == '__main__':
    threading.Thread(target=resolving_exercise, name='Nana').start()
    threading.Thread(target=resolving_exercise, name='Nounou').start()

    time.sleep(1)    # resolve an exercice for 1 second
    chopping = False # stop both threads from resolving
