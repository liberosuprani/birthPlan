#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 76
# 62220 Libero Suprani
# 62238 Afonso Paulo


def currentDay(fileName):
    """
    Reads a file and returns the current day 

    Requires:
    fileName is a str with the name of a .txt file (can be either a doctors, schedule or requests file)

    Ensures:
    a str with the date in the format DD:MM:YYYY
    """
    with open(fileName, "r") as f:
        lines = f.readlines()
        date = lines[5].rstrip()
        return date


def hourToInt(time):
    """
    Returns an int with the hours from a string in the format HHhMM

    Requires: time is a str with a time in the format HHhMM

    Ensures: int with amount of hours in that time
    """
    t = time.split("h")
    return int(t[0])


def minutesToInt(time):
    """
    Returns an int with the minutes from a string in the format HHhMM

    Requires: time is a str with a time in the format HHhMM

    Ensures: int with amount of minutes in that time
    """
    t = time.split("h")
    return int(t[1])


def intToTime(hour, minutes):
    """
    Returns an str in the format HHhMM, from a given amount of hour and minutes 

    Requires: hour is an int with the hours
    minutes is an int with the minutes

    Ensures: str in the format HHhMM
    """
    h = str(hour)
    m = str(minutes)

    if hour < 10:
        h = "0" + h

    if minutes < 10:
        m = "0" + m

    return h + "h" + m


def toTotalIntMinutes(time): 
    '''
    Converts a time in the format "HHhMM" into an integer corresponding to the amount of minutes in that time 
    (total minutes from the amount of hours + minutes)

    Requires: time is a str in the format "HHhMM"
    
    Ensures: An int corresponding to the total amount of minutes in that time
    '''
    
    return hourToInt(time)*60 + minutesToInt(time)


def fromTotalIntMinutes(minutes):
    """
    Converts an amount of minutes into a str in the format HHhMM

    Requires: minutes is an int, corresponding to the amount of minutes

    Ensures: a str in the format HHhMM, which is a conversion from the minutes given into a time
    """
    hours = 0

    while minutes >= 60:
        hours += 1
        minutes -= 60

    return intToTime(hours, minutes)