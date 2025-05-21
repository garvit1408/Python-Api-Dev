# Data Analysis Part

import pandas as pd
import numpy as np

ipl_matches = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRy2DUdUbaKx_Co9F0FSnIlyS-8kp4aKv_I0-qzNeghiZHAI_hw94gKG22XTxNJHMFnFVKsO4xWOdIs/pub?gid=1655759976&single=true&output=csv"
matches = pd.read_csv(ipl_matches)

# print(matches.head())


# use colab for data analysis purpose, then simply copy-paste, colab is way more good
def teamsAPI():
    teams = list(set(list(matches["Team1"]) + list(matches["Team2"])))
    team_dict = {"teams": teams}
    return team_dict


def teamVteamAPI(team1, team2):
    temp_df = matches[
        (matches["Team1"] == team1) & (matches["Team2"] == team2)
        | (matches["Team1"] == team2) & (matches["Team2"] == team1)
    ]
    total_matches = temp_df.shape[0]
    matches_won_team1 = temp_df["WinningTeam"].value_counts()[team1]
    matches_won_team2 = temp_df["WinningTeam"].value_counts()[team2]

    draws = total_matches - (matches_won_team1 + matches_won_team2)

    respones = {
        "total_matches": total_matches,
        team1: int(matches_won_team1),
        team2: int(matches_won_team2),
        "draws": int(draws),
    }
    return respones
