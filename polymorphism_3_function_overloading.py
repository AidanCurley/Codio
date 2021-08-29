from statistics import median

class Median:
    def __init__(self):
        pass

    # Dealing with 2 to 5 parameters
    def calculate_median(num1, num2, num3 = None, num4 = None, num5 = None):
        if num3 != None and num4 != None and num5 != None:
            numbers = [num1, num2, num3, num4, num5]
        elif num3 != None and num4!= None:
            numbers =[num1, num2, num3, num4]
        elif num3 != None:
            numbers = [num1, num2, num3]
        else:
            numbers = [num1, num2]
        return median(numbers)

m = Median
print(m.calculate_median(3, 5, 1, 4, 2))
print(m.calculate_median(8, 6, 4, 2))
print(m.calculate_median(9, 3, 7))
print(m.calculate_median(5, 2))