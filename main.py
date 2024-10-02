class Calculator():
    mainString = ''
    numsAndOper = []
    firstNum = 0
    secondNum = 0
    operator = ''
    answer = 0
    def __init__(self, mainString):
        self.mainString = mainString
                
        

    def validate(self):
        
        try:
            self.numsAndOper = self.mainString.split(" ")
            self.firstNum = int(self.numsAndOper[0])
            self.secondNum = int(self.numsAndOper[2])
            self.operator = self.numsAndOper[1]
            if len(self.numsAndOper) != 3:
                print('Fuck u nigga')
                return False
            else:
                return True
        except Exception as e:
            print("Fick dich Nigga")
            return False

        


    def returnAnser(self):
        op = self.operator
        try:
            match op:
                case '+':
                    self.answer = self.firstNum + self.secondNum
                    print(self.answer)
                case '-':
                    self.answer = self.firstNum - self.secondNum
                    print(self.answer)
                case '*':
                    self.answer = self.firstNum * self.secondNum
                    print(self.answer)
                case '/':
                    self.answer = self.firstNum / self.secondNum
                    print(self.answer)
                case '**':
                    self.answer = self.firstNum ** self.secondNum
                    print(self.answer)
                case '%':
                    self.answer = self.firstNum % self.secondNum
                    print(self.answer)
                case _:
                    print("Invalid operator")
            return True
        except Exception as e:
            print("Probably u tried to devine by 0, u can't")
            return False
        
    def addInFile(self):
        with open('history.txt', 'a+') as f:
            inFile = self.mainString + " = " + str(self.answer) + "\n"
            f.write(inFile)      
    def run(self):
        if(self.validate()):
            if(self.returnAnser()):
                self.addInFile()
                


while True:
    s = input("Write: ")
    c = Calculator(s)
    c.run()

