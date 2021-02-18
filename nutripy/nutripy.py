from enum import Enum
from .config import *

class Gender(Enum):
    MALE = 5
    FEMALE = -161


class Activity(Enum):
    SEDENTARY = 1.4
    ACTIVE = 1.6
    VERY_ACTIVE = 1.7


class Goal(Enum):
    LOSS = -CALORIES_STEP_SIZE
    MAINTAIN = 0
    GAIN = CALORIES_STEP_SIZE


    
class Nutripy(object):
    def _get_basal_metabolic_rate(self, age, weight, height, gender):
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + gender.value
        return bmr

    def get_daily_needs(self, age, weight, height, gender, activity, goal):
        bmr = self._get_basal_metabolic_rate(age, weight, height, gender)
        daily_needs = (bmr * activity.value) + goal.value
        return daily_needs
