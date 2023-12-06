from datetime import datetime, timedelta

fromTz = ['EST', 'PST', 'CST', 'IST', 'JST']
toTZ = ['EST', 'PST', 'CST', 'IST', 'JST']

# create a map to indicate time zone behind/Ahead UTC
time_offsets = {
    'EST': -5,
    'PST': -8,
    'CST': -6,
    'IST': 5.5,
    'JST': 9,
}


def convertTimezone(date, fromTimezone, toTimezone):
    x = time_offsets[fromTimezone]
    y = time_offsets[toTimezone]

    # If x is negative, that means the timezone is behind UTC; otherwise, it is ahead
    # If x is positive, subtract it from UTC

    x = x * -1

    convertedTime = date.replace(tzinfo=None) + timedelta(hours=(x + y))

    # Handle the case where the converted time exceeds 12 AM
    if convertedTime.hour >= 24:
        convertedTime -= timedelta(days=1)

    return convertedTime

# Example usage:
fromTimezone = 'CST'
toTimezone = 'EST'
input_time = datetime(2023, 1, 1, 17, 0, 0)  # 5 PM EST

converted_time = convertTimezone(input_time, fromTimezone, toTimezone)

print(f"Converted time from {fromTimezone} to {toTimezone}: {converted_time.strftime('%Y-%m-%d %H:%M:%S')}")