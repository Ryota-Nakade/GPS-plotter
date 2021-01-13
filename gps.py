import numpy as np
import gmplot 

#google map plot(python3)

# take position from Log -------------
data = []
with open('gps20210113152600.txt','rb') as my_file:
    for line in my_file:
        data.append(line)
        
la = []
lo = []
for line in data:
    if (str(line[:8])=="b'latitude'") and (np.bitwise_not(np.isnan(float(line[10:])))):
        la.append(float(line[10:]))
    elif (str(line[:9])=="b'longitude'") and (np.bitwise_not(np.isnan(float(line[11:])))):
        lo.append(float(line[11:]))
        
la = np.array(la)
lo = np.array(lo)

### plot -------------
gmap = gmplot.GoogleMapPlotter(43.075830, 141.341446, 18)
gmap.scatter( la, lo, '#FF5733', size = 0.1, marker = None )
gmap.draw( './gps20210113152600.html' )


