from solver import Term, BinOp
# "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"

# token = 5 * X^0
#       = + - / *
#		= 9.3 * X^2


class InvalidToken(Exception):
    pass


class Parser:
    def __init__(self, equation):
        self.i = -1
        self.eq = equation.replace(" ", "")
        print(self.eq)
        self.len = len(self.eq)

    def parse_token(self):
        self.i += 1
        if self.i > self.len:
            return None
        if self.eq[self.i].isdigit():
            return Term(self.__number(), self.__power())
        if self.eq[self.i] in "+-/*":
            return 
        return None

    def __number(self):
        sub = ""
        # type 0 for integer and 1 for float
        type = 0
        while self.i < self.len and self.eq[self.i].isdigit():
            sub += self.eq[self.i]
            self.i += 1
            if self.i < self.len and self.eq[self.i] == '.':
                sub += self.eq[self.i]
                type = 1
                self.i += 1
        if self.i > 0 and self.eq[self.i - 1] == '.':
            raise InvalidToken("number in term can't finish by a dot")
        return int(sub) if type == 0 else float(sub)

    def __power(self):
        if self.i + 4 > self.len:
            raise InvalidToken("invalid power in term")
        if self.eq[self.i] != '*':
            raise InvalidToken("expect '*' in term")
        self.i += 1
        if not(self.eq[self.i] in "Xx"):
            raise InvalidToken("expect 'X' or 'x' in term")
        self.i += 1
        if self.eq[self.i] != '^':
            raise InvalidToken("expect '^' in term")
        self.i += 1
        if not(self.eq[self.i].isdigit()):
            raise InvalidToken("expect digit after '^'")
        sub = ""
        while self.i < self.len and self.eq[self.i].isdigit():
            sub += self.eq[self.i]
            self.i += 1
        return int(sub)