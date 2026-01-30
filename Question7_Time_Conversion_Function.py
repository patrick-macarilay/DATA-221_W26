def time_conversion(seconds):
    if not isinstance(seconds, int):
        return 'Please enter an integer between 0 and 86400'
    if seconds < 0 or seconds >= 86400:
        return 'Please enter a valid amount between 0 and 86399'

    hours = seconds / 3600
    minutes = seconds % 3600 / 60
    seconds = seconds % 3600 % 60

    






print(time_conversion('ad'))
