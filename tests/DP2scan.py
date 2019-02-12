import piplates.DAQC2plate as DP2

for i in range(8):
    resp = DP2.getADDR(i)
    if (resp < 8):
        print("found DAQC2 at address: {}".format(resp))
