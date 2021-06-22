"""
Author Josh Bryden

File defines the function 'design' that determines the optimal alpha_b and
alpha_p levels for production of biofuel. The function also determines design
parameters that will maximise biofuel but without constraints on maximal
internal biofuel or oscillation levels. File is to be used in conjunction with
test_2B.py as part of HDAT9300
"""


def design(THRESHOLD_MAX_INTERNAL_FUEL, THRESHOLD_MAX_OSCILLATION_INTERNAL_FUEL,
           alpha_b_array, alpha_p_array, max_internal_biofuel,
           oscillation_internal_biofuel, final_external_biofuel):
    """
    Arguments:
        THRESHOLD_MAX_INTERNAL_FUEL {float} -- [A threshold on the maximum amount of
                                                internal biofuel]

        THRESHOLD_MAX_OSCILLATION_INTERNAL_FUEL {float} -- [A threshold on the
                                             maximum amount of internal biofuel
                                             oscillation]

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

    Outputs:
        best_alpha_b {float} -- [The alpha_b value that returns the most biofuel]

        best_alpha_p {float} -- [The alpha_p value that returns the most biofuel]

        poor_alpha_b {float} -- [The alpha_b value that returns the most biofuel
                                with no constraints]

        poor_alpha_p {float} -- [The alpha_p value that returns the most biofuel
                                with no constraints]
"""
    import numpy as np

    # find shape of final biofuel and assign to rows and cols
    rows = final_external_biofuel.shape[0]
    cols = final_external_biofuel.shape[1]
    # set global max variable to compare to
    global_max_poor = 0
    # loop over rows and cols
    for i in range(rows):
        for j in range(cols):
            # compare each value to max
            if final_external_biofuel[i, j] > global_max_poor:
                # set to max if it is the max value at present
                global_max_poor = final_external_biofuel[i, j]
            else:
                continue
    # find index where max is
    global_max_poor_index = np.where(final_external_biofuel == global_max_poor)
    # assign poor values to the location of the tuple of np.where indexes
    poor_alpha_b = alpha_b_array[global_max_poor_index[0]]
    poor_alpha_p = alpha_p_array[global_max_poor_index[1]]
    # repeat for best values
    global_max_final = 0
    # loop over range of rows and cols
    for i in range(rows):
        for j in range(cols):
            # if [i,j] value is under thresholds
            if max_internal_biofuel[i, j] <= THRESHOLD_MAX_INTERNAL_FUEL:
                if oscillation_internal_biofuel[i, j] <= THRESHOLD_MAX_OSCILLATION_INTERNAL_FUEL:
                    # if final max is less than current [i,j] value then assign to max
                    if global_max_final < final_external_biofuel[i,j]:
                        global_max_final = final_external_biofuel[i,j]


     # find index where global max final is
    global_max_best_index = np.where(final_external_biofuel == global_max_final)
    # assign best values to the location of the tuple of np.where indexes
    best_alpha_b = alpha_b_array[global_max_best_index[0]]
    best_alpha_p = alpha_p_array[global_max_best_index[1]]

    return best_alpha_b, best_alpha_p, poor_alpha_b, poor_alpha_p
