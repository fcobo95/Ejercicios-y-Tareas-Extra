class TaresServiciosWeb:
    # self means that the constructor is taking in the instance of that object.
    def __init__(self, the_array):
        self.the_array = the_array
        self.the_result_array = []

    # This method will handle how to calculate the square root of 1000 numbers that go into an array.
    def float_square_roots(self):
        print('This prints the square root for each number in the array.')

        for each_number in self.the_array:
            try:
                square_root = each_number ** (1 / 2)
                self.the_result_array.append(square_root)
                print('{} : {}'.format(each_number, square_root))
            except Exception as ex:
                return 'Something went wrong: ' + str(ex)
        return 'Process finished with exit code 0'

    def integer_square_roots(self):
        the_result_array = []
        the_array = []
        import random
        for each_number in range(random.randrange(0, 1000)):
            print('')
        return the_result_array


array = TaresServiciosWeb([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16])
print(TaresServiciosWeb.float_square_roots(array))
