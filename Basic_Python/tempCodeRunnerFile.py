class Account:
    def __init__(self, acc_num, acc_pass):
        self.acc_num = acc_num
        self.__acc_pass = acc_pass
    def reset_pass(self):
        print(self.__acc_pass)

a = Account("123456", "pass@1234")
print(a.acc_num)
a.reset_pass()