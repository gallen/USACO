"""
 ID: actuato2
 LANG: PYTHON3
 TASK: beads
"""

class BeadsSection:
    def __init__(self, color):
        self.color = color
        self.length = 0
        self.next = None
        self.prev = None
    def addOne(self):
        self.length += 1
    def setNext(self, beadsSection):
        self.next = beadsSection
        beadsSection.prev = self

# Beads section ring head
g_BSRing = None

# Merge one section with it's next section
def mergeNext(beadsSection):
    global g_BSRing
    next = beadsSection.next
    if beadsSection == next:
        return beadsSection
    # set length
    beadsSection.length = beadsSection.length + next.length
    # reset head
    if g_BSRing == next:
        g_BSRing = beadsSection
    # reset next's next's prev
    next.next.prev = beadsSection
    # reset next
    beadsSection.next = next.next

    # return beadsSection to enable chain call
    return beadsSection

# Merge 
def mergePrev(beadsSection):
    global g_BSRing
    prev = beadsSection.prev
    if beadsSection == prev:
        return beadsSection
     # set length
    beadsSection.length = beadsSection.length + prev.length
    # reset head
    if g_BSRing == prev:
        g_BSRing = beadsSection
    # reset prev's prev's next
    prev.prev.next = beadsSection
    # reset prev
    beadsSection.prev = prev.prev

    # return beadsSection to enable chain call
    return beadsSection   

# construct beads section ring from input.    
def constructBSRing(beads):
    global g_BSRing
    curColor = None
    curSection = None
    for b in beads:
        if curColor != b:
            curColor = b
            temp = BeadsSection(b)
            if curSection != None:
                curSection.setNext(temp)
            curSection = temp
            curSection.addOne()
            if g_BSRing == None: # Right head
                g_BSRing = curSection
        else:
            curSection.addOne()
    curSection.setNext(g_BSRing)

def insertPseudoWhiteAfter(beadsSection):
    psehdoSection = BeadsSection('w')
    psehdoSection.setNext(beadsSection.next)
    beadsSection.setNext(psehdoSection)


# normalize beads section ring
# merge in between white color
# add pseudo white with lengh 0 for b/r neighers
def normalizeBSRing():
    prev = g_BSRing.prev
    if prev == g_BSRing:
        return
    if prev.color == g_BSRing.color:
        mergePrev(g_BSRing)

    curSection = g_BSRing
    while True:
        if curSection.color == 'w':
            if curSection.prev.color == curSection.next.color:
                curSection = mergeNext(mergeNext(curSection.prev))
        curSection = curSection.next
        if curSection == g_BSRing:
            break
    if g_BSRing.next == g_BSRing:
        return
    
    curSection = g_BSRing
    while True:
        if curSection.color != 'w' and curSection.next.color != 'w':
            insertPseudoWhiteAfter(curSection)
        curSection = curSection.next
        if curSection == g_BSRing:
            break       

def calculateMaxBeads():
    ret = 0
    if g_BSRing.next == g_BSRing:
        return ret
    if g_BSRing.next.next == g_BSRing:
        return ret
    if g_BSRing.next.next.next == g_BSRing:
        return ret
    if g_BSRing.next.next.next.next == g_BSRing:
        return ret

    done = False
    curSection = g_BSRing
    while True:
        if curSection.color == 'w':
            curMax = curSection.length
            next = curSection.next
            for i in range(3):
                if next == g_BSRing:
                    done = True
                curMax += next.length
                next = next.next
            if ret < curMax:
                ret = curMax
            if done:
                break
        curSection = curSection.next
        if curSection == g_BSRing:
            break
    return ret 

                

# Main program
# Read input
with open("beads.in") as fInput:
    lines = fInput.readlines()

numOfBeads = int(lines[0].strip())
beads = lines[1].strip()


# Read input to BeadsRing. BeadsRing is a collection of BeadsSections.
constructBSRing(beads)

# normalize beads right
normalizeBSRing()

# calculate max beads if bread
total = calculateMaxBeads()

if total == 0:
    total = numOfBeads 

with open("beads.out", 'w') as fOutput:
    fOutput.write(str(total) + "\n")
