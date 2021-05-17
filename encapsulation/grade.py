class Grade:
    def setgrade(self,kor,eng,mat):
        self.kor = kor
        self.eng = eng
        self.mat = mat

    def sum(self):
        return self.kor + self.eng + self.mat
    def avg(self):
        return self.sum() / 3



if __name__ == '__main__':
    g = Grade()
    g.setgrade(10,20,30)
    print(g.sum())
    print(g.avg())