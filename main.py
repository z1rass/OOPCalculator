class Calculator():
    mainString = ''
    numsAndOper = []
    firstNum = 0
    secondNum = 0
    operator = ''
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
        match op:
            case '+':
                print(self.firstNum + self.secondNum)
            case '-':
                print(self.firstNum - self.secondNum)
            case '*':
                print(self.firstNum * self.secondNum)
            case '/':
                print(self.firstNum / self.secondNum)
            case '**':
                print(self.firstNum ** self.secondNum)
            case '%':
                print(self.firstNum % self.secondNum)
            case _:
                print("Invalid operator")

                
    def run(self):
        if(self.validate()):
            self.returnAnser()



while True:
    s = input("Write: ")
    c = Calculator(s)
    c.run()

