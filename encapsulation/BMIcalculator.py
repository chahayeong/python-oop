class BMIcalculator:
    def setbmi(self, weight, height):
        self.weifht = weight
        self.height = height

    def calbmi(self):
        height2 = (self.height * self.height) * 0.0001
        return self.weifht / height2

if __name__ == '__main__':
    bmi = BMIcalculator()
    bmi.setbmi(42, 162)
    print(bmi.calbmi())