from enum import Enum

class Gender(Enum):
    MALE = 5
    FEMALE = -161


class Activity(Enum):
    SEDENTARY = 1.4
    ACTIVE = 1.6
    VERY_ACTIVE = 1.7


class Goal(Enum):
    LOSS_1000 = -1000
    LOSS_500 = -500
    MAINTAIN = 0
    GAIN_500 = 500
    GAIN_1000 = 1000


class Nutripy(object):
    def _get_basal_metabolic_rate(self, age, weight, height, gender):
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + gender.value
        return bmr

    def get_daily_needs(self, age, weight, height, gender, activity, goal):
        bmr = self._get_basal_metabolic_rate(age, weight, height, gender)
        daily_needs = (bmr * activity.value) + goal.value
        return daily_needs
