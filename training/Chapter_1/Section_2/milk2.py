"""
 ID: actuato2
 LANG: PYTHON3
 TASK: milk2
"""
with open("milk2.in") as fInput:
    lines = fInput.readlines()

Farmers = int(lines[0].strip())
listOfTime = []
FarmerStartTime = []
FarmerEndTime = []
BeginningTime = 0
EndTime = 0
Milked = 0
NotMilked = 0
Start = 0
Stop = 0
time = {}

for i in range(1, Farmers+1, 1):
    Beginning, End =  lines[i].strip().split()
    FarmerStartTime.append(int(Beginning))
    FarmerEndTime.append(int(End))
    time['Farmer' + str(i)] = (int(Beginning),int(End))
    listOfTime.append('Farmer' + str(i))
    if int(Beginning) < Start:
        Start = int(Beginning)
    if int(End) > Stop:
        Stop = int(End)
for z in range(Farmers):
    BeginningTime = time[listOfTime[z]][0]
    EndTime = time[listOfTime[z]][1]
    for i in range(Farmers):
        CheckedFarmer = time[listOfTime[i]]
        if CheckedFarmer[0] <= BeginningTime and  CheckedFarmer[1] >= EndTime:
            BeginningTime = CheckedFarmer[0]
            EndTime = CheckedFarmer[1]
        elif CheckedFarmer[0] >= BeginningTime and CheckedFarmer[0] <= EndTime and CheckedFarmer[1] >= EndTime :
            EndTime = CheckedFarmer[1]
        elif CheckedFarmer[1] <= EndTime and CheckedFarmer[1] >= BeginningTime and CheckedFarmer[0] <= BeginningTime:
            BeginningTime = CheckedFarmer[0]
        if i == Farmers-1:
            if Milked < (EndTime - BeginningTime):
                Milked = EndTime - BeginningTime

PreviousEndTime = 100000000

for m in range(Farmers):
    PreviousEndTime = time[listOfTime[m]][1]
    for z in range(Farmers):
        if z >= Farmers: 
            z -= Farmers
        if m == z:
            continue
        Broken = False
        CurrentBeginningTime = time[listOfTime[z]][0]
        if CurrentBeginningTime > PreviousEndTime:
            for i in range(Farmers):
                Sta = time[listOfTime[i]][0]
                Sto = time[listOfTime[i]][1]
                if ((Sta < CurrentBeginningTime and Sta > PreviousEndTime) 
                or (Sto < CurrentBeginningTime and Sto > PreviousEndTime) 
                or (Sta <= PreviousEndTime and Sto >= CurrentBeginningTime)):
                    Broken = True
        else:
            Broken = True
        if Broken == False and (CurrentBeginningTime - PreviousEndTime) > NotMilked:
            NotMilked = CurrentBeginningTime - PreviousEndTime
        
    

with open("milk2.out", 'w') as fOutput:
    fOutput.write(str(Milked) + ' ' + str(NotMilked) + "\n")
    