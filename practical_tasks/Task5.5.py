class ReadOnly():
    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        return self._x


if __name__ == '__main__':
    read = ReadOnly(20)
    print(read.x)
