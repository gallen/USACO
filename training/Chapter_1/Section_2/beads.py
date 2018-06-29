"""
 ID: actuato2
 LANG: PYTHON3
 TASK: beads
"""
with open("beads.in") as fInput:
    lines = fInput.readlines()


numOfBeads = int(lines[0].strip())
Beads = lines[1].strip()
Beads = list(Beads)
currentColor = False
total = 0

def ForceClose():
    with open("beads.out", 'w') as fOutput:
        fOutput.write(str(numOfBeads) + "\n")
        exit()

for i in range(numOfBeads):
    currentColor = Beads[i]
    Twice = False
    BackConsecutive1 = 0
    BackConsecutive2 = 0
    FrontConsecutive1 = 0
    FrontConsecutive2 = 0
    BeginningBead = 99999999
    if currentColor == 'w':
        continue
    for n in range(i, ((numOfBeads-i)*-1), -1):
        if n == BeginningBead or n == ((numOfBeads-1-BeginningBead)*-1):
            ForceClose()
        if n == i:
            BeginningBead = n
        if Beads[n] == currentColor or Beads[n] == 'w':
            if Twice == False:
                BackConsecutive1 += 1
            BackConsecutive2 += 1
        elif Twice == False:
            BackConsecutive2 += 1
            Twice = True
            currentColor = Beads[n]
        else:
            break
    Twice = False
    BeginningBead = None
    currentColor = Beads[i]
    for e in range(i, (numOfBeads+i), 1):
        if e == BeginningBead:
            ForceClose()
        if e == i:
            BeginningBead = e
        if e >= numOfBeads:
            e = e-numOfBeads
        if Beads[e] == currentColor or Beads[e] == 'w':
            if Twice == False:
                FrontConsecutive1 += 1
            FrontConsecutive2 += 1
        elif Twice == False:
            FrontConsecutive2 += 1
            Twice = True
            currentColor = Beads[e]
        else:
            break
    if BackConsecutive1 + FrontConsecutive2-1 > total:
        total = BackConsecutive1 + FrontConsecutive2-1
    if BackConsecutive2 + FrontConsecutive1-1 > total:
        total = BackConsecutive2 + FrontConsecutive1-1

if total == 0:
    total = numOfBeads
with open("beads.out", 'w') as fOutput:
    fOutput.write(str(total) + "\n")
