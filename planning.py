#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 76
# 62220 Libero Suprani
# 62238 Afonso Paulo


from operator import itemgetter
from constants import *
import copy

def sortDoctors(listOfDoctors): 
    """
    Sorts a list of lists corresponding to the infos of the doctors, 
    according to the order provided in the general specification

    Requires: listOfDoctors is a list of lists, each of them containing infos from a doctor

    Ensures: sorting of the listOfDoctors
    """

    listOfDoctors.sort(key = lambda d : d[DOCT_NAME_IDX].lower())       # sorts first by name (least significant key) 

    # sorts by time of last birth, in case of a tie sorts by categories reversed, then etc
    # If a doctor has already taken his daily pause, 
    # key = -d[DOCT_BIRTHS_MINUTES_IDX] else its the time left until his pause
    listOfDoctors.sort(key = lambda d : (d[DOCT_LAST_BIRTH_IDX], -d[DOCT_CATEGORY_IDX], \
    (-(240-d[DOCT_BIRTHS_MINUTES_IDX]) if d[DOCT_BIRTHS_MINUTES_IDX] < 240 \
        else -d[DOCT_BIRTHS_MINUTES_IDX]), -(2400-d[DOCT_TIME_SINCE_REST_IDX])))
                                                                                                                                                            

def sortRequests(listOfRequests): 
    """ of the requests, 
    according to the order provided in the general specification

    Requires: listOfRequests is a list of lists, each of them containing infos from a request (a mother)

    Ensures: sorting of the listOfRequests
    """

    listOfRequests.sort(key = lambda mother: mother[MOTH_NAME_IDX].lower())
    listOfRequests.sort(key = itemgetter(MOTH_RISK_IDX, MOTH_BRACELET_IDX, MOTH_AGE_IDX), reverse=True)


def sortSchedule(listOfSchedules, listOfFailedSchedulesDict=[]):
    """
    Sorts a list of lists corresponding to the infos of the schedules, 
    according to the order provided in the general specification

    Requires: listOfSchedules is a list of lists, each of them containing infos from a schedule
    (optional) listOfFailedSchedulesDict is a list of dictionaries, each of them containing the infos from a failed schedule

    Ensures: sorting of the listOfSchedules, with the inclusion of failed schedules (if any was given)
    """

    if len(listOfFailedSchedulesDict) < 1:      # if there are no failed schedules, simply sorts them
        listOfSchedules.sort(key = lambda s : (s[SCHED_TIME_IDX], s[SCHED_MOTH_IDX].lower()))
        
    else:
        # in case of failed schedules, we must include them by the name of the first mother 
        # (failed schedules being sorted themselves by the order of priority of the mothers). 
        # Also, the failed schedules have to appear together
        listOfFailedSchedulesDict.sort(key = lambda s : s["name"].lower())

        # sorts the failed scheds according to the priority of the mothers
        listOfFailedSchedulesDict.sort(key = itemgetter("risk", "bracelet", "age"), reverse=True)   

        # creates a list of the failed scheds 
        # (each failed sched is a list with time, name of mother, and the msg to be shown)
        listOfFailedSchedulesList = [[x["time"], x["name"], x["msg"]] for x in listOfFailedSchedulesDict]   

        # gets the first failed sched, appends and sorts it into the list of all schedules
        firstFailedSchedule = copy.copy(listOfFailedSchedulesList[0])   
        listOfSchedules.append(firstFailedSchedule)
        listOfSchedules.sort(key = lambda s : (s[SCHED_TIME_IDX], s[SCHED_MOTH_IDX].lower()))

        # if there is more than one failed sched, include the other ones right after the first into the list of all schedules
        if len(listOfFailedSchedulesList) > 1:
            for i in range(1, len(listOfFailedSchedulesList)):
                listOfSchedules.insert(listOfSchedules.index([firstFailedSchedule]+i), copy.listOfFailedSchedulesList[i]) 





def updateSchedule(doctors, requests, previousSched, nextTime):
    """
    Update birth assistance schedule assigning the given birth assistance requested
    to the given doctors, taking into account a previous schedule.

    Requires:
    doctors is a list of lists with the structure as in the output of
    infoFromFiles.readDoctorsFile concerning the time of previous schedule;
    requests is a list of lists with the structure as in the output of 
    infoFromFile.readRequestsFile concerning the current update time;
    previousSched is a list of lists with the structure as in the output of
    infoFromFiles.readScheduleFile concerning the previous update time;
    nextTime is a string in the format HHhMM with the time of the next schedule
    Ensures:
    a list of birth assistances, representing the schedule updated at
    the current update time (= previous update time + 30 minutes),
    assigned according to the conditions indicated in the general specification
    of the project (omitted here for the sake of readability).
    """
    failedSchedules = []
    currentSchedules = copy.deepcopy(previousSched)

    for s in previousSched:
        if s[SCHED_TIME_IDX] <= nextTime:
            currentSchedules.remove(s)

    for mother in requests:
        isHighRisk = True if mother[MOTH_RISK_IDX] == 3 else False

        foundDoctor = False
        i = 0
        while foundDoctor == False and i < len(doctors):
            doctor = doctors[i]

            if (doctor[DOCT_LAST_BIRTH_IDX] != -1) and \
                (doctor[DOCT_LAST_BIRTH_IDX] + BIRTH_LENGTH_MINUTES <= HOSP_CLOSING_TIME_MINUTES) and \
                ((not isHighRisk) or (isHighRisk and doctor[DOCT_CATEGORY_IDX] >= 2)):

                foundDoctor = True

                newSchedule = [
                    doctor[DOCT_LAST_BIRTH_IDX] if doctor[DOCT_LAST_BIRTH_IDX] > nextTime else nextTime,
                    mother[MOTH_NAME_IDX],
                    doctor[DOCT_NAME_IDX],
                ]

                # if the doctor's amount of minutes in that day was already over 240 (4 hours) 
                isOverLimitTime = True if doctor[DOCT_BIRTHS_MINUTES_IDX] >= 240 else False      

                # in case the doctor´s last birth ends after the new time, add to it
                if doctor[DOCT_LAST_BIRTH_IDX] > nextTime:
                    doctor[DOCT_LAST_BIRTH_IDX] += BIRTH_LENGTH_MINUTES     
                # else, it will now be the next time plus 20  
                else:                                                       
                    doctor[DOCT_LAST_BIRTH_IDX] = nextTime + BIRTH_LENGTH_MINUTES   

                doctor[DOCT_BIRTHS_MINUTES_IDX] += BIRTH_LENGTH_MINUTES
                doctor[DOCT_TIME_SINCE_REST_IDX] += BIRTH_LENGTH_MINUTES

                # if time since last rest is greater than 2400 minutes (40 hours), then set it to -1 (weekly leave)
                if doctor[DOCT_TIME_SINCE_REST_IDX] >= 2400:    
                    doctor[DOCT_LAST_BIRTH_IDX] = -1

                # if doctor's amount of minutes is over 240 (4 hours) and it wasnt's already before 
                # (so it only gives him a single pause in that day)
                if doctor[DOCT_BIRTHS_MINUTES_IDX] >= 240 and isOverLimitTime == False:     
                    doctor[DOCT_LAST_BIRTH_IDX] += 60

                sortDoctors(doctors)

                currentSchedules.append(newSchedule)
            i += 1

        # if after the whole loop it did not find a doctor, then its a failed schedule
        if foundDoctor == False:         
            failedSchedule = {
                "time" : nextTime,
                "name" : mother[MOTH_NAME_IDX],
                "risk" : mother[MOTH_RISK_IDX],
                "bracelet" : mother[MOTH_BRACELET_IDX],
                "age" : mother[MOTH_AGE_IDX],
                "msg" : "redirected to other network",
            }
            failedSchedules.append(failedSchedule)

    sortSchedule(currentSchedules, failedSchedules)
    return currentSchedules