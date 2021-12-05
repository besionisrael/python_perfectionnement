# define enumerations using the Enum base class

from enum import Enum, unique, auto


@unique
class Fruit(Enum):
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    TOMATO = 4
    PEAR = auto() 

class Status(Enum):
    HTTP_OK = 200
    HTTP_CREATED = 201
    HTTP_ACCEPTED = 202
    HTTP_NON_AUTHORITATIVE = 203
    HTTP_NO_CONTENT = 204
    HTTP_PARTIAL_CONTENT = 206
    HTTP_MULTIPLE_CHOICES = 300
    HTTP_MOVED_PERMANENTLY = 301
    HTTP_MOVED_TEMPORARILY = 302
    HTTP_SEE_OTHER = 303
    HTTP_NOT_MODIFIED = 304
    HTTP_BAD_REQUEST = 400
    HTTP_UNAUTHORIZED = 401
    HTTP_PAYMENT_REQUIRED = 402
    HTTP_FORBIDDEN = 403
    HTTP_NOT_FOUND = 404
    HTTP_METHOD_NOT_ALLOWED = 405
    HTTP_INTERNAL_SERVER_ERROR = 500
    HTTP_NOT_IMPLEMENTED = 501
    HTTP_BAD_GATEWAY = 502

def main():
    # enums have human-readable values and types
    print(Fruit.APPLE)
    print(type(Fruit.APPLE))
    print(repr(Fruit.APPLE))

    # enums have name and value properties
    print(Fruit.APPLE.name, Fruit.APPLE.value)

    #Status
    print(Status)
    print(Status(200))
    print(Status['HTTP_UNAUTHORIZED'])
    print(Status.HTTP_BAD_REQUEST)
    print(Status(200).value)
    print(Status(200).name)
    print(Status['HTTP_OK'].value)


    # print the auto-generated value
    print(Fruit.PEAR.value)

    # enums are hashable - can be used as keys
    myFruits = {}
    myFruits[Fruit.BANANA] = "Come Mr. Tally-man"
    print(myFruits[Fruit.BANANA])


    


if __name__ == "__main__":
    main()
