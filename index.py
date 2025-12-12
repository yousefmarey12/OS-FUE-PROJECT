import math
import random


# 
# Segmentation
# 
pageSize = 4

physicalMemory = 32
testArr = [
     {
          "id": 0,
          "arrivalTime": 0,
          "size": 4,
          "segments": [
              {
                  "baseAddress": 5,
                  "size": 2
              },
              {
                  "baseAddress": 8,
                  "size": 4
              }
          ],
          "burstTime": 5,
          "priority": -1,
          "timeQuantum": -1
     },
       {
          "id":1,
          "size": 4,
          "segments": [
                       {
                  "baseAddress": 0,
                  "size": 2
              },
              {
                  "baseAddress": 3,
                  "size": 1
              }
          ],
          "arrivalTime": 1,
          "burstTime": 3,
          "priority": -1,
          "timeQuantum": -1
     },
    {
          "id": 2,
          "arrivalTime": 2,
          "burstTime": 8,
          "segments": [
                       {
                  "baseAddress": 20,
                  "size": 4
              },
              {
                  "baseAddress": 26,
                  "size": 2
              }
          ],
          "size": 4,
          "priority": -1,
          "timeQuantum": -1
     },
       {
          "id": 3,
          "arrivalTime": 3,
          "size": 8,
          "segments": [
                       {
                  "baseAddress": 16,
                  "size": 3
              },
              {
                  "baseAddress": 14,
                  "size": 1
              }
          ],
          "burstTime": 6,
          "priority": -1,
          "timeQuantum": -1
     }
]

segments = {}
def printSegments(processes):
    i = 0
    print("Segment | Base | Limit")
    k = 0
    while i < len(processes):
        j = 0
        while j < len(processes[i]["segments"]):
            
            print(str(k) + "        | " + str(processes[i]["segments"][j]["baseAddress"]) +  "       | " + str(processes[i]["segments"][j]["size"]))
            segments[k] = {
                "baseAddress": processes[i]["segments"][j]["baseAddress"],
                "size": processes[i]["segments"][j]["size"]
            }
            k += 1
            j += 1
        
        i += 1


def getPhysicalAddress(segmentID, offset):
    if segments[segmentID]:
        s = segments[segmentID]
        if (offset > s["size"] ):
            print("Not good offset")
            return -1
        print("Logical Address of segment " + str(segmentID) + " and offset of " + str(offset) + " has a physical address is " + str( s["baseAddress"] + offset))
        return s["baseAddress"] + offset

printSegments(testArr)
getPhysicalAddress(4, 3)


# 
# Paging
# 
frames = []
def getProcess(array, id):
    i = 0
    while i < len(array):
        if array[i]["id"] == id:
            return array[i]
        i += 1


def initializeFrames():
    i = 0
    while i < physicalMemory / pageSize:
        frames.append({
            "id": -1,
            "bytes": []
        })
        j = 0
        while j < pageSize:
            frames[len(frames) - 1]["bytes"].append(-1)
            j += 1
        
        i += 1
        

pageTables = []

def calculatePageOffset(logicalAddress, m, n):
    b = f"{logicalAddress:0{m}b}"
    i = 0
    str1 = ""
    while i < n:
        str1 += b[n + i]
        i += 1

    d= int(str1,2)
    return d

def calculatePageNumber(logicalAddress, m, n):
    b = f"{logicalAddress:0{m}b}"
    i = 0
    print(b)
    str1 = ""
    while i < m - n:
        str1 += b[i]
        i += 1
    p = int(str1, 2)
    return p


def calculateNumPages(processSize, pageSize): 
    return math.ceil(processSize/pageSize)

def logicalToPhysical(frameSize, frameNumber, offset):
    return (frameSize * frameNumber) + offset

def findFreeFrame():
    i = 0
    while i < len(frames):
        if frames[i]["id"] == -1:
            return i
        i += 1
    print("this runs a billion times")
    return -1

def scheduleFrame(id):
    index = findFreeFrame()
    if (index != -1):
        frames[index]["id"] = id
    else:
        print("All frames busy")
    return index
        

def makePageTable(array, processID):
    i = 0
    memoryFull = False
    process = getProcess(array, processID)
    pageTables.append({
        "id": processID,
        "mapping": []
    })
    while i < len(array):

        if pageTables[i]["id"] == id:
            return pageTables[i]
        pageTables.append({
        "id": processID,
        "mapping": []
        })
        i += 1
    numPages= calculateNumPages(process["size"], pageSize)

    i = 0
    while i < numPages and not memoryFull:
        if (scheduleFrame(processID) == -1):
            print("No Memory For Process")
            memoryFull = True
        i += 1


def printMemoryLayout(pagesTables):
    i = 1
    pageNum = 0
    currentPID = pagesTables[0]["id"]
    while i < len(pagesTables):
        if pagesTables[i]["id"] == -1:
            print("Frame #" + str(i) + " is free" )
        if currentPID != pagesTables[i]["id"]:
            pageNum = 0
        print("Frame #" + str(i) + " holds PID #" + str(pagesTables[i]["id"]) + " and page number " + str(pageNum) )
        pageNum += 1
        currentPID = pagesTables[i]["id"]
        i += 1
    i = 1
    pageNum = 0
    currentPID = pagesTables[0]["id"]
    while i < len(pagesTables):
        rand =math.floor((random.random() * pageSize))
        print("For Process of PID #" + str(pageTables[i]["id"]))
        if currentPID != pagesTables[i]["id"]:
            pageNum = 0
        print("The Physical Address at logical address = " +str(pageNum) + " and offset = " + str(rand))
        print(logicalToPhysical(pageSize, pageNum, rand) )

        pageNum += 1
        currentPID = pagesTables[i]["id"]
        i += 1
       


def makePageTables(processes):
    i = 0
    while i < len(processes):
        makePageTable(processes, processes[i]["id"])
        i += 1
    


initializeFrames()
makePageTables(testArr)

printMemoryLayout(frames)




# 
# 
# CPU Scheduling
# 
   


# logicalToPhysical(4, 32)
    
    

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
          "rity": -1,
          "timeQuantum": 3
     },
       {
          "id":1,
          "arrivalTime": 2,
          "burstTime": 4,
          "rity": -1,
          "timeQuantum": 3
     },
       {
          "id": 2,
          "arrivalTime": 4,
          "burstTime": 1,
          "rity": -1,
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
    return SRTF_Scheduler().solve(bursts)
        
        
        
class SRTF_Scheduler:

    def get_completion_times(self, timeline, processes):
        for p in processes:
            p['completion_time'] = 0

        for entry in timeline:
            pid = entry['id']
            time = entry['time']
            for p in processes:
                if p['id'] == pid:
                    p['completion_time'] = max(p['completion_time'], time + 1)

    def calculate_turnaround_time(self, processes):
        total_tat = 0
        for p in processes:
            p['turnaround_time'] = p['completion_time'] - p['arrivalTime']
            total_tat += p['turnaround_time']
        return total_tat

    def calculate_waiting_time(self, processes):
        total_wt = 0
        for p in processes:
            p['waiting_time'] = p['turnaround_time'] - p['burstTime']
            total_wt += p['waiting_time']
        return total_wt

    def print_process_table(self, processes, avg_wt, avg_tat):
        print("\n" + "=" * 80)
        print(f"{'ID':<5} {'Arrival':<10} {'Burst':<10} {'Exit':<10} {'TurnAround':<12} {'Waiting':<10}")
        print("-" * 80)

        processes.sort(key=lambda x: x['id'])

        for p in processes:
            print(
                f"{p['id']:<5} {p['arrivalTime']:<10} {p['burstTime']:<10} {p['completion_time']:<10} {p['turnaround_time']:<12} {p['waiting_time']:<10}")

        print("-" * 80)
        print(f"Average Turnaround Time = {avg_tat:.2f}")
        print(f"Average Waiting Time    = {avg_wt:.2f}")
        print("=" * 80 + "\n")

    def solve(self, bursts):
        processes = [p.copy() for p in bursts]
        for p in processes:
            print(p)
            p['remaining'] = p['burstTime']

        n = len(processes)
        time = 0
        completed = 0
        timeline = []

        processes.sort(key=lambda x: x['arrivalTime'])

        while completed < n:
            available = []
            for p in processes:
                if p['arrivalTime'] <= time and p['remaining'] > 0:
                    available.append(p)

            if not available:
                time += 1
                continue

            current_process = min(available, key=lambda x: x['remaining'])

            timeline.append({"id": current_process["id"], "time": time})

            printTimeInstance(time, current_process['id'])

            current_process['remaining'] -= 1
            time += 1

            if current_process['remaining'] == 0:
                completed += 1

        self.get_completion_times(timeline, processes)
        total_tat = self.calculate_turnaround_time(processes)
        total_wt = self.calculate_waiting_time(processes)
        avg_tat = total_tat / n
        avg_wt = total_wt / n

        self.print_process_table(processes, avg_wt, avg_tat)

        return timeline
        
            
cpuUtilization = 100



def priority_Preemptive(bursts):
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


def printRow(id, arrivalTime, burstTime, CT, TAT, WaitingTime):
    print("=" * 30)
    print("ID = " + str(id) + "|" + "Arrival Time = " + str(arrivalTime) + "|" + "Burst Time = " + str(burstTime) + "|" + "Completion Time = " + str(CT) + "|" + "Turnaround Time = " + str(TAT) + "|" + "Waiting Time = " + str(WaitingTime))  
    print("=" * 30)

def printTable(rows):
    i = 0
    print("=" * 60)
    totalTAT = 0
    totalWaitTime = 0
    
    while i < len(rows):
        printRow(rows[i]["id"], rows[i]["arrivalTime"], rows[i]["burstTime"], rows[i]["completionTime"], rows[i]["turnaroundTime"], rows[i]["waitingTime"])
        totalTAT += rows[i]["turnaroundTime"]
        totalWaitTime += rows[i]["waitingTime"]
        i += 1
    print("Average Turnaround Time " + str(totalTAT/len(rows)))
    print("Average Waiting Time " + str(totalWaitTime/len(rows)))
    print("=" * 60)

    
          

def createGanttChart(algorithm, bursts):
    if algorithm == "FCFS":
        return FCFS(bursts)
    elif algorithm == "SJF":
        return SJF_NonPreemptive(bursts)
    elif algorithm == "SRTF":
         return SJF_Preemptive(bursts)
    elif algorithm == "PRIORITY_PREEMPTIVE":
         return priority_Preemptive(bursts)
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
     i = 1;
     arr = []
     prevID = bursts[0]["id"]
     j = 0
     arr.append([])
     arr2 = []
     arr[0].append(bursts[0])
     while i < len(bursts):
        burst = bursts[i]
        if prevID != burst["id"]:
            j += 1
            arr.append([])
        arr[j].append(burst)
        prevID = burst["id"]
        i += 1

     i = 0
     print(arr)
     while i < len(arr):
        ct = arr[i][len(arr[i]) - 1]["time"] 
        j = 0
        arrivalTime = -1
        burstTime = -1
        while j < len(processArray):
            if processArray[j]["id"] == arr[i][0]["id"]:
                arrivalTime = processArray[j]["arrivalTime"]
                burstTime = processArray[j]["burstTime"]
                break
            j += 1
        if arrivalTime != -1 and burstTime != -1:
            tat = ct - arrivalTime 
            waitingTime = tat - burstTime + 1
            arr2.append({
                "id": arr[i][0]["id"],
                "arrivalTime": arrivalTime,
                "burstTime": burstTime,
                "completionTime": ct,
                "turnaroundTime": tat,
                "waitingTime": waitingTime
            })
        i += 1
     printTable(arr2)
     print("First Come First Serve")


# firstCome(testArr)

# print(firstCome(testArr))
def sjf(processArray = testArr):
    bursts = createGanttChart("SJF", processArray)
    i = 1;
    arr = []
    prevID = bursts[0]["id"]
    j = 0
    arr.append([])
    arr2 = []
    arr[0].append(bursts[0])
    while i < len(bursts):
        burst = bursts[i]
        if prevID != burst["id"]:
            j += 1
            arr.append([])
        arr[j].append(burst)
        prevID = burst["id"]
        i += 1

    i = 0
    print(arr)
    while i < len(arr):
        ct = arr[i][len(arr[i]) - 1]["time"]
        j = 0
        arrivalTime = -1
        burstTime = -1
        while j < len(processArray):
            if processArray[j]["id"] == arr[i][0]["id"]:
                arrivalTime = processArray[j]["arrivalTime"]
                burstTime = processArray[j]["burstTime"]
                break
            j += 1
        if arrivalTime != -1 and burstTime != -1:
            tat = ct - arrivalTime + 1
            waitingTime = tat - burstTime + 1
            arr2.append({
                "id": arr[i][0]["id"],
                "arrivalTime": arrivalTime,
                "burstTime": burstTime,
                "completionTime": ct,
                "turnaroundTime": tat,
                "waitingTime": waitingTime
            })
        i += 1
    printTable(arr2)
    return arr

        
    
 

def srt(processArray = testArr):
     # Mohamed's Job
    SJF_Preemptive(processArray)
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

