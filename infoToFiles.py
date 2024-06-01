#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 76
# 62220 Libero Suprani
# 62238 Afonso Paulo


from constants import *

def writeScheduleFile(sched, header, fileName):
    """
    Writes a collection of scheduled birth assistances into a file.

    Requires:
    - sched is a list with the structure as in the output of
    planning.updateSchedule representing the cruises assigned;
    - header is a string with a header, as in the examples provided in 
    the general specification (omitted here for the sake of readability);
    - fileName is a str with the name of a .txt file.

    Ensures:
    writing of file named fileName representing the birth assistances in schedule,
    one per line, as organized in the examples provided
    in the general specification (omitted here for the sake of readability); 
    the lines in this file keeps the ordering top to bottom of 
    the assistances as ordered head to tail in sched.
    """

    finalString = header
    data = ""

    for s in sched:
        s[SCHED_TIME_IDX] = dateTime.fromTotalIntMinutes(s[SCHED_TIME_IDX])
        data += f"{s[SCHED_TIME_IDX]}, {s[SCHED_MOTH_IDX]}, {s[SCHED_DOCT_IDX]}\n"
        
    finalString += data
    with open(fileName, "w") as f:
        f.write(finalString)


def writeDoctorsFile(doctors, header, fileName):
    """
    Writes a collection of doctors into a file.

    Requires:
    - doctors is a list of lists, each containing the infos from a doctor;
    - header is a string with a header, as in the examples provided in 
    the general specification (omitted here for the sake of readability);
    - fileName is a str with the name of a .txt file.

    Ensures:
    writing of file named fileName representing the doctors,
    one per line, as organized in the examples provided
    in the general specification (omitted here for the sake of readability); 
    """

    doctors.sort(key = lambda d : d[DOCT_NAME_IDX].lower())

    finalString = header
    data = ""

    for d in doctors:
        d[DOCT_CATEGORY_IDX] = str(d[DOCT_CATEGORY_IDX])
        d[DOCT_LAST_BIRTH_IDX] = dateTime.fromTotalIntMinutes(d[DOCT_LAST_BIRTH_IDX]) \
            if d[DOCT_LAST_BIRTH_IDX] != -1 else WKL_PAUSE

        d[DOCT_BIRTHS_MINUTES_IDX] = str(d[DOCT_BIRTHS_MINUTES_IDX])
        d[DOCT_TIME_SINCE_REST_IDX] = dateTime.fromTotalIntMinutes(d[DOCT_TIME_SINCE_REST_IDX])

        data += f"{d[DOCT_NAME_IDX]}, {d[DOCT_CATEGORY_IDX]}, {d[DOCT_LAST_BIRTH_IDX]}, \
{d[DOCT_BIRTHS_MINUTES_IDX]}, {d[DOCT_TIME_SINCE_REST_IDX]}\n"
        
    finalString += data
    with open(fileName, "w") as f:
        f.write(finalString)