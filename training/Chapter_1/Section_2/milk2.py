"""
 ID: gallen1
 LANG: PYTHON3
 TASK: milk2
"""



class Timespan:
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end
    def span(self):
        return (self.end - self.begin)

def canMerge(span1, span2):
    if (span1.end < span2.begin or span2.end < span1.begin):
        return False
    else:
        return True

def merge(span1, span2):
    return Timespan(min(span1.begin, span2.begin), max(span1.end, span2.end))

                
def mergeAll(mergeGroup):
    begins = [x.begin for x in mergeGroup]
    ends = [x.end for x in mergeGroup]
    return Timespan(min(begins), max(ends))

# Main program
g_initTimeSpans = [] # initial time span
g_mergedTimeSpans = [] # merged time span

# read input file
with open("milk2.in") as fInput:
    lines = fInput.readlines()

# read input to g_initTimeSpans
Farmers = int(lines[0].strip())
for i in range(1, Farmers+1, 1):
    b, e =  lines[i].strip().split()
    g_initTimeSpans.append(Timespan(int(b), int(e)))

# merge time spans
# either keep g_mergedTimeSpans sorted or sort it at the end.
for i in range(Farmers):
    checkSpan = g_initTimeSpans[i]
    newMergedTimeSpans = []
    canMergeTimeSpans = [checkSpan]
    for mSpan in g_mergedTimeSpans:
        if canMerge(checkSpan, mSpan):
            canMergeTimeSpans.append(mSpan)
        else:
            newMergedTimeSpans.append(mSpan)
    if len(canMergeTimeSpans) > 1:
        newMergedTimeSpans.append(mergeAll(canMergeTimeSpans))
    else:
        newMergedTimeSpans.append(checkSpan)
    g_mergedTimeSpans = newMergedTimeSpans


'''
while(True):
    mergedSpan = findFirstMerge()
    if mergedSpan == None:
        break
    else:
        g_mergedTimeSpans.append(mergedSpan)
'''

g_mergedTimeSpans.sort(key = lambda x: x.begin)


# find out max time span
maxTimeSpan = max(g_mergedTimeSpans, key = lambda x: x.span()).span()
if len(g_mergedTimeSpans) > 1:
    maxGaps = max([y.begin - x.end for(x, y) in zip(g_mergedTimeSpans[:-1], g_mergedTimeSpans[1:])])
else:
    maxGaps = 0



with open("milk2.out", 'w') as fOutput:
    fOutput.write(str(maxTimeSpan) + ' ' + str(maxGaps) + "\n")
    