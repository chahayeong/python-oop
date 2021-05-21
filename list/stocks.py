class Stocks(object):
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def stockprint(self):
        return f'종목이름: {self.name}, 종목코드: {self.code}'

    @staticmethod
    def del_element(ls, code):
        for i, j in enumerate(ls):
            if j.code == code:
                del ls[i]

    @staticmethod
    def main():
        ls = []
        while True:
            menu = input('1.종목추가 2.종목출력 3.종목삭제 4.종목수정 0.프로그램종료')
            if menu == '1':
                ls.append(Stocks(input('종목이름:'), input('종목코드:')))
            elif menu == '2':
                for i in ls:
                    print(f'출력결과: {i.stockprint()}')
            elif menu == '3':
                stock = Stocks(None, input('삭제할 종목코드'))
                stock.del_element(ls,stock.code)
            elif menu == '4':
                code = input('수정할 종목코드')
                stock = Stocks(input('수정할 이름'), code)
                stock.del_element(ls, code)
                ls.append(stock)
            elif menu == '0':
                print('프로그램을 종료합니다')
                break
            else:
                print('잘못된 입력입니다')

Stocks.main()