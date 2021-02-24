from .nutripy import Nutripy, Goal, Gender, Activity
from .config import *

import numpy as np
from enum import Enum

from scipy.ndimage.filters import uniform_filter1d


def is_close(a, b, close=150):
    if abs(a - b) < close:
        return True
    return False


class Phase(Enum):
    LOSS = 0
    STOP = 1
    MAINTAINANCE = 2 
    GAIN = 3



def gain(x):
    if x > 0.5: 
        return 0
    if x <= 0.5:
        return CALORIES_STEP_SIZE

def maintain(x):
    if x > -0.5 and x < 0.5: 
        return 0
    if x > 0.5:
        return -CALORIES_STEP_SIZE
    if x < 0.5:
        return CALORIES_STEP_SIZE
    
def loss(x):
    if x < -0.5: 
        return 0
    if x > -0.5:
        return -CALORIES_STEP_SIZE



def get_new_state(age, height, gender, activity, goal, weight_history, phases_history, tdci, tdee):
    
    assert len(weight_history) == len(phases_history), \
    "weight history should have the same length as phase history"


    nut = Nutripy()

    delta_cal = 0

    new_weight = weight_history[-1]
    current_phase = phases_history[-1]
    
    duration = 1 # counts the number of weeks within the phase

    for i in range(1, len(phases_history)):
        if phases_history[-i-1] == current_phase:
            duration += 1
        else:
            break

    if goal == Goal.GAIN:
        if current_phase == Phase.GAIN and duration <= 16:
            new_phase = Phase.GAIN

        if current_phase == Phase.GAIN and duration > 16:
            new_phase = Phase.STOP
            duration = 1

    elif goal == Goal.LOSS:
        if current_phase == Phase.LOSS and duration <= 16:
            new_phase = Phase.LOSS

        if current_phase == Phase.LOSS and duration > 16:
            new_phase = Phase.STOP
            duration = 1

    else:
        raise NotImplementedError

    if current_phase == Phase.STOP:
        if is_close(tdee, tdci, close=200):
            new_phase = Phase.MAINTAINANCE
        else:
            new_phase = Phase.STOP
            #phases_history.append(new_phase)
            
    if current_phase == Phase.MAINTAINANCE:
            new_phase = Phase.MAINTAINANCE # todo: renew main Phase or do another goal
      
    print(current_phase)
    if new_phase == Phase.MAINTAINANCE:
        if len(weight_history) > 3:
            weight_derivative = np.gradient(weight_history)
            y = uniform_filter1d(weight_derivative, size=3)
            delta_cal = maintain(y[-1])

    if goal == Goal.GAIN:
        if new_phase == Phase.GAIN:
            if len(weight_history) > 3:
                weight_derivative = np.gradient(weight_history)
                y = uniform_filter1d(weight_derivative, size=3)
                delta_cal = gain(y[-1])
        if new_phase == Phase.STOP:
            if duration == 1:
                tdee = nut.get_daily_needs(age, new_weight, height, gender, activity, goal)
                print(tdee)

            if not is_close(tdee, tdci, close=200):
                delta_cal = -CALORIES_STEP_SIZE

    elif goal == Goal.LOSS:
        if new_phase == Phase.LOSS:
            if len(weight_history) > 3:
                weight_derivative = np.gradient(weight_history)
                y = uniform_filter1d(weight_derivative, size=3)
                delta_cal = loss(y[-1])
        if new_phase == Phase.STOP:
            if duration == 1:
                    tdee = nut.get_daily_needs(age, new_weight, height, gender, activity, goal)

            if not is_close(tdee, tdci, close=200):
                delta_cal = CALORIES_STEP_SIZE
    else:
        raise NotImplementedError


    return {
        "phase": new_phase,
        "tdci": tdci + delta_cal,
        "tdee": tdee
    }




if __name__ == "__main__":
    def delta_weight(tdci, tdee, sigma=.6):
        return np.random.normal(0, sigma) + ((tdci - tdee) * 7) / 7000 


    nut = Nutripy()

    params = {
    "age": 30, 
    "height": 180, 
    "gender": Gender.MALE, 
    "activity": Activity.SEDENTARY, 
    "goal": Goal.GAIN,
    "weight_history": [80, 80, 80.5, 80],
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
