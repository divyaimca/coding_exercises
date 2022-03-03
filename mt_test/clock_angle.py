from time import time
import math

def clock_angle(timeString, unit):
    print(timeString, unit)
    hour,minute = [int(x) for x in timeString.split(":")]
    # print(hour,minute)
    if  0 < hour > 24:
        print("Invalid Hour")
    
    if  0 < minute > 60:
        print("Invalid Minute")
    if minute == 60:
        minute = 0
    if hour == 12:
        hour = 0
    if hour > 12:
        hour = hour -12

    min_angle = (hour * 60 + minute ) * .5 ##  12 hours = 360 degree, 1 hour = 30 degree, 1 min = 0.5 degrees
    hr_angle = minute * 6  ##   60 min == 360 degree, 1 min = 6 degree


    clock_angle = abs(hr_angle - min_angle)

    result = min(360 - clock_angle, clock_angle)


    
    if unit == "degrees":
        return int(result)
    elif unit == "radians":
        return round((result) * (math.pi/180),4)
    else:
        pass



print(clock_angle("09:30", "degrees"))
print(clock_angle("09:15", "radians"))
print(clock_angle("21:00", "degrees"))
