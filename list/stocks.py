class Stocks(object):
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def stockprint(self):
        return f'종목이름: {self.name}, 종목코드: {self.code}'

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
                stockName = input('삭제할 종목 이름을 입력하세요')
                for i,j in enumerate(ls):
                    if j.name == stockName:
                        del ls[i]
            elif menu == '4':
                modify_name = input('수정할 종목 이름을 입력하세요')
                modify_info = Stocks(modify_name, input('종목코드:'))
                for i, j in enumerate(ls):
                    if j.name == modify_name:
                        del ls[i]
                        ls.append(modify_info)
            elif menu == '0':
                print('프로그램을 종료합니다')
                break
            else:
                print('잘못된 입력입니다')

Stocks.main()