"""
 ID: actuato2
 LANG: PYTHON3
 TASK: ride
"""

import math

def multiply(n):
    total = 1
    for i in range(0, len(n)):
        total *= n[i]
    return(total)

with open("ride.in") as fInput:
    lines = fInput.readlines()

lines = [line.strip() for line in lines]

letterValues = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

Groupnumbers = []

for e in range(len(lines[0])):
    Groupnumbers.append(letterValues[lines[0][e]])

CometNumbers = []

for i in range(len(lines[1])):
    CometNumbers.append(letterValues[lines[1][i]])

GroupValue = multiply(Groupnumbers) 
CometValue = multiply(CometNumbers)

if GroupValue % 47 == CometValue % 47:    
    with open("ride.out", 'w') as fOutput:
        fOutput.write("GO\n")
else:
    with open("ride.out", 'w') as fOutput:
        fOutput.write("STAY\n")


    
