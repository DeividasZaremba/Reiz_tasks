def get_angle(hours, minutes):
    if hours < 0 or hours >= 24:
        return 'Invalid hours input'
    elif hours > 12:
        hours -= 12
    hours_angle = (hours + minutes / 60) * 30

    if minutes < 0 or minutes >= 60:
        return 'Invalid minutes input'
    else:
        minute_angle = minutes * 6

    angle_diff = abs(hours_angle - minute_angle)
    return round(min(360 - angle_diff, angle_diff), 1)

if __name__ == '__main__':
    hours = int(input('Enter hours: '))
    minutes = int(input('Enter minutes: '))
    print(f'Lesser angle between hours and minutes arrow is {get_angle(hours, minutes)}°')