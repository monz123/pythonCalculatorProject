def addition(a, b):
    return a + b


def subtraction(a, b):
    return b - a


def multiplication(a, b):
    return a * b


def division(a, b):
    return float(b/a)


def square(a):
    return a * a


class Calculator:
    result = 0

    def __init__(self):
        self.result = 1
        pass

    def add(self, a, b):
        self.result = addition(int(a), int(b))
        return self.result

    def sub(self, a, b):
        self.result = subtraction(int(a), int(b))
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(int(a), int(b))
        return self.result

    def squares(self, a):
        self.result = square(int(a))
        return self.result

    def divide(self, a, b):
        self.result = division(int(a), int(b))
        return self.result




