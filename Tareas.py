# -------------------- CLASS FloatArray BEGINS ----------------------------------------------------------------------- #
class FloatArray:
    # self means that the constructor is taking in the instance of that object.
    # self is always taken as the first argument in the constructor parameters
    def __init__(self):
        self.the_array = []
        self.the_result_array = []

    def fill_array(self):
        for each_number in range(20):
            self.the_array.append(each_number)

    def format(self, x, y):
        return print('{} : {}'.format(x, y))

    # This method will handle how to calculate the square root of 1000 numbers that go into an array.
    def square_root(self):
        print('This prints the square root for each number in the array.')
        for each_number in self.the_array:
            try:
                square_root = each_number ** (1 / 2)
                self.the_result_array.append(square_root)
                self.format(each_number, square_root)
            except Exception as ex:
                return 'Something went wrong: ' + str(ex)
        return ''

    def subtract(self, number1, number2):
        return number1 - number2

    def subtract_n_from_array(self, n):
        for each_number in self.the_array:
            new_number = self.subtract(each_number, n)
            self.format(each_number, new_number)
        return 'Succesful operation'


# -------------------- CLASS FloatArray ENDS ------------------------------------------------------------------------- #
# Instance of FloatArray class
floatClass = FloatArray()
print('---------------BEGIN OF FLOATARRAY CLASS---------------' + '\n')
FloatArray.fill_array(floatClass)
FloatArray.square_root(floatClass)
FloatArray.subtract_n_from_array(floatClass, 10)
print('---------------END OF FLOATARRAY CLASS---------------' + '\n')


# -------------------- CLASS IntegerArray BEGINS --------------------------------------------------------------------- #
class IntegerArray:
    def __init__(self):
        self.the_array = []
        self.the_result_array = []

    def integer_square_roots(self):
        import random
        for each_number in range(1000):
            try:
                self.the_array.append(random.randint(1, 1000))
            except Exception as ex:
                return 'Something went wrong: ' + str(ex)
        for each_number in self.the_array:
            try:
                square_root = each_number ** (1 / 2)
                self.the_result_array.append(each_number + square_root)
                print('{} : {}'.format(each_number, square_root))
            except Exception as ex:
                return 'Something went wrong: ' + str(ex)
        return ''

# -------------------- CLASS IntegerArray ENDS ----------------------------------------------------------------------- #
# Instance of IntegerArray class
# intClass = IntegerArray()
# print('---------------BEGIN OF INTEGERARRAY CLASS---------------' + '\n')
# print(IntegerArray.integer_square_roots(intClass))
# print('---------------END OF INTEGERARRAY CLASS---------------' + '\n')
