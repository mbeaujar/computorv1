# "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"

OPERATOR = 0
TERM = 1
PLUS = 2
MIN = 3
MUL = 4
DIV = 5


class Term:
    def __init__(self, value, power):
        self.value = value
        self.power = power
        self.type = TERM

    def __str__(self) -> str:
        return str(self.value) + " * X^" + str(self.power)


class BinOp:
    def __init__(self, operator, left, right):
        self.operator = operator
        self.type = OPERATOR
        self.left = left
        self.right = right


class Solver:
    def __init__(self):
        self.root = None
