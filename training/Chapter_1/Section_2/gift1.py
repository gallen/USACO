"""
 ID: actuato2
 LANG: PYTHON3
 TASK: gift1
"""
with open("gift1.in") as fInput:
    lines = fInput.readlines()

NP = int(lines[0].strip())
Friends = {}
listOfFriends = []
Money = 0

#Friends = {x.strip() : 0 for x in lines[1: NP + 1]}
#listOfFriends = [x.strip() : 0 for x in lines[1: NP + 1]]

for e in range(NP):
    Person = lines[e+1].strip()
    Friends[Person] = 0
    listOfFriends.append(Person)


Total = len(lines)-NP
Recievers = 0

for i in range(1, Total,1):
    checkedLine = lines[i+NP].strip()
    if checkedLine in Friends and Recievers == 0:
        Giver = checkedLine
    elif checkedLine in Friends:
        Friends[checkedLine] += Money
    else:
        Money, Recievers = [int(x) for x in checkedLine.split()]
        if Money == 0 and Recievers == 0:
            Money = 0
        else:
            Money = Money - (Money % Recievers)
            Friends[Giver] -= Money 
            Money = Money/Recievers
        Recievers += 1
    Recievers -= 1

MoneyOfFriends = []
for i in range(NP):
    MoneyOfFriends.append(Friends[listOfFriends[i]])

with open("gift1.out", 'w') as fOutput:
    for i in range(NP):
        fOutput.write(str(listOfFriends[i]) + " ")
        fOutput.write(str(int(MoneyOfFriends[i])) + "\n")



 

