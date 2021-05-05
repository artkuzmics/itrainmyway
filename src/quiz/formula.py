import pandas as pd

import numpy as np
from pandas import read_csv
from django.conf import settings


def formula(quiz):


    filename = settings.BASE_DIR + "/quiz/static/loveyoursport_weights.csv"

    #filename = "../static/loveyoursport_weights.csv"

    data = read_csv(filename,delimiter=",")
    data = data.set_index(["Sport"])

    selection = {
        "time":{"minutes":[1,2],"hours":[2,3,4],"days":[3,4,5]},
        "money":{"as little as possible":[1,2,3], "reasonable amount":[2,3,4],"show me what you got":[3,4,5]},
        "contactsport":{"no":[1,2,3],"maybe":[1,2,3,4,5],"yes":[3,4,5]},
        "how":{"on my own":[1,2,3],"in a team":[3,4,5],"either is good":[1,2,3,4,5]},
        "fitnesslevel":{"start me gently":[1,2],"ready":[2,3,4],"unbeatable":[3,4,5]},
        "height":{"short":[1,2,3],"average":[2,3,4],"tall":[3,4,5]}
    }


    # Step 1
    keys = list(selection.keys())

    for key in keys:
        data = data.loc[data[key].isin(selection[key][quiz[key]])]
        quiz.pop(key)

    who_with = {'alone':[1,3,5,7], 'group':[2,3,6,7], 'family':[4,5,6,7]}
    checked = [c for c in who_with if c in quiz]

    # Select filter values from checked options
    filter = [who_with[c] for c in checked]

    # Flatten list
    filter = [item for sublist in filter for item in sublist]

    # Remove duplicates
    filter = list(set(filter))

    # Select sports according to filter
    data = data.loc[data["who with"].isin(filter)]



    if len(data) > 5:
        # Step 2

        checkbox = list(quiz.keys())[1:]

        strengths = ["flexibility","focus","lower_body","balance","endurance"]
        weaknesses = ["speed","hand_eye_coordination","upper_body","foot_eye_coordination","being_in_water"]

        picked_strengths = [s for s in strengths if s in checkbox]
        picked_weaknesses = [w for w in weaknesses if w in checkbox]

        strength_sum = data[picked_strengths].sum(axis=1)
        weakness_sum = data[picked_weaknesses].sum(axis=1)

        Step_2 = strength_sum - weakness_sum


        # Selecting top 3 to BANK (or more if the score of the sports are the same)
        top = -np.sort(-Step_2.unique())[:3]

        #print(Step_2.loc[Step_2.isin(top)].sort_values(ascending=False))

        A = set(Step_2.loc[Step_2.isin(top)].index)



        # Step 4

        characteristics = ["perfectionist","patient","high_energy","competitive","thrive_under_pressure"]

        checked = [c for c in characteristics if c in checkbox]
        unchecked = [c for c in characteristics if c not in checked]

        checked_sum = data[checked].sum(axis=1)
        unchecked_sum = data[unchecked].sum(axis=1)

        Step_4 = checked_sum - unchecked_sum * 0.5

        # Selecting top 3 to BANK (or more if the score of the sports are the same)
        top = -np.sort(-Step_4.unique())[:3]

        #print(Step_4.loc[Step_4.isin(top)].sort_values(ascending=False))

        B = set(Step_4.loc[Step_4.isin(top)].index)


        # Step 5

        environments = ["tried_and_tested", "ever_changing", "centre_of_attention", "express_myself", "adrenaline_fuelled"]

        checked = [c for c in environments if c in checkbox]
        unchecked = [c for c in environments if c not in checked]

        checked_sum = data[checked].sum(axis=1)
        unchecked_sum = data[unchecked].sum(axis=1)

        Step_5 = checked_sum - unchecked_sum * 0.5

        # Selecting top 3 to BANK (or more if the score of the sports are the same)
        top = -np.sort(-Step_5.unique())[:3]

        #print(Step_5.loc[Step_5.isin(top)].sort_values(ascending=False))

        C = set(Step_5.loc[Step_5.isin(top)].index)

        # Bank

        rating = pd.DataFrame(dict(Strength = Step_2, Personality = Step_4, Settings = Step_5))

        rating = rating.sort_values(by = ['Strength', 'Personality', 'Settings'], ascending=False)

        """
        A = set(Step_2_score.sort_values(ascending=False).iloc[:3].index)
        B = set(Step_4_score.sort_values(ascending=False).iloc[:3].index)
        C = set(Step_5_score.sort_values(ascending=False).iloc[:3].index)"""

        longlist = []

        longlist.append(list(A & B & C))
        longlist.append(list(A & B))
        longlist.append(list(A & C))
        longlist.append(list(B & C))
        longlist.append(list(rating.index))

    else:
        longlist = list(data.index)



    longlist.append(["Running", "Cycling", "Rock_Climbing", "Acro_Yoga", "Trampolining"])


    # Flatten list
    flatten = []
    for sublist in longlist:
        if type(sublist) == list:
            for item in sublist:
                flatten.append(item)
        else:
            flatten.append(sublist)

    longlist = flatten


    #Remove duplicates
    longlist = [sport for i, sport in enumerate(longlist) if sport not in longlist[:i]]


    return longlist[:6]
