class Contacts(object):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def get_contact(self):
        return f'이름:{self.name}, 전화번호:{self.phone}, 이메일:{self.email}, 주소:{self.address}'



    @staticmethod
    def main():
        ls = []
        while True:
            menu = input('1.입력 2.출력 3.삭제 4.수정 0.프로그램 종료')
            if menu == '1':
                ls.append(Contacts(input('이름:'),input('전화번호:'), input('이메일:'), input('주소:')))

            elif menu == '2':
                for i in ls:
                    print(f'출력결과: {i.get_contact()}')

            elif menu == '3':
                delete = input('삭제할 이름을 입력하세요')
                for i,j in enumerate(ls):
                    if j.name == delete:
                        del ls[i]

            elif menu == '4':
                edit_name = input('수정할 이름: ')
                edit_info = Contacts(edit_name, input('수정 전화번호'), input('수정 이메일'), input('수정 주소'))
                for i, j in enumerate(ls):
                    if j.name == edit_name:
                        del ls[i]
                        ls.append(edit_info)

            elif menu == '0':
                print('프로그램을 종료합니다')
                break

            else:
                print('잘못된 입력입니다')

Contacts.main()
