#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 76
# 62220 Libero Suprani
# 62238 Afonso Paulo

import sys
import infoFromFiles
import planning
from constants import *
import infoToFiles

def plan(doctorsFileName, scheduleFileName, requestsFileName):
    """
    Runs the birthPlan application.

    Requires:
    doctorsFileName is a str with the name of a .txt file containing a list
    of doctors at date d and time t, organized as in the examples provided;
    scheduleFileName is a str with the name of a .txt file containing a list
    of birth assistances assigned to doctors at date d and time t, as in the examples provided;
    requestsFileName is a str with the name of a .txt file containing a list
    of cruises requested at date d and time t+30mins;
    Ensures:
    writing of two .txt files containing the updated list of doctors assigned
    to mothers and the updated list of birth assistances, according to 
    the requirements in the general specifications provided (omitted here for 
    the sake of readability);
    these two output files are named, respectively, doctorsXXhYY.txt and
    scheduleXXhYY.txt, where XXhYY represents the time 30 minutes
    after the time t indicated in the files doctorsFileName,
    scheduleFileName and requestsFileName, and are written in the same directory
    of the latter.
    """
    
    doctorsList = infoFromFiles.readDoctorsFile(doctorsFileName)
    requestsList = infoFromFiles.readRequestsFile(requestsFileName)
    schedulesList = infoFromFiles.readScheduleFile(scheduleFileName)

    planning.sortDoctors(doctorsList)
    planning.sortRequests(requestsList)
    
    updatedSchedule = planning.updateSchedule(doctorsList, requestsList, schedulesList, CURRENT_TIME)     

    infoToFiles.writeScheduleFile(updatedSchedule, FILE_SCHED_HEADER, f"schedule{sys.argv[3][-9:-4]}.txt")
    infoToFiles.writeDoctorsFile(doctorsList, FILE_DOCT_HEADER, f"doctors{sys.argv[3][-9:-4]}.txt")


plan(sys.argv[1], sys.argv[2], sys.argv[3])