from datetime import datetime
from operator import itemgetter
from collections import OrderedDict

#parse the input
logentries = {}
with open(r'C:\Users\jeremymill\Documents\AoC2018\4\input.txt') as f:
    for line in f:
        line = line.replace('[', '').replace(']', '').split(' ')
        dt = datetime.strptime("{} {}".format(line[0], line[1]), '%Y-%m-%d %H:%M')
        logentries[dt] = line
#convert to a sorted list
logentries = OrderedDict(sorted(logentries.items()))
#loop variables. Guard Sleeptime is the array of midnight minutes
guard_sleeptime = {}
#guard_totaltime is the total # of minutes slept
guard_totaltime = {}
#track the current guard and what time they fell asleep
current_guard = None
AsleepTime = None
#for the ordered iteration of legentries...
for logtime, line in logentries.items():    
    #if a guard is begining a shift:
    if line[2].startswith('G'):
        gid = int(line[3].replace('#', ''))
        current_guard = gid
        if gid not in guard_sleeptime:
            guard_sleeptime[gid] = [0]*60
            guard_totaltime[gid] = 0
    #if a guard is 'falling asleep'
    if line[2].startswith('f'):
        AsleepTime = logtime
    #if a guard is 'waking up'
    if line[2].startswith('w'):
        #adjust minute total
        for minute in range(AsleepTime.minute, logtime.minute):
            guard_sleeptime[current_guard][minute] += 1
        #adjust the complete total
        guard_totaltime[current_guard] += (logtime.minute - AsleepTime.minute)
        AsleepTime = None
#find the guard with the most sleep time
maxguard = max(guard_totaltime.items(), key=itemgetter(1))[0]
#find the minute with the max number of sleep minutes
maxhour = guard_sleeptime[maxguard].index(max(guard_sleeptime[maxguard]))
print("part 1:")
print(maxguard)
print(maxhour)
print(maxguard * maxhour)
print("part 2:") #last wrong: 57764
current_maxguard = None
current_maxindex = None
current_maxvalue = None
for gid, sleeptime in guard_sleeptime.items():
    max_minute_index = sleeptime.index(max(sleeptime))
    max_minute_value = sleeptime[max_minute_index]
    if current_maxindex is None or max_minute_value > current_maxvalue:
        current_maxguard = gid
        current_maxvalue = max_minute_value
        current_maxindex = max_minute_index
print(current_maxguard)
print(current_maxindex)
print(current_maxguard * current_maxindex)
