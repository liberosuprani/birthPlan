#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 76
# 62220 Libero Suprani
# 62238 Afonso Paulo


import dateTime
from constants import *

def removeHeader(fileHandler):
    """
    Returns the content of a file without its header

    Requires:
    fileHandler is a file handler pointing to the file whose info is intended 

    Ensures:
    a str with all the info in the file without the header
    """
    lines = fileHandler.readlines()
    return lines[7:]


def checkFileConsistency(fileName):

    """
    Checks the consistency between a file name and its header

    Requires: 
    fileName is a str with the name of a .txt file (can be either a doctors, schedule or requests file)

    Ensures:
    raise of an exception in case there is an inconsistency between the file name and its header
    """

    with open(fileName, "r") as f:
        lines = f.readlines()
        headerType = lines[6].rstrip()[:-1]

        auxFileName = fileName

        if "requests" in auxFileName:
            auxFileName = auxFileName.replace("requests", "mothers")

        if auxFileName[:-9].lower() != headerType.lower():
            raise IOError(f"File head error: scope inconsistency between name and header in file <{fileName}>.") 
    

def readDoctorsFile(fileName):
    """
    Reads a file with a list of doctors into a collection.

    Requires:
    fileName is str with the name of a .txt file containing
    a list of doctors organized as in the examples provided in
    the general specification (omitted here for the sake of readability).
    Ensures:
    list of lists where each list corresponds to a doctor listed in
    the file fileName (with all the info pieces belonging to that doctor),
    following the order provided in the lines of the file.
    """

    checkFileConsistency(fileName)
   
    with open(fileName, "r") as f:
        inFile = removeHeader(f) 

        doctList = []
        for line in inFile:
            requestData = line.rstrip().split(", ")
            doctList.append(requestData)
    for d in doctList:
        d[DOCT_CATEGORY_IDX] = int(d[DOCT_CATEGORY_IDX])

        # doctor's last birth's time is converted into total minutes if he's not in weekly pause, else its -1
        d[DOCT_LAST_BIRTH_IDX] = dateTime.toTotalIntMinutes(d[DOCT_LAST_BIRTH_IDX]) \
            if d[DOCT_LAST_BIRTH_IDX] != WKL_PAUSE else -1
        
        d[DOCT_BIRTHS_MINUTES_IDX] = int(d[DOCT_BIRTHS_MINUTES_IDX])
        d[DOCT_TIME_SINCE_REST_IDX] = dateTime.toTotalIntMinutes(d[DOCT_TIME_SINCE_REST_IDX])

    return doctList


def readRequestsFile(fileName):
    """
    Reads a file with a list of requested assistances with a given file name into a collection.

    Requires:
    fileName is a str with the name of a .txt file containing
    a list of requests organized as in the examples provided in 
    the general specification 
    
    Ensures:
    list of lists where each list corresponds to a request listed in
    the file fileName (with all the info pieces belonging to that request),
    following the order provided in the lines of the file.
    """

    checkFileConsistency(fileName) 

    with open(fileName, "r") as f:
        inFile = removeHeader(f)       

        reqList = [] 
        for line in inFile:
            requestData = line.rstrip().split(", ")
            reqList.append(requestData)        

    for r in reqList:
        r[MOTH_AGE_IDX] = int(r[MOTH_AGE_IDX])

        # converts the bracelet colors into integers according to their importance 
        r[MOTH_BRACELET_IDX] = 1 if \
            r[MOTH_BRACELET_IDX] == "green" else (2 if r[MOTH_BRACELET_IDX] == "yellow" else 3)     
        # converts the risks into integers according to their level
        r[MOTH_RISK_IDX] = 1 if r[MOTH_RISK_IDX] == "low" else (2 if r[MOTH_RISK_IDX] == "medium" else 3)      

    return reqList


def readScheduleFile(fileName):
    """
    Reads a file with a list of scheduled assistances with a given file name into a collection.

    Requires:
    fileName is a str with the name of a .txt file containing
    a list of scheduled assistances organized as in the examples provided in
    the general specification

    Ensures:
    list of lists where each list corresponds to a scheduled assistance listed in
    the file fileName (with all the info pieces belonging to that assistance),
    following the order provided in the lines of the file.
    """

    checkFileConsistency(fileName) 

    with open(fileName, "r") as f:
        inFile = removeHeader(f)       

        schedList = [] 
        for line in inFile:
            requestData = line.rstrip().split(", ")
            schedList.append(requestData)
    for s in schedList:
        s[SCHED_TIME_IDX] = dateTime.toTotalIntMinutes(s[SCHED_TIME_IDX])

    return schedList