import pytest
from formula import *

def test_01():
    sports = formula({
                    'time': 'minutes',
                    'money': 'reasonable amount',
                    'alone': 'on',
                    'group': 'on',
                    'family': 'on',
                    'contactsport': 'no',
                    'how': 'on my own',
                    'fitnesslevel': 'start me gently',
                    'height': 'tall',
                    'flexibility': 'on',
                    'focus': 'on',
                    'speed': 'on',
                    'perfectionist': 'on',
                    'patient': 'on',
                    'ever_changing': 'on',
                    })

    assert set(sports) == {'Kettlebell Workout', 'Billiards', 'Vinyasa Yoga', 'Frisbee', 'Strength Training'}


def test_02():
    sports = formula({
                    'time': 'hours',
                    'money': 'reasonable amount',
                    'alone': 'on',
                    'group': 'on',
                    'contactsport': 'no',
                    'how': 'on my own',
                    'fitnesslevel': 'ready',
                    'height': 'tall',
                    'endurance': 'on',
                    'focus': 'on',
                    'hand_eye_coordination': 'on',
                    'foot_eye_coordination': 'on',
                    'being_in_water': 'on',
                    'perfectionist': 'on',
                    'patient': 'on',
                    'high_energy': 'on',
                    'competitive': 'on',
                    'thrive_under_pressure': 'on',
                    'tried_and_tested': 'on',
                    'express_myself': 'on',

                    })

    assert set(sports) == {'Distance Running','Latin Dancing','Trampolining','Hot Yoga','High Intensity Interval Training'}
