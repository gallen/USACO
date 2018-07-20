INPUT = 4734

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

result = ['']

class TriTree:
    def __init__(self, value):
        self.value = value
        self.first = None
        self.second = None
        self.third = None
    def setFirst(self, tree):
        self.first = tree
        return tree
    def setSecond(self, tree):
        self.second = tree
        return tree
    def setThird(self, tree):
        self.third = tree
        return tree

def buildTree(num):
    root = TriTree('')
    curTreeNodes = [root]  

    for n in num:
        chars = KEY_PAD_MAPPING[n]
        tempTreeNodes = []
        for node in curTreeNodes:
            tempTreeNodes.append(node.setFirst(TriTree(chars[0])))
            tempTreeNodes.append(node.setSecond(TriTree(chars[1])))
            tempTreeNodes.append(node.setThird(TriTree(chars[2])))
        curTreeNodes = tempTreeNodes
    return root

result = []

def walkTree(tree, name):
    if tree.first == None:
        result.append(name)
    else:
        name1 = name + tree.value
        name2 = str(name1)
        name3 = str(name1)
        walkTree(tree.first, name1)
        walkTree(tree.second, name2)
        walkTree(tree.third, name3)



tree = buildTree(str(INPUT))
walkTree(tree, '')
result.sort()
print(result)
