# Time Conversion Function

def timeConversion(seconds):
    if not isinstance(seconds, int):
        return 'Input must be an integer.'

    if seconds < 0 or seconds >= 86400:
        return 'Input must be between 0 and 86399.'

    hours = seconds // 3600
    minutes = seconds % 3600 // 60
    secs = seconds % 3600 % 60

    if hours < 12:
        timePeriod = "AM"
    else:
        timePeriod = "PM"

    checkZeroSeconds = hours % 12
    if checkZeroSeconds == 0:
        hours = 12

    return f'{hours} {minutes} {secs} {timePeriod}'

print(timeConversion(4122))
print(timeConversion(86400))
print(timeConversion(0))

