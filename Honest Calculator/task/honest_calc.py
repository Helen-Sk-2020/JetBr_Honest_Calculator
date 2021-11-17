class Calculator:
    messages = {
        0: "Enter an equation",
        1: "Do you even know what numbers are? Stay focused!",
        2: "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
        3: "Yeah... division by zero. Smart move...",
        4: "Do you want to store the result? (y / n):",
        5: "Do you want to continue calculations? (y / n):",
        6: " ... lazy",
        7: " ... very lazy",
        8: " ... very, very lazy",
        9: "You are",
        10: "Are you sure? It is only one digit! (y / n)",
        11: "Don't be silly! It's just one number! Add to the memory? (y / n)",
        12: "Last chance! Do you really want to embarrass yourself? (y / n)"
    }
    
    def __init__(self):
        self.var_1 = self.var_2 = self.result = self.memory = 0
        self.calc = self.oper = ''
        self.operators = ['+', '-', '*', '/']
    
    def take_calc(self):
        print(self.messages[0])
        self.calc = input().split()
    
    def check_var(self):
        try:
            if self.calc[0] == 'M' and self.calc[2] == 'M':
                self.var_1 = self.memory
                self.var_2 = self.memory
            elif self.calc[0] == 'M':
                self.var_1 = self.memory
                self.var_2 = float(self.calc[2])
            elif self.calc[2] == 'M':
                self.var_1 = float(self.calc[0])
                self.var_2 = self.memory
            else:
                self.var_1 = float(self.calc[0])
                self.var_2 = float(self.calc[2])
            return True
        except (ValueError, IndexError):
            print(self.messages[1])
    
    def check_oper(self):
        try:
            if self.calc[1] in self.operators:
                self.oper = self.calc[1]
                return True
            else:
                raise ValueError
        except (ValueError, IndexError):
            print(self.messages[2])
    
    def implement(self):
        if self.oper == '+':
            self.result = self.var_1 + self.var_2
            print(self.result)
            return True
        elif self.oper == '-':
            self.result = self.var_1 - self.var_2
            print(self.result)
            return True
        elif self.oper == '*':
            self.result = self.var_1 * self.var_2
            print(self.result)
            return True
        elif self.oper == '/':
            try:
                self.result = self.var_1 / self.var_2
                print(self.result)
                return True
            except ZeroDivisionError:
                self.result = 0
                print(self.messages[3])
                return False
    
    def store_result(self):
        print(self.messages[4])
        counter = 10
        while True:
            answer = input()
            if answer == 'y':
                if counter == 13 and answer == 'y':
                    self.memory = self.result
                    break
                if self.is_one_digit(self.result):
                    print(self.messages[counter])
                    counter += 1
                else:
                    self.memory = self.result
                    break
            elif answer == 'n':
                break
    
    @staticmethod
    def is_one_digit(v):
        try:
            if float(v) == int(v):
                if -10 < int(v) < 10:
                    return True
        except ValueError:
            return False
    
    def check_difficulty(self):
        message = ""
        if self.is_one_digit(self.var_1) and self.is_one_digit(self.var_2):
            message += self.messages[6]
        if self.var_1 == 1 or self.var_2 == 1 and self.oper == '*':
            message += self.messages[7]
        if self.var_1 == 0 or self.var_2 == 0:
            if self.oper == '+' or self.oper == '-' or self.oper == '*':
                message += self.messages[8]
        
        if message != "":
            print(self.messages[9] + message)


def main():
    calculation = Calculator()
    while True:
        calculation.take_calc()
        if calculation.check_var():
            if calculation.check_oper():
                calculation.check_difficulty()
                if calculation.implement():
                    calculation.store_result()
                    print(calculation.messages[5])
                    answer = input()
                    if answer == 'n':
                        break


if __name__ == "__main__":
    main()
