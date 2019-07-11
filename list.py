list = []
list.append('a')
print (list)

def makelist(min,max):
    list=[]
    for i in range(min, max):
        list.append(i)
    return list

makelist(10,23)


def makeEvenList(min,max):
    sample=[]
    for x in range (min,max):
        if x%2==0:
            sample.append(x)
    return sample