## PV test script

from epics import caget, caput
from PVnamelist import pvnamelist

for pv in pvnamelist:
    try:
        print(pv + " is " + str(caget(pv)))
    except:
        print("can not get pv: " + pv)
