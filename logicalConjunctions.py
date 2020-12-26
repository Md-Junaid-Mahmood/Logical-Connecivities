from operators import *

class symbol:
    def __init__(self, variable):
        self.name = variable
        self.boolValue = 0

    def symbolDescription(self, text):
        self.description = text

    def printDescription(self):
        print(f"Description for the {self.name} is {self.description}")

class knowledgeBase:
    def __init__(self):
        self.knowledge = list()

    def appendAdd(self, symbol1, symbol2):
        xyz = andOperator(symbol1, symbol2)
        self.knowledge.append(xyz)

    def appendOr(self, symbol1, symbol2):
        xyz = orOperator(symbol1, symbol2)
        self.knowledge.append(xyz)

    def appendXor(self, symbol1, symbol2):
        xyz = xorOperator(symbol1, symbol2)
        self.knowledge.append(xyz)

    def appendNot(self, symbol1):
        xyz = notOperator(symbol1)
        self.knowledge.append(xyz)

    def appendAssert(self, symbol1):
        xyz = assertOperator(symbol1)
        self.knowledge.append(xyz)

    def appendImplication(self, symbol1, symbol2):
        xyz = implicationOperator(symbol1, symbol2)
        self.knowledge.append(xyz)

    def appendbiDirectionalImplication(self, symbol1, symbol2):
        xyz = biDirectionalImplicationOperator(symbol1, symbol2)
        self.knowledge.append(xyz)

    def printFunction(self):
        print(f"[", end = "")
        for id in range(len(self.knowledge) - 1):
            val = self.knowledge[id]
            val.printFunction()
            print(f" and ", end = "")
        val = self.knowledge[len(self.knowledge) - 1]
        val.printFunction()
        print("]")

    def binaryConverter(self, num, count):
        stg = ""
        i = 0
        while num != 0:
            if num % 2 == 0:
                stg = "0" + stg
            else:
                stg = "1" + stg
            i = i + 1
            num = int(num/2)
        i = count - i
        stg = "0"*i + stg
        return(stg)

    def modelCheckAlgorithm(self, prime):
        listOfSymbols = list()
        primeNumber = -1
        count = 0
        for id in range(len(self.knowledge)):
            val = self.knowledge[id]
            s1 = val.sym1
            s2 = val.sym2

            if s1 in listOfSymbols:
                pass
            else:
                count = count + 1
                listOfSymbols.append(s1)
                if s1 == prime:
                    primeNumber = count

            if s2 is None:
                pass
            elif s2 in listOfSymbols:
                pass
            else:
                count = count + 1
                listOfSymbols.append(s2)
                if s2 == prime:
                    primeNumber = count
       
        ct = pow(2, count)

        for i in range(ct):
            strep = self.binaryConverter(i, count)
       
            for j in range(count):
                listOfSymbols[j].boolValue = int(strep[j])

            exp = True
            for j in range(len(self.knowledge)):
                val = self.knowledge[j]
                exp = val.evaluateExpression()
                if exp == False:
                    break

            if exp == True and listOfSymbols[primeNumber - 1].boolValue == 0:
                prime.printDescription()
                print("Above statement is false")
                return

        prime.printDescription()
        print("Above statement is true")
        return