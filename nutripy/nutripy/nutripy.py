class Nutripy(object):
 
    def _get_gender_factor(self, gender):
        if gender == "male":
            return 5
        elif gender == "female":
            return -161

    def _get_activity_factor(self, activity):
        if activity == "sedentary":
            return 1.2
        elif activity == "lightly_active":
            return 1.375
        elif activity == "moderately_active":
            return 1.55
        elif activity == "very_active":
            return 1.725
        elif activity == "extra_active":
            return 1.9 

    def _get_goal_factor(self, goal):
        if goal == "loss_1000":
            return -1000
        elif goal == "loss_500":
            return -500
        elif goal == "maintain":
            return 0
        elif goal == "gain_500":
            return 500
        elif goal == "gain_1000":
            return 1000

    def _get_basal_metabolic_rate(self, age, weight, height, gender):
        gender_factor = self._get_gender_factor(gender)
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + gender_factor
        return bmr

        
    def get_daily_needs(self, age, weight, height, gender, activity, goal):
        bmr = self._get_basal_metabolic_rate(age, weight, height, gender)
        activity_factor = self._get_activity_factor(activity)
        goal_factor = self._get_goal_factor(goal)
        daily_needs = (bmr * activity_factor) + goal_factor
        return daily_needs
