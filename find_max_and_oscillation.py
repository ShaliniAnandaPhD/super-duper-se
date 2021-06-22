"""
Purpose: The file defines the function find_max_and_oscillation which is used
in the file test_1A_1B to test both sim_biofuel and this file.

Author Josh Bryden

"""
import numpy as np


def find_max_and_oscillation(input_array):
    """
    Arguments:
        input_array {array} -- [takes biofuel_int_array which contains levels of
                            internal biofuel within the bacteria]

    Outputs:
        max_value {float} -- [maximum value from input_array]
        oscillationSize {float} -- [amount of oscillation in internal biofuel]
    """

    # find max value in the input array
    max_value_int = np.max(input_array)
    # if last value is max then oscillation is zero
    if input_array[-1] == max_value_int:
        oscillationSize = 0
        return max_value_int, oscillationSize
    else:
        # find index of max value
        max_value_index = np.argmax(input_array)
        # slice array from max index +1 onwards and find min
        min_biofuel_int = np.min(input_array[max_value_index+1:])
        # compute oscillation
        oscillationSize = max_value_int-min_biofuel_int
        return max_value_int, oscillationSize
