
# Table of Contents

1.  [Nutripy](#orgcca8af6)
    1.  [Installation](#org7b34a71)
    2.  [Usage](#orgdb8aa60)
        1.  [Compute daily needs](#orgc931f04)
        2.  [Weight loss / mass gain management (work in progress)](#org07163db)


<a id="orgcca8af6"></a>

# Nutripy

[file:https://travis-ci.org/yafeunteun/nutripy.svg?branch=master](https://travis-ci.org/yafeunteun/nutripy) [![img](https://coveralls.io/repos/yafeunteun/nutripy/badge.svg)](https://coveralls.io/r/yafeunteun/nutripy)
[![img](https://api.codeclimate.com/v1/badges/2ccd4965df3cd83f13ad/maintainability.svg)](https://codeclimate.com/github/yafeunteun/nutripy/maintainability)


<a id="org7b34a71"></a>

## Installation

    pip install nutripy


<a id="orgdb8aa60"></a>

## Usage


<a id="orgc931f04"></a>

### Compute daily needs

    import nutripy
    from nutripy import Nutripy
    
    nut = Nutripy()
            
    age = 25
    weight = 60
    height = 180
    gender = nutripy.nutripy.Gender.MALE
    activity = nutripy.nutripy.Activity.SEDENTARY
    goal = nutripy.nutripy.Goal.GAIN
    daily_needs = nut.get_daily_needs(age, weight, height, gender, activity, goal)


<a id="org07163db"></a>

### Weight loss / mass gain management (work in progress)

The main feature of Nutripy is its ability to manage one's weight
loss and/or weight gain. 

**Work In Progress**

