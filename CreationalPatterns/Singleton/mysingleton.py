#
# Singleton implementation of design pattern
# Author: Nilesh Sutar
# Email: sutar.nilesh@gmail.com


class Singleton(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__new__(cls)
        return cls.__instance

    def __init__(self, name=None):
        self.name = name

    def display(self):
        print(self.name, id(self), self.__hash__(), type(self))


class MySingleton(Singleton):
    pass


def main():
    a1 = Singleton('foo')
    a1.display()

    a2 = Singleton('bar')
    a2.display()

    a3 = MySingleton('foobar')
    a3.display()

    a4 = MySingleton('barfoo')
    a4.display()

    print("a1 == a2 : %s" % a1 == a2)
    print("a1 == a3: %s" % a1 == a3)
    print("a3 == a4: %s" % a3 == a4)
    print("a1 is singleton? %s" % isinstance(a1, Singleton))
    print("a2 is singleton? %s" % isinstance(a3, Singleton))
    print("a1 is singleton? %s" % isinstance(a1, MySingleton))
    print("a2 is singleton? %s" % isinstance(a3, MySingleton))


if __name__ == "__main__":
    main()

