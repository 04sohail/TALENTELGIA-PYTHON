class Employee:
    def __init__(self):
        print("this is constructor")
    def sum(self,num2):
        print("thi belongs to employee")
        return num2
    @staticmethod
    def stats(num):
        return num

    @classmethod
    def class1(self,num):
        return num

class Numbers(Employee):
    def __init__(self):
        print("numbers")
    def sum(self, num2):
        print("this belongs to sum")
        return num2


b1 = Employee()
# print(b1.sum(1))
# print(b1.stats(1))
# print(b1.class1())
# print(Employee.class1(1))
print(Numbers().sum(2))
print(Numbers().sum(30))
