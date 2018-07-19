"""
PROG: namenum
LANG: PYTHON3
"""

KEY_PAD_MAPPING = {
    '2': "ABC",
    '5': "JKL",
    '8': "TUV",
    '3': "DEF",
    '6': "MNO",
    '9': "WXY",
    '4': "GHI",
    '7': "PRS"
    }

# Read name dictionary
with open('dict.txt') as fInput:
    lines = fInput.readlines()
    nameDict = {line.strip() for line in lines}

# Read input number
with open("namenum.in") as fInput:
    inputNum = fInput.readline().strip()

# Find all name list
result = ['']
for c in inputNum:
    lookupLetters = KEY_PAD_MAPPING[c]
    result = result * 3 # duplicate result 3 times
    resultLen = len(result)
    cur = 0 # current set position
    for l in lookupLetters:
        for i in range(resultLen // 3):
            result[cur] = result[cur] + l # Use char list could be more efficient
            cur += 1

# Filter names based on name dictionary
result = [x for x in result if x in nameDict]

# Sort...
result.sort()

# Write output
with open('namenum.out', 'w') as fOutput:
    if result:
        for r in result:
            fOutput.write(str(r) + '\n') 
    else:
        fOutput.write("NONE" + '\n')