def add_time(start, duration, day=None):
    """Add a period of time to an initial moment.

    This function does not import any Python libraries and assumes that the
    start times are valid times. The minutes in the duration time will be a
    whole number less than 60, but the hour can be any whole number.

    Parameters
    ----------
    start : str
        a start time in the 12-hour clock format (ending in AM or PM).
    duration : str
        a duration time that indicates the number of hours and minutes.
    day : str
        a starting day of the week, case insensitive.
        default value : False

    Returns
    -------
    new_time : str
        time resultang from adding 'duration' to 'start' in the 12-hour
        clock format.
        If the result will be the next day, it should show (next day) after
        the time. If the result will be more than one day later, it should
        show (n days later) after the time, where "n" is the number of days
        later.
        If the function is given the optional starting day of the week
        parameter, then the output should display the day of the week of the
        result. The day of the week in the output should appear after the
        time and before the number of days later.
    """

    # Split data from inputs
    start_time, meridiem = start.split(" ")
    start_hour, start_minute = start_time.split(":")
    delta_hour, delta_minute = duration.split(":")
    # Convert start hour to 24 hs format
    start_hour = int(start_hour)
    if meridiem == "PM":
        start_hour += 12
        meridiem = "AM"
    # Cast data to integers
    start_minute = int(start_minute)
    delta_hour = int(delta_hour)
    delta_minute = int(delta_minute)

    # Calculate auxiliary quantities
    addition_minutes = start_minute + delta_minute
    final_minutes = addition_minutes % 60
    final_hours = start_hour + delta_hour + addition_minutes // 60
    extra_days = final_hours // 24
    final_hour = final_hours % 12
    change_meridiem = (final_hours % 24) // 12

    # Correct 0 hour to 12
    if final_hour == 0:
        final_hour = 12

    # Perform change of meridiem
    if change_meridiem == 0:
        final_meridiem = "AM"
    else:
        if meridiem == "AM":
            final_meridiem = "PM"
        else:
            final_meridiem = "AM"

    # Construct final and conditiona annotaions
    if day is None:
        annotation = ""
    else:
        day = day.capitalize()
        # Dictionary containing encoding for days of the week
        week_encoding = {
            "Monday": 0,
            "Tuesday": 1,
            "Wednesday": 2,
            "Thursday": 3,
            "Friday": 4,
            "Saturday": 5,
            "Sunday": 6,
        }
        # Dictionary with decoding key
        week_decoding = {value: key for key, value in week_encoding.items()}
        # Calculate final day of the week
        first_day = week_encoding[day]
        last_day = (first_day + extra_days) % 7
        last_day = week_decoding[last_day]
        annotation = f", {last_day}"

    if extra_days == 1:
        annotation += " (next day)"
    elif extra_days > 1:
        annotation += f" ({extra_days} days later)"

    # Construct output
    new_hour = f"{final_hour}:{final_minutes:02d}"
    new_time = f"{new_hour} {final_meridiem:s}{annotation}"

    return new_time
