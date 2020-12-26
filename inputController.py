import inquirer
from logicalConjunctions import *
from operators import *

class inputController:
    def __init__(self, var1, var2, var3, var4):
        self.varSymbol = var1
        self.varSentence = var2

        self.varPerformAlgorithm = var3
        self.varExit = var4

        self.symbolList = list()
        xyz = symbol("None")
        xyz.symbolDescription("It represents a void")
        self.symbolList.append(xyz)


    def inputStream(self):
        kb = knowledgeBase()
        print("Following options are available: ")
        print(f"{self.varSymbol} for inserting Symbol")
        print(f"{self.varSentence} for inserting Sentence")

        print(f"{self.varPerformAlgorithm} for performing algorithm")
        print(f"{self.varExit} for exit")

        print("Please Input Your Choice: ", end = "")
        charInput = input()
        print("")
        while charInput != self.varExit:
            if charInput == self.varSymbol:
                self.takeSymbol()
            elif charInput == self.varSentence:
                self.takeSentence(kb)
            elif charInput == self.varPerformAlgorithm:
                print("Input Prime Symbol: ", end = "")
                strg = input()
                self.perfromAlgorithm(kb, strg)
            else:
                print("Please Enter correct command")
            print("Please Input Your Choice: ", end = "")
            charInput = input()
            print("")
            

    def takeSymbol(self):
        print("Input Symbol for Your Statement: ", end = "")
        strg1 = input()
        print("")
        print("Input Description for Your Symbol: ", end = "")
        strg2 = input()
        print("")

        xyz = symbol(strg1)
        xyz.symbolDescription(strg2)

        self.symbolList.append(xyz)

    def takeSentence(self, kb):
        try:
            print("Input Operator for Your Statement: ", end = "")
            options = [inquirer.List('op',
                message="What size do you need?",
                choices=['And', 'Or', 'Xor','Not', 'Assert','Imply', 'BidirectionalImply'],
                ),
            ]
            answers = inquirer.prompt(options)

            print("Input first Symbol: ", end = "")
            strg1 = input()
            print("")

            print("Input second Symbol: ", end = "")
            strg2 = input()
            print("")

            ob1 = -1
            ob2 = -1
            w = 0
            for i in range(len(self.symbolList)):
                if self.symbolList[i].name == strg1:
                    ob1 = i
                    w = w + 1

                if self.symbolList[i].name == strg2:
                    ob2 = i
                    w = w + 1

                if w == 2:
                    break

            if w != 2:
                raise Exception("Symbols entered are invalid")
        
            if answers['op'] == 'And':
                kb.appendAdd(self.symbolList[ob1], self.symbolList[ob2])
            elif answers['op'] == 'Or':
                kb.appendOr(self.symbolList[ob1], self.symbolList[ob2])
            elif answers['op'] == 'Xor':
                kb.appendXor(self.symbolList[ob1], self.symbolList[ob2])
            elif answers['op'] == 'Not':
                kb.appendNot(self.symbolList[ob1])
            elif answers['op'] == 'Assert':
                kb.appendAssert(self.symbolList[ob1])
            elif answers['op'] == 'Imply':
                kb.appendImplication(self.symbolList[ob1], self.symbolList[ob2])
            else:
                kb.appendbiDirectionalImplication(self.symbolList[ob1], self.symbolList[ob2])
        except:
            print("Please enter the valid Symbol")
            print("1 to continue or any other number to return: ", end = "")
            number = int(input())
            print("")
            if number == 1:
                self.takeSentence(kb)
            else:
                return


    def takePrimeSymbol(self, strg):
        ob = -1
        for i in range(len(self.symbolList)):
            if self.symbolList[i].name == strg:
                ob = i
                break
        
        if ob == -1:
            raise Exception("Given symbol {strg} is invalid")
        return self.symbolList[ob]

    def perfromAlgorithm(self, kb, strg):
        try:
            prime = self.takePrimeSymbol(strg)
            kb.printFunction()
            kb.modelCheckAlgorithm(prime)
        except:
            print("Please enter the correct Symbol")
            print("1 to continue or any other number to return: ", end = "")
            number = int(input())
            print("")
            if number == 1:
                print("Input Prime Symbol: ", end = "")
                strg = input()
                self.perfromAlgorithm(kb, strg)
            else:
                return