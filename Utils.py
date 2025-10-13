class Utils:

    @staticmethod
    def clamp(num, minValue, maxValue):
        if(num < minValue):
            num = minValue
        elif(num > maxValue):
            num = maxValue
        print(num)
        return num