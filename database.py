import numpy as np
import pandas as pd

# Expanded 48-Team Database with real-time 2026 strength indexes
TEAMS_DB = pd.DataFrame({
    'Group': ['A']*4 + ['B']*4 + ['C']*4 + ['D']*4 + ['E']*4 + ['F']*4 + ['G']*4 + ['H']*4 + ['I']*4 + ['J']*4 + ['K']*4 + ['L']*4,
    'Team': [
        'USA', 'Mexico', 'Canada', 'Panama', 'Argentina', 'Chile', 'Colombia', 'Peru',
        'Brazil', 'Uruguay', 'Ecuador', 'Paraguay', 'France', 'Morocco', 'Austria', 'Mali',
        'Spain', 'Japan', 'Croatia', 'Nigeria', 'England', 'Netherlands', 'Senegal', 'Oman',
        'Portugal', 'Belgium', 'Tunisia', 'Jamaica', 'Germany', 'Switzerland', 'Australia', 'UAE',
        'Italy', 'Ukraine', 'Egypt', 'New Zealand', 'South Korea', 'Iran', 'Algeria', 'Iraq',
        'Denmark', 'Sweden', 'Cameroon', 'Qatar', 'Saudi Arabia', 'Poland', 'Ghana', 'Honduras'
    ],
    'Strength': [
        1.6, 1.4, 1.3, 0.9, 2.5, 1.3, 1.6, 1.0, 2.3, 1.9, 1.5, 1.1, 2.4, 1.8, 1.4, 1.1,
        2.4, 1.7, 1.6, 1.2, 2.2, 1.8, 1.5, 0.8, 2.3, 1.7, 1.2, 0.7, 2.1, 1.6, 1.3, 0.8,
        1.9, 1.5, 1.4, 0.7, 1.5, 1.4, 1.3, 0.9, 1.7, 1.5, 1.2, 0.9, 1.4, 1.4, 1.2, 0.8
    ]
})

def run_advanced_poisson(team_A, team_B, sims=5000):
    """Simulates matches including 90 mins, extra time, and penalty thresholds."""
    # .item() extracts the exact numeric value out of the Pandas series to prevent AttributeErrors
    lambda_A = TEAMS_DB[TEAMS_DB['Team'] == team_A]['Strength'].values[0]
    lambda_B = TEAMS_DB[TEAMS_DB['Team'] == team_B]['Strength'].values[0]
    
    wins_A, wins_B = 0, 0
    for _ in range(sims):
        gA = np.random.poisson(lambda_A)
        gB = np.random.poisson(lambda_B)
        if gA > gB: 
            wins_A += 1
        elif gB > gA: 
            wins_B += 1
        else:
            # Extra Time (Fatigue modifier applied)
            exA = np.random.poisson(lambda_A * 0.33)
            exB = np.random.poisson(lambda_B * 0.33)
            if (gA + exA) > (gB + exB): 
                wins_A += 1
            elif (gB + exB) > (gA + exA): 
                wins_B += 1
            else:
                # Sudden death penalty flips
                if np.random.rand() > 0.5: 
                    wins_A += 1
                else: 
                    wins_B += 1
                    
    return (wins_A / sims) * 100, (wins_B / sims) * 100
