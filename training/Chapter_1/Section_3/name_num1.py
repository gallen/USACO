"""
PROG: namenum
LANG: PYTHON3
"""

# key pad mapping
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


# Num to names function.
# Input is a num string, output is a list of possible name
def numToNames(num):
    if (len(num) == 1):
        return list(KEY_PAD_MAPPING[num])
    else:
        lastNameList = numToNames(num[0:-1]) # Name list from last step
        trailerChars =  KEY_PAD_MAPPING[num[-1]] # trailer charactors for the last digit
        ret = []
        for c in trailerChars:
            copy = lastNameList.copy()
            ret += [x + c for x in copy]
        return ret


# Main program:

# Read name dictionary
with open('dict.txt') as fInput:
    lines = fInput.readlines()
    nameDict = {line.strip() for line in lines}

# Read input number
with open("namenum.in") as fInput:
    inputNum = fInput.readline().strip()

# Find result
result = [x for x in numToNames(inputNum) if x in nameDict]

# Sort...
result.sort()

# Write output
with open('namenum.out', 'w') as fOutput:
    if result:
        for r in result:
            fOutput.write(str(r) + '\n') 
    else:
        fOutput.write("NONE" + '\n')
