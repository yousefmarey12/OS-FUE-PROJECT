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
          "arrivalTime":10,
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
          "arrivalTime": 4,
          "burstTime": 4,
          "priority": 54,
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


# def createGanttChart(type="FCFS", bursts=[]):
#     time = 0
#     arr = []
#     # ---------------------------
#     # FCFS (your original logic)
#     # ---------------------------
#     if type == "FCFS":
#         bursts.sort(key=sorter("arrivalTime"))
#         for obj in bursts:
#             for _ in range(obj["burstTime"]):
#                 printTimeInstance(time, obj["id"])
#                 obj = {
#                     "time": time,
#                     "id": obj["id"]
#                 }
#                 arr.append(obj)
#                 time += 1
#         return arr

#     # ---------------------------
#     # SJF (Non-Preemptive)
#     # ---------------------------
#     elif type == "SJF":

#         # sort by arrival time
#         bursts.sort(key=sorter("arrivalTime"))

#         n = len(bursts)
#         completed = [False] * n     # track which processes are done
#         done = 0
#         arr = []
#         while done < n:

#             # get all processes that have arrived by current time
#             available = [
#                 bursts[i] for i in range(n)
#                 if bursts[i]["arrivalTime"] <= time and not completed[i]
#             ]

#             if not available:
#                 # CPU is idle → jump forward
#                 time += 1
#                 continue

#             # choose shortest burst time among arrived processes
#             job = min(available, key=lambda p: p["burstTime"])

#             # find index of job
#             idx = bursts.index(job)

#             # execute the job
#             for _ in range(job["burstTime"]):
#                 printTimeInstance(time, job["id"])
#                 obj = {
#                     "time": time,
#                     "id": job["id"] 
#                 }
#                 arr.append(obj)
#                 time += 1

#             completed[idx] = True
#             done += 1

     
def FCFS(bursts):
    time = 0
    arr = []
    bursts = sorted(bursts, key=lambda x: x["arrivalTime"])

    for p in bursts:
        # Instance:
            # The time elapsed is less than the time of the arrival of the earliest burst
            # Then the CPU will be IDLE and time += 1
        while time < p["arrivalTime"]:
            time += 1 
        for _ in range(p["burstTime"]):
            # Now we want to loop over the burstTime (notice how instead of an alphabet we use _)
            printTimeInstance(time, p["id"])
            obj = {
                "id": p["id"],
                "time": time
            }
            # we have to add it to the array to use for later and stats
            arr.append(obj)
            # a burst time takes one time unit so we increment it
            time += 1

    return arr


def SJF_NonPreemptive(bursts):
    time = 0
    n = len(bursts)
    completed = [False] * n
    arr = []
    done = 0
    
    while done < n:
        # print("hello")
        sorted1 =  sorted(bursts, key= lambda x: x["arrivalTime"])
       
        available = [
            
        ]

        i = 0
        while i < len(sorted1):
            if (sorted1[i]["arrivalTime"] <= time and  completed[i] == False):
                available.append(sorted1[i])
            i += 1
        while len(available) == 0:
            # print(sorted1)
            time += 1
            if sorted1[0]["arrivalTime"] <= time:
                break
        # print("available")
        # print(available)
        
        job = min(available, key=lambda x: x["burstTime"])
        idx = sorted1.index(job)

        for _ in range(job["burstTime"]):
            
            printTimeInstance(time,     job["id"])
            obj = {
                "time": time,
                "id": job["id"]
            }
            arr.append(obj)
            time += 1
        completed[idx] = True
        done += 1
    return arr


def SJF_Preemptive(bursts):  # SRTF
    time = 0
    n = len(bursts)
    remaining = []
    arr = []
    for i in range(0, n):
        remaining.append(bursts[i]["burstTime"])
    completed = 0
    while completed < n:
        bursts = sorted(bursts, key=lambda x: x["arrivalTime"])
        available = []
        i = 0
        while i < len(bursts):
            if (bursts[i]["arrivalTime"] <= time and remaining[i] > 0):
                available.append((i, bursts[i]))
            i += 1
        
        if not available:
            time += 1
            continue
        
        job = min(available, key=lambda x: remaining[x[0]])
        idx = bursts.index(job[1])
        printTimeInstance(time, job[1]["id"])
        obj = {
            "time": time,
            "id": job[1]["id"]
          }
        arr.append(obj)
        remaining[idx] -= 1
        time += 1
        if remaining[idx] == 0:
            completed += 1
    return arr
        
        
        
        
            
cpuUtilization = 100



def Priority_Preemptive(bursts):
    time = 0
    n = len(bursts)
    remaining = []
    arr = []
    wait =0
    for i in range(0, n):
        remaining.append(bursts[i]["burstTime"])
    completed = 0
    while completed < n:
        bursts = sorted(bursts, key=lambda x: x["arrivalTime"])
        available = []
        i = 0
        while i < len(bursts):
            if (bursts[i]["arrivalTime"] <= time and remaining[i] > 0):
                available.append((i, bursts[i]))
            i += 1
        
        if not available:
            printTimeInstance(time)
            time += 1
            wait += 1
            
            continue
        
        job = min(available, key=lambda x: x[1]["priority"])
        idx = bursts.index(job[1])
        printTimeInstance(time, job[1]["id"])
        obj = {
            "time": time,
            "id": job[1]["id"]
          }
        arr.append(obj)
        remaining[idx] -= 1
        time += 1
        
        if remaining[idx] == 0:
            completed += 1
    global cpuUtilization
    cpuUtilization =  ((time - wait) / time) * 100
    return arr
       
          

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


# print(firstCome(testArr))
def sjf(processArray = testArr):

     bursts = createGanttChart("SJF", processArray)
     print("Shortest Job First")

def srt(processArray = testArr):
     # Mohamed's Job

     bursts = createGanttChart("SRTF", processArray)
     print(bubbleSort(bursts))
     print("Shortest Remaining Time")
# srt(testArr)

def bubbleSort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j]["id"] > arr[j+1]["id"]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break
    return arr
def priority(processArray = testArrP):
     # Yousef's Job
     # Create bursts from testArr
     arr = [] 
     bursts =createGanttChart("PRIORITY_PREEMPTIVE", processArray )
    #  print(bursts)
    #  print(bubbleSort(bursts))
     i = 0
     currentID = bursts[0]["id"]
     arr = []
     arr.append([])
     bursts2 = bubbleSort(bursts)
     j = 0
    #  print(bursts
     while i < len(bursts2):
         if currentID == bursts2[i]["id"]:
            arr[j].append(bursts2[i])
         else:
            j += 1
            arr.append([])
            arr[j].append(bursts2[i])
            
         currentID = bursts2[i]["id"]
         i += 1
         

     print(len(arr[2]))
     i = 0
     
     avgWaitingTime = 0
     avgTAT = 0
     while i < len(arr):
         j = 0
         sTime = 0
         eTime = 0
         wTime = 0
         while  j < len(arr[i]):
               
                if j != 0:
                    wTime += (arr[i][j]["time"] - arr[i][j -1]["time"] - 1)
                if j == 0:
                    sTime = arr[i][0]["time"]
                if j == len(arr[i]) - 1:
                    eTime = arr[i][j]["time"]
                    avgWaitingTime +=wTime
                    avgTAT += (eTime - sTime + 1)
                    print("Start Time for Process "  + str(arr[i][0]["id"]) + " is " + str(sTime))
                    print("End Time for Process "  + str(arr[i][0]["id"]) + " is " + str(eTime))
                    print("Turnaround Time for Process is " + str(eTime - sTime + 1))
                    print("Wait Time for Process is " + str(wTime))
                j += 1
         print("___________")
         i += 1
     avgWaitingTime = avgWaitingTime / len(arr)
     avgTAT = avgTAT / len(arr)
     print("CPU Utilization is " + str(cpuUtilization) + "%")
     print("Average Waiting Time is " + str(avgWaitingTime))
     print("Average TAT is " + str(avgTAT))
     print("Priority-Based")

srt(testArr)