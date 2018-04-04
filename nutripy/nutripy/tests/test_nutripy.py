import unittest
from ..nutripy import Nutripy


class TddNutripy(unittest.TestCase):
 
    def test_correct_gender_factor(self):
        nut = Nutripy()
        gender_factor = nut._get_gender_factor("male")
        self.assertEqual(gender_factor, 5)
        gender_factor = nut._get_gender_factor("female")
        self.assertEqual(gender_factor, -161)

    def test_correct_activity_factor(self):
        nut = Nutripy()
        activity_factor = nut._get_activity_factor("sedentary")
        self.assertEqual(activity_factor, 1.2)
        activity_factor = nut._get_activity_factor("lightly_active")
        self.assertEqual(activity_factor, 1.375)
        activity_factor = nut._get_activity_factor("moderately_active")
        self.assertEqual(activity_factor, 1.55)
        activity_factor = nut._get_activity_factor("very_active")
        self.assertEqual(activity_factor, 1.725)
        activity_factor = nut._get_activity_factor("extra_active")
        self.assertEqual(activity_factor, 1.9)

    def test_correct_goal_factor(self):
        nut = Nutripy()
        goal_factor = nut._get_goal_factor("loss_1000")
        self.assertEqual(goal_factor, -1000)
        goal_factor = nut._get_goal_factor("loss_500")
        self.assertEqual(goal_factor, -500)
        goal_factor = nut._get_goal_factor("maintain")
        self.assertEqual(goal_factor, 0)
        goal_factor = nut._get_goal_factor("gain_500")
        self.assertEqual(goal_factor, 500)
        goal_factor = nut._get_goal_factor("gain_1000")
        self.assertEqual(goal_factor, 1000)

    def test_correct_basal_metabolic_rate(self):
        nut = Nutripy()
        
        age = 25
        weight = 60
        height = 180
        gender = "male"
        bmr = nut._get_basal_metabolic_rate(age, weight, height, gender)
        self.assertEqual(bmr, 1605)

    def test_correct_daily_needs(self):
        nut = Nutripy()
        
        age = 25
        weight = 60
        height = 180
        gender = "male"
        activity = "sedentary"
        goal = "loss_1000"
        daily_needs = nut.get_daily_needs(age, weight, height, gender, activity, goal)
        self.assertEqual(daily_needs, 926)
        
        
if __name__ == '__main__':
    unittest.main()
    
