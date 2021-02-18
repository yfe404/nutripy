
# Table of Contents

1.  [Nutripy](#orgd1a3798)
    1.  [Installation](#orgb43f36b)
    2.  [Usage](#org1c5c1e1)
        1.  [Activity](#org6c4da6d)
        2.  [Goal](#orgb0579fe)


<a id="orgd1a3798"></a>

# Nutripy

[file:https://travis-ci.org/yafeunteun/nutripy.svg?branch=master](https://travis-ci.org/yafeunteun/nutripy) [![img](https://coveralls.io/repos/yafeunteun/nutripy/badge.svg)](https://coveralls.io/r/yafeunteun/nutripy)
[![img](https://api.codeclimate.com/v1/badges/2ccd4965df3cd83f13ad/maintainability.svg)](https://codeclimate.com/github/yafeunteun/nutripy/maintainability)


<a id="orgb43f36b"></a>

## Installation

    pip install nutripy


<a id="org1c5c1e1"></a>

## Usage

    from nutripy import Nutripy
    
    nut = Nutripy()
            
    age = 25
    weight = 60
    height = 180
    gender = "male"
    activity = "sedentary"
    goal = "loss_1000"
    daily_needs = nut.get_daily_needs(age, weight, height, gender, activity, goal)


<a id="org6c4da6d"></a>

### Activity

The parameter **activity** can take several values described in this section.

-   `sedentary`: little or no exercice
-   `lightly_active`: exercice/sports 1-3 times/week
-   `moderately_active`: exercice/sports 3-5 times/week
-   `very_active`: exercice/sports 6-7 times/week
-   `extra_active`: very hard exercice/sports or physical job


<a id="orgb0579fe"></a>

### Goal

The parameter **goal** can take several values described in this section.

-   `loss_1000`: lose 1 kg per week
-   `loss_500`: lose 0.5 kg per week
-   `maintain`: maintain your weight
-   `gain_500`: gain 0.5 kg per week
-   `gain_1000`: gain 1 kg per week

