import math
import random


testArr = [
     {
          "id": 0,
          "arrivalTime": 0,
          "burstTime": 7,
          "priority": -1,
          "timeQuantum": -1
     },
       {
          "id":1,
          "arrivalTime": 2,
          "burstTime": 4,
          "priority": -1,
          "timeQuantum": -1
     },
       {
          "id": 2,
          "arrivalTime": 4,
          "burstTime": 1,
          "priority": -1,
          "timeQuantum": -1
     },
       {
          "id": 3,
          "arrivalTime": 5,
          "burstTime": 4,
          "priority": -1,
          "timeQuantum": -1
     },
]

testArrP = [
     {
          "id": 0,
          "arrivalTime": 0,
          "burstTime": 7,
          "priority": 3,
          "timeQuantum": -1
     },
       {
          "id":1,
          "arrivalTime": 2,
          "burstTime": 4,
          "priority": 2,
          "timeQuantum": -1
     },
       {
          "id": 2,
          "arrivalTime": 4,
          "burstTime": 1,
          "priority": 4,
          "timeQuantum": -1
     },
       {
          "id": 3,
          "arrivalTime": 5,
          "burstTime": 4,
          "priority": 1,
          "timeQuantum": -1
     },
]

testArrR = [
     {
          "id": 0,
          "arrivalTime": 0,
          "burstTime": 7,
          "priority": -1,
          "timeQuantum": 3
     },
       {
          "id":1,
          "arrivalTime": 2,
          "burstTime": 4,
          "priority": -1,
          "timeQuantum": 3
     },
       {
          "id": 2,
          "arrivalTime": 4,
          "burstTime": 1,
          "priority": -1,
          "timeQuantum": 3
     },

]
def initiateProcess(id, arrivalTime, burstTime, priority = -1, timeQuantum = -1):
    obj = {}
    obj["id"] = id
    obj["arrivalTime"] = arrivalTime
    obj["burstTime"] = burstTime
    obj["priority"] = priority
    obj["timeQuantum"] = timeQuantum
    return obj


def createProcess(str = ""):
     randID = math.floor(random.random() * 50)
     arrivalTime = math.floor(random.random() * 100)
     burstTime = math.floor(random.random() * 100)
     if (str == "priority"):
          priority = math.floor(random.random() * 20)
     else:
          priority = -1
     if (str == "round"):
          timeQuantum =  math.floor(random.random() * 10)
     else:
          timeQuantum = -1
     return initiateProcess(randID, arrivalTime, burstTime, priority, timeQuantum)


def sorter(key = "arrivalTime"):
    def sorter(e):
        return e[key]
    return sorter

def sorterSJF(key = "burstTime"):
    def sorter(e):
        return e[key]
    return sorter

def printTimeInstance(time, processID = ""):
     if processID != "":
        print("At time = " + str(time) +", Process ID of "  + str(processID) +" is running.")
     else:
         print("At time = " + str(time) +", CPU is doing nothing.")


def createGanttChart(type="FCFS", bursts=[]):
    time = 0

    # ---------------------------
    # FCFS (your original logic)
    # ---------------------------
    if type == "FCFS":
        bursts.sort(key=sorter("arrivalTime"))
        for obj in bursts:
            for _ in range(obj["burstTime"]):
                printTimeInstance(time, obj["id"])
                time += 1
        return

    # ---------------------------
    # SJF (Non-Preemptive)
    # ---------------------------
    elif type == "SJF":

        # sort by arrival time
        bursts.sort(key=sorter("arrivalTime"))

        n = len(bursts)
        completed = [False] * n     # track which processes are done
        done = 0

        while done < n:

            # get all processes that have arrived by current time
            available = [
                bursts[i] for i in range(n)
                if bursts[i]["arrivalTime"] <= time and not completed[i]
            ]

            if not available:
                # CPU is idle → jump forward
                time += 1
                continue

            # choose shortest burst time among arrived processes
            job = min(available, key=lambda p: p["burstTime"])

            # find index of job
            idx = bursts.index(job)

            # execute the job
            for _ in range(job["burstTime"]):
                printTimeInstance(time, job["id"])
                time += 1

            completed[idx] = True
            done += 1

     
def FCFS(bursts):
    time = 0
    arr = []
    bursts = sorted(bursts, key=lambda x: x["arrivalTime"])

    for p in bursts:
        while time < p["arrivalTime"]:
            time += 1  # CPU idle
        for _ in range(p["burstTime"]):
            printTimeInstance(time, p["id"])
            obj = {
                "id": p["id"],
                "time": time
            }
            arr.append(obj)
            time += 1

    return arr


def SJF_NonPreemptive(bursts):
    time = 0
    n = len(bursts)
    arr = []
    completed = [False] * n
    bursts = sorted(bursts, key=lambda x: x["arrivalTime"])  # stable

    done = 0
    while done < n:

        # processes that have arrived
        available = [
            bursts[i] for i in range(n)
            if bursts[i]["arrivalTime"] <= time and not completed[i]
        ]

        if not available:
            time += 1  # idle CPU
            continue

        # pick job with smallest burst time
        job = min(available, key=lambda p: p["burstTime"])
        idx = bursts.index(job)

        # execute fully (non-preemptive)
        for _ in range(job["burstTime"]):
            printTimeInstance(time, job["id"])

            time += 1

        completed[idx] = True
        done += 1


def SJF_Preemptive(bursts):  # SRTF
    time = 0
    n = len(bursts)
    arr = []
    bursts = sorted(bursts, key=lambda x: x["arrivalTime"])
    remaining = [p["burstTime"] for p in bursts]
    completed = 0

    while completed < n:

        available = [
            (i, bursts[i])
            for i in range(n)
            if bursts[i]["arrivalTime"] <= time and remaining[i] > 0
        ]

        if not available:
            time += 1
            continue

        # pick smallest remaining time
        idx, job = min(available, key=lambda x: remaining[x[0]])

        # execute for 1 time unit
        printTimeInstance(time, job["id"])
        remaining[idx] -= 1
        time += 1

        if remaining[idx] == 0:
            completed += 1



def Priority_Preemptive(bursts):
    time = 0
    n = len(bursts)
    arr = []
    bursts = sorted(bursts, key=lambda x: x["arrivalTime"])
    remaining = [p["burstTime"] for p in bursts]
    completed = 0

    while completed < n:

        available = [
            (i, bursts[i])
            for i in range(n)
            if bursts[i]["arrivalTime"] <= time and remaining[i] > 0
        ]

        if not available:
            time += 1
            continue

        # smallest priority number = highest priority
        idx, job = min(available, key=lambda x: x[1]["priority"])

        # execute 1 time unit
        printTimeInstance(time, job["id"])
        remaining[idx] -= 1
        time += 1

        if remaining[idx] == 0:
            completed += 1
       
          

def createGanttChart(algorithm, bursts):
    if algorithm == "FCFS":
        return FCFS(bursts)
    elif algorithm == "SJF":
        return SJF_NonPreemptive(bursts)
    elif algorithm == "SRTF":
         return SJF_Preemptive(bursts)
    elif algorithm == "PRIORITY_PREEMPTIVE":
         return Priority_Preemptive(bursts)
    else:
        raise ValueError("Unknown algorithm")


                

def createBurst(id, start, end):
     obj = {}
     obj["id"] = id
     obj["start"] = start
     obj["end"] = end
     return obj
     
     
def firstCome(processArray = testArr):
     # Tony's Job
     bursts = createGanttChart("FCFS", processArray)
     print("First Come First Serve")


print(firstCome(testArr))
def sjf(processArray = testArr):

     bursts =createGanttChart("SJF", processArray)
     print("Shortest Job First")
# sjf(testArr)

def srt(processArray = testArr):
     # Mohamed's Job

     bursts =createGanttChart("SRTF", processArray)
     print("Shortest Remaining Time")
def priority(processArray = testArrP):
     # Yousef's Job
     # Create bursts from testArr
    
     bursts =createGanttChart("PRIORITY_PREEMPTIVE", processArray )
     print("Priority-Based")

srt(testArr)