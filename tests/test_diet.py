import unittest
from nutripy import Nutripy, Gender, Activity, Goal
from nutripy.diet import get_new_state, Phase, is_close

import numpy as np

class TddDiet(unittest.TestCase):
 
    def test_has_gained_weight_with_gain_goal(self):
        def delta_weight(tdci, tdee, sigma=.6):
            return np.random.normal(0, sigma) + ((tdci - tdee) * 7) / 7000 


        nut = Nutripy()

        initial_weight = 80

        params = {
            "age": 30, 
            "height": 180, 
            "gender": Gender.MALE, 
            "activity": Activity.SEDENTARY, 
            "goal": Goal.GAIN,
            "weight_history": [initial_weight, 80, 80.5, 80],
            "phases_history":[Phase.GAIN, Phase.GAIN, Phase.GAIN, Phase.GAIN],
            "tdci": nut.get_daily_needs(30, 80, 180, Gender.MALE, Activity.SEDENTARY, Goal.GAIN),
            "tdee": nut.get_daily_needs(30, 80, 180, Gender.MALE, Activity.SEDENTARY, Goal.GAIN),
        }

    
        for i in range(20):
            state = get_new_state(**params)
        
            new_phase = state["phase"]
            new_tdci = state["tdci"]
            new_tdee = state["tdee"]
            
            tdci = params["tdci"]
            tdee = params["tdee"]
        
            delta_w = delta_weight(tdci, tdee)
            new_weight = params["weight_history"][-1] + delta_w
        
            params["phases_history"].append(new_phase)
            params["weight_history"].append(new_weight)
        
            params["tdci"] = new_tdci
            params["tdee"] = new_tdee

        assert initial_weight < params["weight_history"][-1]




    def test_has_lost_weight_with_fat_loss_goal(self):
        def delta_weight(tdci, tdee, sigma=.6):
            return np.random.normal(0, sigma) + ((tdci - tdee) * 7) / 7000 


        nut = Nutripy()

        initial_weight = 80

        params = {
            "age": 30, 
            "height": 180, 
            "gender": Gender.MALE, 
            "activity": Activity.SEDENTARY, 
            "goal": Goal.LOSS,
            "weight_history": [initial_weight, 80, 80.5, 80],
            "phases_history":[Phase.LOSS, Phase.LOSS, Phase.LOSS, Phase.LOSS],
            "tdci": nut.get_daily_needs(30, 80, 180, Gender.MALE, Activity.SEDENTARY, Goal.LOSS),
            "tdee": nut.get_daily_needs(30, 80, 180, Gender.MALE, Activity.SEDENTARY, Goal.LOSS),
        }

    
        for i in range(20):
            state = get_new_state(**params)
        
            new_phase = state["phase"]
            new_tdci = state["tdci"]
            new_tdee = state["tdee"]
            
            tdci = params["tdci"]
            tdee = params["tdee"]
        
            delta_w = delta_weight(tdci, tdee)
            new_weight = params["weight_history"][-1] + delta_w
        
            params["phases_history"].append(new_phase)
            params["weight_history"].append(new_weight)
        
            params["tdci"] = new_tdci
            params["tdee"] = new_tdee

        assert initial_weight > params["weight_history"][-1]


    def test_maintainance_goal_raises_not_implemented_error(self):
        def delta_weight(tdci, tdee, sigma=.6):
            return np.random.normal(0, sigma) + ((tdci - tdee) * 7) / 7000 


        nut = Nutripy()

        initial_weight = 80

        params = {
            "age": 30, 
            "height": 180, 
            "gender": Gender.MALE, 
            "activity": Activity.SEDENTARY, 
            "goal": Goal.MAINTAIN,
            "weight_history": [initial_weight, 80, 80.5, 80],
            "phases_history":[Phase.MAINTAINANCE, Phase.MAINTAINANCE, Phase.MAINTAINANCE, Phase.MAINTAINANCE],
            "tdci": nut.get_daily_needs(30, 80, 180, Gender.MALE, Activity.SEDENTARY, Goal.MAINTAIN),
            "tdee": nut.get_daily_needs(30, 80, 180, Gender.MALE, Activity.SEDENTARY, Goal.MAINTAIN),
        }

        try:
            for i in range(20):
                state = get_new_state(**params)
        
                new_phase = state["phase"]
                new_tdci = state["tdci"]
                new_tdee = state["tdee"]
            
                tdci = params["tdci"]
                tdee = params["tdee"]
        
                delta_w = delta_weight(tdci, tdee)
                new_weight = params["weight_history"][-1] + delta_w
        
                params["phases_history"].append(new_phase)
                params["weight_history"].append(new_weight)
        
                params["tdci"] = new_tdci
                params["tdee"] = new_tdee

                raise Exception
        except NotImplementedError:
            pass




        
if __name__ == '__main__':
    unittest.main()
    
