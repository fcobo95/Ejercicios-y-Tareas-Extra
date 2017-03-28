class TaresServiciosWeb:
    def __init__(self):
        self.data = []

    def __init__(self, the_array, the_result_array):
        self.the_array = the_array
        self.the_result_array = the_result_array

    # This method will handle how to calculate the square root of 1000 numbers that go into an array.
    def float_square_roots(self):
        the_result_array = []
        the_array = []
        # I fill the_array with float values
        for each_value in range(1000):
            the_array.append(float(each_value))
        """
        I iterate through all the values of "the_array" and calculate their respective square root value
        it then appends it to "the_result_array" and transforms it into a Dictionary.
        """
        for each_number in the_array:
            square_root = each_number ** (1 / 2)
            print(the_result_array.append({
                "Number": each_number,
                "Square Root": square_root
            }))
        return the_result_array

    float_square_roots()

    def integer_square_roots(self):
        the_result_array = []
        the_array = []
        import random
        for each_number in range(random.randrange(0, 1000)):
            print('')
        return None