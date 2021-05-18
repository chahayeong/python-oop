class Person(object):
    def __init__(self, name, year, address):
        self.name = name
        self.year = year
        self.address = address

    def yearCal(self):
        return 2021 - self.year

    @staticmethod
    def main():
        p = Person(str(input('이름:')), int(input('출생년도:')), str(input('주소:')))
        print(f'회원이름: {p.name}')
        print(f'회원나이: {p.yearCal()}')
        print(f'회원주소: {p.address}')

Person.main()
