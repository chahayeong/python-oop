from random import *

class Account(object):
    def __init__(self, name, price):
        self.bankname = 'SC은행'
        self.name = name
        self.account = self.create_account_number()
        self.price = price

    def get_account(self):
        return f'은행명: {self.bankname}, 예금주: {self.name}, 계좌번호: {self.account}, 잔액: {self.price}'

    @staticmethod
    def create_account_number(self):
        ls = []
        for i in range(3):
            ls.append(str(random.randint(0,9)))
        ls.append('-')
        for i in range(2):
            ls.append(str(random.randint(0,9)))
            ls.append('-')
            for i in range(6):
                ls.append(str(random.randint(0,9)))
                return "".join(ls)

    @staticmethod
    def del_account(ls, name):
        for i, j in enumerate(ls):
            if j.name == name:
                del ls[i]

    @staticmethod
    def main():
        ls = []
        while True:
            menu = input('1.계좌개설, 2.계좌출력, 3.계좌삭제, 4.계좌수정 0.프로그램종료 ')

            if menu == '1':
                ls.append(Account(str(input('예금주:')), int(input('초기잔액:'))))
            elif menu == '2':
                for i in ls:
                    print(i.get_account())
            elif menu == '3':
                account = Account(input('삭제할 계좌 이름:'), None)
                account.del_account(ls, account.name)
            elif menu == '4':
                name = input('수정할 계좌 이름:')
                acct = Account(input('이름 수정:'), input('잔액 수정:'))
                acct.del_account(ls, name)
                ls.append(acct)

            elif menu == '0':
                print('프로그램을 종료합니다')
                break
            else:
                print('잘못된 입력입니다')


Account.main()