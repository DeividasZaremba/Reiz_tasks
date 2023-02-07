def get_angle(hours, minutes):
    if hours < 0 or hours >= 24: # here we can accept hours input from 0 to 23
        return 'Invalid hours input'
    elif hours >= 12: # if hours is over 12, we convert to 12-hour format
        hours -= 12
    hours_angle = (hours + minutes / 60) * 30 # each hour covers 30° (360/12)

    if minutes < 0 or minutes >= 60: # here we can accept minutes input from 0 to 59
        return 'Invalid minutes input'
    else:
        minute_angle = minutes * 6 # each minute covers 6° (360 / 60)

    angle_diff = abs(hours_angle - minute_angle) # we find the difference in angle and convert to absolute
    return round(min(360 - angle_diff, angle_diff), 1) # we find lesser angle by returning smaller angle

if __name__ == '__main__':
    hours = int(input('Enter hours: '))
    minutes = int(input('Enter minutes: '))
    print(f'Lesser angle between hours and minutes arrow is {get_angle(hours, minutes)}°')