class BMIcalculator(object):
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def cal_bmi(self):
        return self.weight / self.height ** 2 * 10000

    def bmirate(self):
        bmi = self.cal_bmi()
        rate =''

        if bmi <= 18.5:
            rate = '저체중'
        elif bmi <= 23:
            rate = '정상'
        elif bmi <= 25:
            rate = '과체중 의심'
        elif bmi <= 30:
            rate = '비만'
        else:
            rate = '고도 비만'
        return rate


    @staticmethod
    def main():
        bcal = BMIcalculator(int(input('몸무게 : ')), int(input('키 :')))
        print(f'키 : {bcal.weight}, 몸무게 : {bcal.height}의 BMI : {bcal.cal_bmi()}')
        print(f'bmi결과 : {bcal.bmirate()}')


BMIcalculator.main()