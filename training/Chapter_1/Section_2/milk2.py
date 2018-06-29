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


def findFirstMerge():
    global g_initTimeSpans
    if len(g_initTimeSpans) <= 0:
        return None
    elif len(g_initTimeSpans) == 1:
        ret = g_initTimeSpans[0]
        g_initTimeSpans = []
        return ret
    else:
        mergedSpan = g_initTimeSpans[0]
        AlreadyChecked = [0]
        for i in range(len(g_initTimeSpans)-1):
            checkedIndex = i + 1
            if canMerge(g_initTimeSpans[checkedIndex], mergedSpan):
                mergedSpan = merge(g_initTimeSpans[checkedIndex], mergedSpan)
                AlreadyChecked.append(checkedIndex)
        g_initTimeSpans = [g_initTimeSpans[x] for x in range(len(g_initTimeSpans)) if x not in AlreadyChecked]
        return mergedSpan
                


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
while(True):
    mergedSpan = findFirstMerge()
    if mergedSpan == None:
        break
    else:
        g_mergedTimeSpans.append(mergedSpan)


g_mergedTimeSpans.sort(key = lambda x: x.begin)


# find out max time span
maxTimeSpan = max(g_mergedTimeSpans, key = lambda x: x.span()).span()
if len(g_mergedTimeSpans) > 1:
    maxGaps = max([y.begin - x.end for(x, y) in zip(g_mergedTimeSpans[:-1], g_mergedTimeSpans[1:])])
else:
    maxGaps = 0



with open("milk2.out", 'w') as fOutput:
    fOutput.write(str(maxTimeSpan) + ' ' + str(maxGaps) + "\n")
    