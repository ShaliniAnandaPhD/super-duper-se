"""
Author Josh Bryden

File defines the function generate that is used to create 3 matrices that
define levels of internal biofuel, levels of oscillation in internal biofuel and
the final levels of external biofuel that can be produced from our design
parameters. File is to be used in conjunction with test 2A.py as part of HDAT9300.
"""
import numpy as np
import sim_biofuel as sb
import find_max_and_oscillation as fmo


def generate(data_set_to_use, time_array, INITIAL_BACTERIA_AMOUNT,
             alpha_b_array, ALPHA_P_LOWER, ALPHA_P_UPPER, ALPHA_P_STEP):
    """

    Arguments:
        data_set_to_use {int} -- [Set id for system constants needed for simulation]
        time_array {[array} -- [An array of uniformly distributed time instances]
        INITIAL_BACTERIA_AMOUNT {float} -- [The initial amount of bacteria]
        ALPHA_P_LOWER {float} -- [The first element in alpha_p_array]
        ALPHA_P_UPPER {float} -- [The last element in alpha_p_array]
        ALPHA_P_STEP {float} -- [The step value in alpha_p_array]

    Outputs:
        alpha_b_array {array} -- [Array of the parameter alpha_b which is the
                                    production rate of biofuel]
        alpha_p_array {array} -- [Array of the parameter alpha_p which is the
                                    production rate of efflux pumps]
        max_internal_biofuel {array} -- [Array of the max internal biofuel for
                                            each alpha_b and alpha_p]
        oscillation_internal_biofuel {array} -- [Array of the oscillation of
                                                    internal biofuel for each
                                                    alpha_b and alpha_p]
        final_external_biofuel {array} -- [Array of the final external biofuel
                                             for each alpha_b and alpha_p]
    """

    # create alpha p array
    # ALPHA_P_UPPER needs to be last element so stop is upper + step
    alpha_p_array = np.arange(ALPHA_P_LOWER, ALPHA_P_UPPER + ALPHA_P_STEP,
                              ALPHA_P_STEP)

    # create matrices with rows len(alpha_b_array) + cols len(alpha_p_array)
    max_internal_biofuel = np.zeros((len(alpha_b_array), len(alpha_p_array)))
    # create same shape as above
    oscillation_internal_biofuel = np.zeros_like(max_internal_biofuel)
    final_external_biofuel = np.zeros_like(max_internal_biofuel)

    # assign num of cols and rows to variables --> return tuple so index 0 and 1
    # TODO CHECK PYLINT DOCS RE "unscriptable object"
    # * (https://stackoverflow.com/questions/58646585/why-pylintreturns-unsubscriptable-object-for-numpy-ndarray-shape)
    #! Works here but still returns warning error from pylint for two lines below
    rows = max_internal_biofuel.shape[0]
    cols = max_internal_biofuel.shape[1]

    # simulate for pairs of alpha_b and alpha_p
    # loop over range of rows and cols (already contains 0 in rows and cols)
    # hence no need for a 0 start in the range function or a -1
    for i in range(rows):
        for j in range(cols):
            # call sim_biofuel using each element of alpha_b + alpha_p arrays
            bacteria_amount_array, sensor_array, pump_array, biofuel_int_array, \
                biofuel_ext_array = sb.sim_biofuel(data_set_to_use,
                                                   time_array, INITIAL_BACTERIA_AMOUNT,
                                                   alpha_b_array[i], alpha_p_array[j])

            # call find_max_and_oscillation onto biofuel_int_array
            # this finds the max integer value and oscillation size
            max_value_int, oscillationSize = fmo.find_max_and_oscillation(biofuel_int_array)
            # assign max_value_int to our matrix of max internal biofuels
            max_internal_biofuel[i, j] = max_value_int
            # assign our oscillation value from find_max_and_oscillation to matrix
            oscillation_internal_biofuel[i,j] = oscillationSize
            # assign the last value of biofuel_ext_array (from sim_biofuel) to matrix
            final_external_biofuel[i,j] = biofuel_ext_array[-1]

    return alpha_b_array, alpha_p_array, max_internal_biofuel, \
             oscillation_internal_biofuel, final_external_biofuel
