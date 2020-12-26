class andOperator:
    def __init__(self, symbol1, symbol2):
        self.name1 = symbol1.name
        self.name2 = symbol2.name
        self.sym1 = symbol1
        self.sym2 = symbol2

    def printFunction(self):
        print(f"({self.name1} & {self.name2})", end = "")

    def evaluateExpression(self):
        x = self.sym1.boolValue
        y = self.sym2.boolValue
        if x == 1 and y == 1:
            return True
        else:
            return False

class orOperator:
    def __init__(self, symbol1, symbol2):
        self.name1 = symbol1.name
        self.name2 = symbol2.name
        self.sym1 = symbol1
        self.sym2 = symbol2

    def printFunction(self):
        print(f"({self.name1} | {self.name2})", end = "")

    def evaluateExpression(self):
        x = self.sym1.boolValue
        y = self.sym2.boolValue
        if x == 1 or y == 1:
            return True
        else:
            return False

class xorOperator:
    def __init__(self, symbol1, symbol2):
        self.name1 = symbol1.name
        self.name2 = symbol2.name
        self.sym1 = symbol1
        self.sym2 = symbol2

    def printFunction(self):
        print(f"({self.name1} xor {self.name2})", end = "")

    def evaluateExpression(self):
        x = self.sym1.boolValue
        y = self.sym2.boolValue
        if x == 1 and y == 0:
            return True
        elif x == 0 and y == 1:
            return True
        else:
            return False

class notOperator:
    def __init__(self, symbol1):
        self.name1 = symbol1.name
        self.name2 = None
        self.sym1 = symbol1
        self.sym2 = None

    def printFunction(self):
        print(f"(!{self.name1})", end = "")

    def evaluateExpression(self):
        x = self.sym1.boolValue
        if x == 1:
            return False
        else:
            return True

class assertOperator:
    def __init__(self, symbol1):
        self.name1 = symbol1.name
        self.name2 = None
        self.sym1 = symbol1
        self.sym2 = None

    def printFunction(self):
        print(f"({self.name1})", end = "")

    def evaluateExpression(self):
        x = self.sym1.boolValue
        if x == 0:
            return False
        else:
            return True

class implicationOperator:
    def __init__(self, symbol1, symbol2):
        self.name1 = symbol1.name
        self.name2 = symbol2.name
        self.sym1 = symbol1
        self.sym2 = symbol2

    def printFunction(self):
        print(f"({self.name1} -> {self.name2})", end = "")

    def evaluateExpression(self):
        x = self.sym1.boolValue
        y = self.sym2.boolValue
        if x == 0:
            return True
        elif y == 1:
            return True
        else:
            return False

class biDirectionalImplicationOperator:
    def __init__(self, symbol1, symbol2):
        self.name1 = symbol1.name
        self.name2 = symbol2.name
        self.sym1 = symbol1
        self.sym2 = symbol2

    def printFunction(self):
        print(f"({self.name1} <-> {self.name2})", end = "")

    def evaluateExpression(self):
        x = self.sym1.boolValue
        y = self.sym2.boolValue
        if x == 1 and y == 1:
            return True
        elif x == 0 and y == 0:
            return True
        else:
            return False
