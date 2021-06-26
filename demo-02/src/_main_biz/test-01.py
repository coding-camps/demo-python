# -*- coding: utf-8 -*-

class ACls(object):

    def __init__(self, name: str):
        self._name = name

    @property
    def name(self):
        # print("-" * 10)
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError(str(name), "must be a string.")
        self._name = name

    @name.deleter
    def name(self):
        raise TypeError("Cannot delete property name")


class BCls(ACls):
    def __init__(self, name:str, age: int):
        # super().__init__(name)
        super(self.__class__, name)
        self.age = age


if __name__ == '__main__':
    # aclz = ACls("AAA str")
    # print(aclz.name)
    # aclz.name = "BBB str"
    # print(aclz.name)
    # print("ok")
    bclz = BCls("sb.", 10)
    print(bclz.name)
