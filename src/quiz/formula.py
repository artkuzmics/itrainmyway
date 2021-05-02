import pandas as pd
from pandas import read_csv
from django.conf import settings


def formula(quiz):


    filename = settings.BASE_DIR + "/quiz/static/loveyoursport_weights.csv"
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

    # Step 2

    checkbox = list(quiz.keys())[1:]

    strengths = ["flexibility","focus","lower_body","balance","endurance"]
    weaknesses = ["speed","hand_eye_coordination","upper_body","foot_eye_coordination","being_in_water"]

    picked_strengths = [s for s in strengths if s in checkbox]
    picked_weaknesses = [w for w in weaknesses if w in checkbox]

    strength_sum = data[picked_strengths].sum(axis=1)
    weakness_sum = data[picked_weaknesses].sum(axis=1)

    Step_2_score = strength_sum - weakness_sum


    # Step 4

    characteristics = ["perfectionist","patient","high_energy","competitive","thrive_under_pressure"]

    checked = [c for c in characteristics if c in checkbox]
    unchecked = [c for c in characteristics if c not in checked]

    checked_sum = data[checked].sum(axis=1)
    unchecked_sum = data[unchecked].sum(axis=1)

    Step_4_score = checked_sum - unchecked_sum * 0.5


    # Step 5

    environments = ["tried_and_tested", "ever_changing", "centre_of_attention", "express_myself", "adrenaline_fuelled"]

    checked = [c for c in environments if c in checkbox]
    unchecked = [c for c in environments if c not in checked]

    checked_sum = data[checked].sum(axis=1)
    unchecked_sum = data[unchecked].sum(axis=1)

    Step_5_score = checked_sum - unchecked_sum * 0.5

    # Bank

    rating = pd.DataFrame(dict(Strength = Step_2_score, Personality = Step_4_score, Settings = Step_5_score))

    rating = rating.sort_values(by = ['Strength', 'Personality', 'Settings'], ascending=False)

    A = set(Step_2_score.sort_values(ascending=False).iloc[:3].index)
    B = set(Step_4_score.sort_values(ascending=False).iloc[:3].index)
    C = set(Step_5_score.sort_values(ascending=False).iloc[:3].index)

    longlist = []

    longlist.append(list(A & B & C))
    longlist.append(list(A & B))
    longlist.append(list(A & C))
    longlist.append(list(B & C))
    longlist.append(list(rating.index))
    longlist.append(["Running", "Cycling", "Rock Climbing", "Acro Yoga", "Trampolining"])

    # Flatten list
    longlist = [item for sublist in longlist for item in sublist]

    #Remove duplicates
    longlist = [sport for i, sport in enumerate(longlist) if sport not in longlist[:i]]

    return longlist



#formula({'csrfmiddlewaretoken': 'pTyG1egdeBGJE3zqrjAZDRgsvwpGwrhBmKqVexNwyfZ2vWZt2G6CxE65oqkTDWpv', 'time': 'days', 'money': 'reasonable amount', 'Who do you want to exercise with': '', 'alone': 'on', 'group': 'on', 'contactsport': 'maybe', 'how': 'in a team', 'fitnesslevel': 'unbeatable', 'height': 'short', 'Which of these are your superpowers': '', 'flexibility': 'on', 'focus': 'on', 'Which of the below are your weaknesses': '', 'upper_body_stregth': 'on', 'foot_eye_coordination': 'on', 'Which of the below characteristics describe you': '', 'perfectionist': 'on', 'patient': 'on', 'Which of these workout environments do you enjoy': '', 'express_myself': 'on', 'adrenaline_fuelled': 'on', 'gender': 'male', 'age': '25'})
