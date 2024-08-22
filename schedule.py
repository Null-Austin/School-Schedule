file = open('schedule.txt', 'r')
schedule = file.read()
file.close
file1 = open('timed.txt')
td=int(file1.readlines()[1])
file1.close()

import time
from datetime import datetime

currentDateAndTime = datetime.now()
def get_times():
    lines = schedule.splitlines()[1:]  # get all text except the first line
    num_lines = len(lines)  # how many lines there are
    index = 0  # start with the first line
    time_list = []

    while index < num_lines:
        first_word = lines[index].split(' ', 1)[1]  # get the value of the first word (0)
        time_list.append(first_word)
        index += 1

    return time_list
def get_clases():
    lines = schedule.splitlines()[1:]  # get all text except the first line
    num_lines = len(lines)  # how many lines there are
    index = 0  # start with the first line
    time_list = []

    while index < num_lines:
        first_word = lines[index].split(' ', 1)[0]  # get the value of the first word (0)
        time_list.append(first_word)
        index += 1

    return time_list
def split_times(time):
    return([time.replace('-',' ').split(' ', 1)[1],time.replace('-',' ').split(' ', 1)[0]][::-1])
def currenttime():
    clock = datetime.now()
    a=str(currentDateAndTime.minute)
    if len(a) == 1:
        a="0"+a
    #return(str(currentDateAndTime.hour+td)+':'+a)
    return("10:34")

ClassTimes = get_times()
ClassSchedule = get_clases()
ctime = currenttime()
x=0
while(True):
    print(x)
    if split_times(ClassTimes[x])[0]<=ctime:
        print("ctime is bigger")
        while(True):
            x+=1
            print(x)
            if split_times(ClassTimes[x])[0]<=ctime:
                print("classtime is bigger")
                x-=1
                break
            continue
        continue
    x+=1
    continue
print(ClassSchedule[x])