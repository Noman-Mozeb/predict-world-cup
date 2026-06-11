import numpy as np
import pandas as pd

TEAMS_DB = pd.DataFrame({
    'Team': ['Argentina', 'France', 'Spain', 'England', 'Brazil', 'Portugal', 'Morocco', 'Germany'],
    'Strength': [2.4, 2.3, 2.4, 2.1, 2.2, 2.2, 1.8, 2.0],
    'WC_2022': ['Winner', 'Runner-up', 'Round of 16', 'Quarter-final', 'Quarter-final', 'Quarter-final', '4th Place', 'Groups']
})

def run_poisson_engine(team_A, team_B, sims=5000):
    strength_A = TEAMS_DB[TEAMS_DB['Team'] == team_A]['Strength'].values
    strength_B = TEAMS_DB[TEAMS_DB['Team'] == team_B]['Strength'].values

    wins_A, wins_B = 0, 0
    for _ in range(sims):
        gA = np.random.poisson(strength_A)
        gB = np.random.poisson(strength_B)
        if gA > gB: wins_A += 1
        elif gB > gA: wins_B += 1
        else:
            if (gA + np.random.poisson(strength_A * 0.3)) > (gB + np.random.poisson(strength_B * 0.3)): wins_A += 1
            else: wins_B += 1

    return (wins_A / sims) * 100, (wins_B / sims) * 100
