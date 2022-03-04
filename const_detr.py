class Sample:
    num = 0

    def __init__(self, var):
        Sample.num += 1
        self.var = var

        print("Object value is = ", var)
        print("Variable value = ", Sample.num)

    def __del__(self):
        Sample.num -= 1

        print("Object with value %d is exit from the scope" % self.var)


S1 = Sample(10)