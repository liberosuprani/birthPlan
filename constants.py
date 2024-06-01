#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 76
# 62220 Libero Suprani
# 62238 Afonso Paulo


import dateTime
import sys

# Value for weekly pause in the output schedule
WKL_PAUSE = "weekly leave"


# In a file:
# Number of header's lines
NUM_HEADER_LINES = 7


# In a doctor's list:
# Index of the element with the doctor's name
DOCT_NAME_IDX = 0
# Index of the element with the doctor's category
DOCT_CATEGORY_IDX = 1
# Index of the element with the doctor's time of last birth
DOCT_LAST_BIRTH_IDX = 2
# Index of the element with the doctor's minutes since the beggining of the day
DOCT_BIRTHS_MINUTES_IDX = 3
# Index of the element with the doctor's time since his last weekly rest
DOCT_TIME_SINCE_REST_IDX = 4
 

# In a mother's list:
# Index of the element with the mother's name
MOTH_NAME_IDX = 0
# Index of the element with the mother's age
MOTH_AGE_IDX = 1
# Index of the element with the mother's bracelet
MOTH_BRACELET_IDX = 2
# Index of the element with the mother's risk of birth
MOTH_RISK_IDX = 3

# In a requests' list:
# Index of the element with the request's time
SCHED_TIME_IDX = 0
# Index of the element with the request's assigned mother 
SCHED_MOTH_IDX = 1
# Index of the element with the request's assigned doctor
SCHED_DOCT_IDX = 2

# Time of the current request
CURRENT_TIME = dateTime.toTotalIntMinutes(sys.argv[3][-9:-4])

# Length of a birth in minutes
BIRTH_LENGTH_MINUTES = 20

# Hospital closing time (20h) in minutes
HOSP_CLOSING_TIME_MINUTES = 1200

FILE_DOCT_HEADER = f"""Organization:\nSmartH\nHour:\n{sys.argv[3][-9:-4]}\nDay:\n\
{dateTime.currentDay(sys.argv[3])}\nDoctors:\n"""

FILE_SCHED_HEADER = f"""Organization:\nSmartH\nHour:\n{sys.argv[3][-9:-4]}\nDay:\n\
{dateTime.currentDay(sys.argv[3])}\nSchedule:\n"""