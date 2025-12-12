import math
import random


frames = []
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
pageSize = 4
physicalMemory = 32
pageTables = []

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

def calculatePageOffset(logicalAddress, m, n):
    b = f"{logicalAddress:0{m}b}"
    i = 0
    str1 = ""
    while i < n:
        str1 += b[n + i]
        i += 1

    d = int(str1, 2)
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
    return math.ceil(processSize / pageSize)

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
    numPages = calculateNumPages(process["size"], pageSize)

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
            print("Frame #" + str(i) + " is free")
        if currentPID != pagesTables[i]["id"]:
            pageNum = 0
        print("Frame #" + str(i) + " holds PID #" + str(pagesTables[i]["id"]) + " and page number " + str(pageNum))
        pageNum += 1
        currentPID = pagesTables[i]["id"]
        i += 1
    i = 1
    pageNum = 0
    currentPID = pagesTables[0]["id"]
    while i < len(pagesTables):
        rand = math.floor((random.random() * pageSize))
        print("For Process of PID #" + str(pageTables[i]["id"]))
        if currentPID != pagesTables[i]["id"]:
            pageNum = 0
        print("The Physical Address at logical address = " + str(pageNum) + " and offset = " + str(rand))
        print(logicalToPhysical(pageSize, pageNum, rand))

        pageNum += 1
        currentPID = pagesTables[i]["id"]
        i += 1

def makePageTables(processes):
    i = 0
    while i < len(processes):
        makePageTable(processes, processes[i]["id"])
        i += 1

def paging_main():
    global frames, pageTables
    frames = []
    pageTables = []

    print("\n==== PAGING SIMULATOR ====\n")

    total_memory = int(input("Enter total physical memory size: "))
    frame_size = int(input("Enter frame size: "))
    num_processes = int(input("Enter number of processes: "))

    global physicalMemory, pageSize
    physicalMemory = total_memory
    pageSize = frame_size

    initializeFrames()

    processes = []
    for i in range(num_processes):
        print(f"\n--- Enter details for Process {i} ---")
        pid = int(input("Enter Process ID: "))
        size = int(input("Enter Process Size: "))

        processes.append({
            "id": pid,
            "size": size
        })

    for p in processes:
        makePageTable(processes, p["id"])

    print("\n===== MEMORY LAYOUT =====")
    printMemoryLayout(frames)

    print("\n===== ADDRESS TRANSLATION =====")
    pid = int(input("Enter Process ID to translate: "))
    page = int(input("Enter Page Number: "))
    offset = int(input("Enter Offset: "))

    found = None
    for pt in pageTables:
        if pt["id"] == pid:
            found = pt
            break

    if not found:
        print("❌ Process not found!")
        return

    if page >= len(found["mapping"]):
        print("❌ Invalid page number!")
        return

    if offset >= frame_size:
        print("❌ Offset exceeds frame size!")
        return

    frame_num = found["mapping"][page]
    physical = logicalToPhysical(frame_size, frame_num, offset)

    print(f"\nLogical Address (Page={page}, Offset={offset}) -> Physical Address = {physical}")

    print("\n===== DONE =====\n")

if __name__ == "__main__":
    paging_main()