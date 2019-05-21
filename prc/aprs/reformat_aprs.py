
# W.A. Watters, 2019.05.20
# This script converts the UTC time to seconds since epoch in EDT
# also converts nan speed values to 0.0

import time
import calendar
import csv
import numpy as np
import epdobase as eb

ep = eb.cl_epdobase()
ep.load('./aprs_raw_copy.csv','csv')
ep.numerize()

epout = eb.cl_epdobase()
epout.init_fields(['time','lat','lng','speed','altitude'])

times = []

for i in range(ep.len()):
    currtime = ep.dcty['time'][i]
    timeinsec= calendar.timegm(time.strptime(currtime,'%Y-%m-%d %H:%M:%S'))
    if np.isnan(ep.ndct['speed'][i]):
        ep.ndct['speed'][i] = 0.0
    times.append(timeinsec)

for fld in epout.flds:
    epout.ndct[fld] = ep.ndct[fld]
    
epout.ndct['time'] = np.array(times)
epout.characterize()

epout.save('csv','aprs_reformated.csv')


