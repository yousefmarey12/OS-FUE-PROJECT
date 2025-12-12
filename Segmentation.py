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
        "id": 1,
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
            print(str(k) + "        | " + str(processes[i]["segments"][j]["baseAddress"]) + "       | " + str(
                processes[i]["segments"][j]["size"]))
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
        if (offset > s["size"]):
            print("Not good offset")
            return -1
        print("Logical Address of segment " + str(segmentID) + " and offset of " + str(
            offset) + " has a physical address is " + str(s["baseAddress"] + offset))
        return s["baseAddress"] + offset


def segmentation_main():
    global segments
    segments = {}

    print("\n==== SEGMENTATION SIMULATOR ====\n")

    total_memory = int(input("Enter total physical memory size: "))

    num_processes = int(input("Enter number of processes: "))

    processes = []


    for p in range(num_processes):
        print(f"\n--- Process {p} ---")
        pid = int(input("Enter Process ID: "))
        seg_count = int(input("Enter number of segments: "))

        seg_list = []
        for s in range(seg_count):
            print(f"\nSegment {s}:")
            base = int(input("  Enter base address: "))
            size = int(input("  Enter segment size: "))

            seg_list.append({
                "baseAddress": base,
                "size": size
            })

        processes.append({
            "id": pid,
            "segments": seg_list
        })

    print("\n===== SEGMENT TABLE =====")
    printSegments(processes)

    print("\n===== LOGICAL → PHYSICAL TRANSLATION =====")
    segmentID = int(input("Enter Segment Number: "))
    offset = int(input("Enter Offset: "))

    result = getPhysicalAddress(segmentID, offset)

    print("\n===== DONE =====")

if __name__ == "__main__":
    segmentation_main()