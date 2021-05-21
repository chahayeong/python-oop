from random import *

class Account(object):
    def __init__(self, name, account, price):
        self.bankname = 'SC은행'
        self.name = name
        self.account = account
        self.price = price

    def get_account(self):
        return f'은행명: {self.bankname}, 예금주: {self.name}, 계좌번호: {self.account}, 잔액: {self.price}'

    @staticmethod
    def rand_account():
        num1 = randrange(0, 999)
        num2 = randrange(0, 99)
        num3 = randrange(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        account_number = num1 + '-' + num2 + '-' + num3

        return account_number

    @staticmethod
    def del_account(ls, account):
        for i, j in enumerate(ls):
            if j.account == account:
                del ls[i]

    @staticmethod
    def main():
        ls = []
        while True:
            menu = input('1.계좌개설, 2.계좌출력, 3.계좌삭제, 4.입금 5.출금 0.프로그램종료 ')

            if menu == '1':
                ls.append(Account(str(input('예금주:')),Account.rand_account(), int(input('초기잔액:'))))
            elif menu == '2':
                for i in ls:
                    print(i.get_account())
            elif menu == '3':
                account = Account(input('삭제할 계좌 번호:'),None, None)
                account.del_account(ls, account.name)
            elif menu == '4':
                number = input('입금할 계좌번호:')
                money = input('입금액:')
                for i,j in enumerate(ls):
                    if j.account == number:
                        replace = Account(j.name, j.account, int(j.price) + int(money))
                        Account.del_account(ls, number)
                        ls.append(replace)
            elif menu == '5':
                number = input('출금할 계좌번호:')
                money = input('출금액:')
                for i,j in enumerate(ls):
                    if j.account == number:
                        replace = Account(j.name, j.account, int(j.price) - int(money))
                        Account.del_account(ls, number)
                        ls.append(replace)
            elif menu == '0':
                print('프로그램을 종료합니다')
                break
            else:
                print('잘못된 입력입니다')


Account.main()