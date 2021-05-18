class Human(object):
    def __init__(self,name,year,gender):
        self.name = name
        self.year = year
        self.gender = gender

    def __del__(self):
        print("나의 죽음을 알리지마라")

    def who(self):
        print(self.name)
        print(self.year)
        print(self.gender)

    def setInfo(self, name, year, gender):
        self.name = name
        self.year = year
        self.gender = gender

areum = Human("하영",25,"여자")
areum.who()

areum.setInfo("세영",23,"여자")
areum.who()