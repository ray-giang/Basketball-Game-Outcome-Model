
# Creating a function to cover this entire flow

import pandas as pd

def predict_game_outcome(config, model):    
    if type(config) == dict:
        df = pd.DataFrame(config)
    else:
        df = config
    df = df.drop(columns = ['win_flag_team1'])
    y_pred_prob = model.predict_proba(df)
    prob = float(y_pred_prob[:,1])
    return "Team 1 has a {}% chance of winning".format(round(prob*100,2))

