"""
 ID: actuato2
 LANG: PYTHON3
 TASK: friday
"""
with open("friday.in") as fInput:
    lines = fInput.readlines()
 
yearsSince1900 = int(lines[0])
leapYears = []
for x in range(yearsSince1900):
    if (1900+x) % 100 == 0 :
        if (1900+x) % 400 == 0:
            leapYears.append(x)
    elif (1900 + x) % 4 == 0:
        leapYears.append(x)

thirteenth = 1
totalThirteenths = [0,0,0,0,0,0,0]
totalThirteenths[thirteenth-1] += 1 
listOfMOY = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
monthsOfYears = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sep': 30, 'Oct': 31, 'Nov': 30, 'Dec':31}

for e in range(yearsSince1900):
    monthsOfYears['Feb'] = 28
    if e in leapYears:
        monthsOfYears['Feb'] = 29
    for i in range(12):
        thirteenth += (monthsOfYears[listOfMOY[i]] % 7)
        if thirteenth > 7:
            thirteenth -= 7
        totalThirteenths[thirteenth-1] += 1

totalThirteenths[thirteenth-1] -= 1

with open("friday.out", 'w') as fOutput:
    for m in range(7):
        fOutput.write(str(totalThirteenths[m]))
        if m != 6:
            fOutput.write(" ")
        else:
            fOutput.write("\n")

        
    
    


    