import piplates.RELAYplate as RP

#Poll() from DAQCplate.py
def Poll():
    ppFoundCount=0
    for i in range (0,8):
        rtn = RP.getADDR(i)
        if (rtn==i):
            print ("RELAYplate found at address",rtn)
            ppFoundCount += 1
    if (ppFoundCount == 0):
        print ("No RELAYplates found")

Poll()
