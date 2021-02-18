import unittest
from ..nutripy import Nutripy, Gender, Activity, Goal


class TddNutripy(unittest.TestCase):
 
    def test_correct_basal_metabolic_rate(self):
        nut = Nutripy()
        
        age = 25
        weight = 60
        height = 180
        gender = Gender.MALE
        bmr = nut._get_basal_metabolic_rate(age, weight, height, gender)
        self.assertEqual(bmr, 1605)

    def test_correct_daily_needs(self):
        nut = Nutripy()
        
        age = 25
        weight = 60
        height = 180
        gender = Gender.MALE
        activity = Activity.SEDENTARY
        goal = Goal.LOSS_1000
        daily_needs = nut.get_daily_needs(age, weight, height, gender, activity, goal)
        self.assertEqual(daily_needs, 926)
        
        
if __name__ == '__main__':
    unittest.main()
    
