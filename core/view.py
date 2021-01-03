class View:
    def __init__(self):
        self.__data = []

    def load(self, data):
        self.__data = data
        return self

    def show(self):
        print(self.__data)

    def success(self):
        print(self.__data)

    def error(self):
        print(self.__data)