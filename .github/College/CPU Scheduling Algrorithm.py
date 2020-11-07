def FCFS(NumOfProcesses, BurstTimeList):
    waitingTime = 0
    GanttChart = []
    for i in range(0, NumOfProcesses):
        for j in range(0, BurstTimeList[i][1]):
            GanttChart.append(BurstTimeList[i][0])
        waitingTime += BurstTimeList[i][1]*(NumOfProcesses-i-1)
    waitingTime /= NumOfProcesses
    return GanttChart, waitingTime

def SJFNonPreemptive(NumOfProcesses, BurstTimeList):
    swapList = []
    for i in range(0, NumOfProcesses):
        c = i
        for j in range(i+1, NumOfProcesses):
            if BurstTimeList[j][1]<BurstTimeList[c][1]:
                c = j
        if c != i:
            swapList         = BurstTimeList[c]
            BurstTimeList[c] = BurstTimeList[i]
            BurstTimeList[i] = swapList
    return FCFS(NumOfProcesses, BurstTimeList)

def SJFPreemptive(NumOfProcesses, BurstTimeList):
    ArrivalTime = []
    ArrivalStatus = []
    waitingTime = 0
    totalTime = 0
    GanttChart = []
    for i in range(0, NumOfProcesses):
        ArrivalTime.append(BurstTimeList[i][2])
        ArrivalStatus.append(False)
        waitingTime -= (BurstTimeList[i][1]+BurstTimeList[i][2])
        totalTime += BurstTimeList[i][1]
    smallestIndex = 0
    smallestValue = totalTime
    for i in range(0, totalTime):
        smallestValue = totalTime
        for j in range(0, NumOfProcesses):
            if i == ArrivalTime[j]:
                ArrivalStatus[j] = True
        for j in range(0, NumOfProcesses):
            if ArrivalStatus[j] and BurstTimeList[j][1] < smallestValue and BurstTimeList[j][1] != 0:
                smallestValue = BurstTimeList[j][1]
                smallestIndex = j
        GanttChart.append(smallestIndex+1)
        BurstTimeList[smallestIndex][1] -= 1
        if BurstTimeList[smallestIndex][1] == 0:
            waitingTime += (i+1)
    waitingTime /= NumOfProcesses
    return GanttChart, waitingTime

def PriorityNonPreemptive(NumOfProcesses, BurstTimeList):
    swapList = []
    for i in range(0, NumOfProcesses):
        c = i
        for j in range(i+1, NumOfProcesses):
            if BurstTimeList[j][2]<BurstTimeList[c][2]:
                c = j
        if c != i:
            swapList         = BurstTimeList[c]
            BurstTimeList[c] = BurstTimeList[i]
            BurstTimeList[i] = swapList
    return FCFS(NumOfProcesses, BurstTimeList)

def PriorityPreemptive(NumOfProcesses, BurstTimeList):
    ArrivalTime = []
    ArrivalStatus = []
    waitingTime = 0
    totalTime = 0
    GanttChart = []
    for i in range(0, NumOfProcesses):
        ArrivalTime.append(BurstTimeList[i][2])
        ArrivalStatus.append(False)
        waitingTime -= (BurstTimeList[i][1]+BurstTimeList[i][2])
        totalTime += BurstTimeList[i][1]
    smallestIndex = 0
    smallestValue = 30
    for i in range(0, totalTime):
        smallestValue = totalTime
        for j in range(0, NumOfProcesses):
            if i == ArrivalTime[j]:
                ArrivalStatus[j] = True
        for j in range(0, NumOfProcesses):
            if ArrivalStatus[j] and BurstTimeList[j][3] < smallestValue and BurstTimeList[j][1] != 0:
                smallestValue = BurstTimeList[j][3]
                smallestIndex = j
        GanttChart.append(smallestIndex+1)
        BurstTimeList[smallestIndex][1] -= 1
        if BurstTimeList[smallestIndex][1] == 0:
            waitingTime += (i+1)
    waitingTime /= NumOfProcesses
    return GanttChart, waitingTime

def RoundRobin(NumOfProcesses, BurstTimeList, TimeQuantum):
    waitingTime = 0
    GanttChart = []
    myLen = 0
    for i in range(0, NumOfProcesses):
        waitingTime -= BurstTimeList[i][1]
    i = 0
    NumOfZeroes = 0
    while True:
        if(BurstTimeList[i][1]==0):
            i = (i+1)%NumOfProcesses
            continue
        if BurstTimeList[i][1]>TimeQuantum:
            BurstTimeList[i][1] -= TimeQuantum
            myLen += TimeQuantum
            for j in range(0, TimeQuantum):
                GanttChart.append(BurstTimeList[i][0])
        else:
            myLen += BurstTimeList[i][1]
            for j in range(0, BurstTimeList[i][1]):
                GanttChart.append(BurstTimeList[i][0])
            BurstTimeList[i][1] = 0
            NumOfZeroes += 1
            waitingTime += myLen
        if NumOfZeroes == NumOfProcesses:
            break
        i = (i+1)%NumOfProcesses
    waitingTime /= NumOfProcesses
    return GanttChart, waitingTime


def EnterBurstTime(BurstTimeList, NumOfProcesses):
    for i in range(0, NumOfProcesses):
        x = int(input("Enter the burst time for process "+str(i+1)+" : "))
        BurstTimeList[i].append(x)

def EnterArrivalTime(BurstTimeList, NumOfProcesses):
    for i in range(0, NumOfProcesses):
        x = int(input("Enter the arrival time for process "+str(i+1)+" : "))
        BurstTimeList[i].append(x)

def EnterPriority(BurstTimeList, NumOfProcesses):
    for i in range(0, NumOfProcesses):
        x = int(input("Enter the priority for process "+str(i+1)+" : "))
        BurstTimeList[i].append(x)

def GanttOutput(GanttChart):
    firstLine = "|"
    aboveLine = "_"
    underLine = "‾"
    secondLine = "0"
    for i in range(0, len(GanttChart)):
        firstLine = firstLine + "P" + str(GanttChart[i]) + "|"
        if i<10:
            secondLine = secondLine + "  " + str((i+1))
        else:
            secondLine = secondLine + " " + str((i+1))
    for i in range(1, len(firstLine)):
        underLine += "‾"
        aboveLine += "_"
    return aboveLine + "\n" + firstLine + "\n" + underLine + "\n" + secondLine



while(1):
    print ("\n\nChoose the type of the scheduler:")
    print ("F  for FCFS")
    print ("S  for SJF non preemptive")
    print ("SP for SJF preemptive")
    print ("P  for priority non preemptive")
    print ("PP for priority preemptive")
    print ("RR for round robin")
    print ("Q  for Quit")
    scheduler = input()
    if scheduler == "Q" or scheduler == 'q':
        break
    NumOfProcesses = int(input("Enter the number of processes: "))
    BurstTimeList = []
    for i in range(0, NumOfProcesses):
        newList = []
        newList.append((i+1))
        BurstTimeList.append(newList)
    waitingTime = 0
    GanttChart = []
    if scheduler == 'F' or scheduler == 'f':
            EnterBurstTime(BurstTimeList, NumOfProcesses)
            GanttChart, waitingTime = FCFS(NumOfProcesses, BurstTimeList)
    elif scheduler == 'S' or scheduler == 's':
            EnterBurstTime(BurstTimeList, NumOfProcesses)
            GanttChart, waitingTime = SJFNonPreemptive(NumOfProcesses, BurstTimeList)
    elif scheduler == 'SP' or scheduler == 'sp':
            EnterBurstTime(BurstTimeList, NumOfProcesses)
            EnterArrivalTime(BurstTimeList, NumOfProcesses)
            GanttChart, waitingTime = SJFPreemptive(NumOfProcesses, BurstTimeList)
    elif scheduler == 'P' or scheduler == 'p':
            EnterBurstTime(BurstTimeList, NumOfProcesses)
            EnterPriority(BurstTimeList, NumOfProcesses)
            GanttChart, waitingTime = PriorityNonPreemptive(NumOfProcesses, BurstTimeList)
    elif scheduler == 'PP' or scheduler == 'pp':
            EnterBurstTime(BurstTimeList, NumOfProcesses)
            EnterArrivalTime(BurstTimeList, NumOfProcesses)
            EnterPriority(BurstTimeList, NumOfProcesses)
            GanttChart, waitingTime = PriorityPreemptive(NumOfProcesses, BurstTimeList)
    elif scheduler == 'RR' or scheduler == 'rr':
            EnterBurstTime(BurstTimeList, NumOfProcesses)
            TimeQuantum = int(input("Enter the time quantum: "))
            GanttChart, waitingTime = RoundRobin(NumOfProcesses, BurstTimeList, TimeQuantum)
    print("GanttChart :")
    print(GanttOutput(GanttChart))
    print("waiting time = ", waitingTime)
