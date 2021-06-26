# -*- coding: utf-8 -*-
# import pretty_errors


class A(object):
    def __init__(self):
        self.__x = 3

    def __spam(self):
        print("A.__spam() is called")

    def bar(self):
        self.__spam()


class B(A):
    def __init__(self):
        A.__init__(self)
        self.__x = 37

    # def __spam(self):
    #     print("B.__spam() is called")

    def barx(self):
        # self.__spam()
        self._A__spam()


if __name__ == '__main__':
    # print(pretty_errors.__version__)
    print("- " * 10)
    a = A()
    a.bar()
    print(dir(a))
    print(getattr(a, "_A__x"), hasattr(a, "__x"), hasattr(a, "_A__x"))

    print("= " * 10)
    b = B()
    b.bar()
    b.barx()
    print(dir(b))
