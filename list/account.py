from random import *

class Account(object):
    def __init__(self, name, price):
        self.bankname = 'SC은행'
        self.name = name
        self.account = self.rand_account()
        self.price = price

    def get_account(self):
        return f'은행명: {self.bankname}, 예금주: {self.name}, 계좌번호: {self.account}, 잔액: {self.price}'

    def rand_account(self):
        num1 = randrange(0, 999)
        num2 = randrange(0, 99)
        num3 = randrange(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        account_number = num1 + '-' + num2 + '-' + num3

        return account_number

    @staticmethod
    def main():
        ls = []
        while True:
            menu = input('1.계좌개설, 2.계좌출력, 0.프로그램종료 ')

            if menu == '1':
                ls.append(Account(str(input('예금주:')), int(input('초기잔액:'))))
            elif menu == '2':
                for i in ls:
                    print(i.get_account())
            elif menu == '0':
                print('프로그램을 종료합니다')
                break
            else:
                print('잘못된 입력입니다')


Account.main()