# Constants


def biofuel_simulation_design_parameter_sets( set_id ) :

    if set_id == 1 :
        return {

            # Initial (normalized) amount of bateria
            'INITIAL_BACTERIA_AMOUNT' : 0.01,

            # Simulation start and end times, simulation time interval
            'TIME_START' : 0,     # Start time
            'TIME_END' : 40,      # End time
            'TIME_DELTA' : 0.1,   # Delta t

            # alpha_b: Lower and upper limits, number of points
            'ALPHA_B_EXP_LOWER' : -2,
            'ALPHA_B_EXP_UPPER' : 0,
            'ALPHA_B_NUMBER_POINTS' : 20,

            # alpha_p: Lower and upper limits, step size
            'ALPHA_P_LOWER' : 0.01,
            'ALPHA_P_UPPER' : 0.1,
            'ALPHA_P_STEP' : 0.01,

            # Design parameters for biofuel system
            # Upper limit on the amount of internal fuel
            'THRESHOLD_MAX_INTERNAL_FUEL' : 0.15,
            # Upper limit on the amount of oscillation
            'THRESHOLD_MAX_OSCILLATION_INTERNAL_FUEL' : 0.01

        }

    elif set_id == 2 :
        return {

            # Initial (normalized) amount of bateria
            'INITIAL_BACTERIA_AMOUNT' : 0.1,

            # Simulation start and end times, simulation time interval
            'TIME_START' : 0,     # Start time
            'TIME_END' : 50,      # End time
            'TIME_DELTA' : 0.05,   # Delta t

            # alpha_b: Lower and upper limits, number of points
            'ALPHA_B_EXP_LOWER' : -2,
            'ALPHA_B_EXP_UPPER' : 0,
            'ALPHA_B_NUMBER_POINTS' : 30,

            # alpha_p: Lower and upper limits, step size
            'ALPHA_P_LOWER' : 0.005,
            'ALPHA_P_UPPER' : 0.1,
            'ALPHA_P_STEP' : 0.005,

            # Design parameters for biofuel system
            # Upper limit on the amount of internal fuel
            'THRESHOLD_MAX_INTERNAL_FUEL' : 0.15,
            # Upper limit on the amount of oscillation
            'THRESHOLD_MAX_OSCILLATION_INTERNAL_FUEL' : 0.01

        }
