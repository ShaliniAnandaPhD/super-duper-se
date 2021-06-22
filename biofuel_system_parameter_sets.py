
# Constants

def biofuel_system_parameter_sets( set_id ) :
    if set_id == 1 :
        return {
            'ALPHA_N' : 0.66 , # Growth rate (1/h)
            'ALPHA_R' : 0.01 , # Basal repressor production rate (1/h)
            'BETA_R'  : 2.1  , # Repressor degradation rate (1/h)
            'BETA_P'  : 0.66 , # Pump degradation rate (1/h)
            'DELTA_N' : 0.91 , # Biofuel toxicity coefficient (1/(Mh))
            'DELTA_B' : 0.5  , # Biofuel export rate per pump (1/(Mh))
            'GAMMA_P' : 0.14 , # Pump toxicity threshold
            'GAMMA_I' : 60e-6 , # Inducer saturation threshold (M)
            'GAMMA_R' : 1.8   , # Repressor saturation threshold
            'K_R'     : 10    , # Repressor activation constant (h)
            'K_P'     : 0.2   , # Pump activation constant (1/h)
            'K_B'     : 100   , # Repressor deactivation constant (1/M)
            'V'       : 0.1   , # Ratio of intra to extracellular volume
            'I'       : 1e-3  # Amount of inducer
        }

    elif set_id == 2 :
        return {
            'ALPHA_N' : 0.50  , # Growth rate (1/h)
            'ALPHA_R' : 0.01  , # Basal repressor production rate (1/h)
            'BETA_R'  : 1.5   , # Repressor degradation rate (1/h)
            'BETA_P'  : 0.40  , # Pump degradation rate (1/h)
            'DELTA_N' : 0.78  , # Biofuel toxicity coefficient (1/(Mh))
            'DELTA_B' : 0.45   , # Biofuel export rate per pump (1/(Mh))
            'GAMMA_P' : 0.23  , # Pump toxicity threshold
            'GAMMA_I' : 50e-6 , # Inducer saturation threshold (M)
            'GAMMA_R' : 1.5   , # Repressor saturation threshold
            'K_R'     : 9    , # Repressor activation constant (h)
            'K_P'     : 0.17   , # Pump activation constant (1/h)
            'K_B'     : 100   , # Repressor deactivation constant (1/M)
            'V'       : 0.1   , # Ratio of intra to extracellular volume
            'I'       : 1e-3  # Amount of inducer
        }
