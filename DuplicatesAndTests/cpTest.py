import checkpointLogic as cpl

cpl.cp0 = checkpt(0, 4, 17)
cpl.cp1 = checkpt(1, 5, 6)
cpl.cp2 = checkpt(2, 23, 24)
cpl.cp3 = checkpt(3, 16, 20)

cpl.cp0.assignPins()
cpl.cp1.assignPins()
cpl.cp2.assignPins()
cpl.cp3.assignPins()


i=0
while(True):
    if cpl.checkpointReached(i % 4):
        print(i%4)
        i +=1