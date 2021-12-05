# demonstrate built-in utility functions


def main():
    # use any() and all() to test sequences for boolean values
    list1 = [1, 2, 3, 0, 5, 6]
    
    # any will return true if any of the sequence values are true
    print(any(list1))
    
    # all will return true only if all values are true
    print(all(list1))
    
    # min and max will return minimum and maximum values in a sequence
    print("min: ", min(list1))
    print("max: ", max(list1))    
    
    # Use sum() to sum up all of the values in a sequence
    print("sum: ", sum(list1))

    # **** Iterator

    # define a list of days in English and French
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

    # use iter to create an iterator over a collection
    i = iter(days)
    print(next(i))  # Sun
    print(next(i))  # Mon
    print(next(i))  # Tue

    # iterate using a function and a sentinel
    with open("testfile.txt", "r") as fp:
        for line in iter(fp.readline, ''):
            print(line)

    # use regular interation over the days
    for m in range(len(days)):
        print(m+1, days[m])

    # using enumerate reduces code and provides a counter
    for i, m in enumerate(days, start=1):
        print(i, m)

    # use zip to combine sequences
    for m in zip(days, daysFr):
        print(m)

    for i, m in enumerate(zip(days, daysFr), start=1):
        print(i, m[0], "=", m[1], "in French")
    
    
if __name__ == "__main__":
    main()
    