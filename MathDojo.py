class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        print (num + nums)
        return self

    def subtract(self, num, *nums):
        print (nums - num)
        return self