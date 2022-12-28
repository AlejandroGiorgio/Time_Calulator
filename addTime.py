def add_time(starTime, addTime, day=0):
    dayCount = 0
    dayStamp = 0
    startTime = starTime.split(" ")
    startHndM = startTime[0]
    dayPeriod = startTime[1]
    addTime = addTime.split(":")
    addHour = int(addTime[0])
    addMInutes = int(addTime[1])
    weekday = {1: "monday", 2: "tuesday", 3: "wednesday",
               4: "thurdsday", 5: "friday", 6: "saturday", 7: "sunday"}
    halfDay = 0
    start = startHndM.split(":")
    hour = int(start[0])
    minutes = int(start[1])
    minutes += addMInutes
    hour += addHour

    if minutes >= 60:
        hour += 1
        minutes -= 60

    while hour >= 24:
        dayStamp += 1
        dayCount += 1
        hour -= 24

    if hour > 12:
        halfDay = 1
        hour -= 12
        if hour == 0:
            hour = 1

    if hour >= 12:
        if dayStamp == 1 and dayPeriod == "PM":
            dayCount += 1
            dayPeriod = "AM"
        if dayPeriod == "AM" and dayStamp == 0:
            dayPeriod = "PM"

    if not day == 0:
        day = day.lower()
        for key, value in weekday.items():
            if day == value:
                day = int(key)
        if dayPeriod == "PM" and halfDay == 1:
            dayCount += 1
            dayPeriod = "AM"
            halfDay -= 1
            if day > 7:
                day -= 7
        elif dayPeriod == "AM" and halfDay == 1:
            dayPeriod = "PM"
        day += (dayCount % 7)
        while day > 7:
            day -= 7
        for key, value in weekday.items():
            if day == key:
                day = value
                day = day.capitalize()
    else:
        if dayPeriod == "PM" and halfDay == 1:
            dayCount += 1
            if dayStamp == "1":
                dayCount += 1
            dayPeriod = "AM"
            halfDay -= 1
        elif dayPeriod == "AM" and halfDay == 1:
            dayPeriod = "PM"

    if len(str(minutes)) < 2:
        minutes = f"0{minutes}"

    if not day == 0:
        if dayCount == 0:
            return f"{hour}:{minutes} {dayPeriod}, {day}"
        elif dayCount == 1:
            return f"{hour}:{minutes} {dayPeriod}, {day} (next day)"
        else:
            return f"{hour}:{minutes} {dayPeriod}, {day} ({dayCount} days later)"
    else:
        if dayCount == 0:
            return f"{hour}:{minutes} {dayPeriod}"
        elif dayCount == 1:
            return f"{hour}:{minutes} {dayPeriod} (next day)"
        else:
            return f"{hour}:{minutes} {dayPeriod} ({dayCount} days later)"
