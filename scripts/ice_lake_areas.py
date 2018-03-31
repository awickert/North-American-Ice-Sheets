import shapefile
import pyproj
import numpy as np
import matplotlib.pyplot as plt
import glob2
from functools import partial
from shapely.geometry import shape
from shapely.ops import transform

files = sorted(glob2.glob('**/ice*.shp'))

# Projection to equal area
proj = partial(pyproj.transform, pyproj.Proj(init='epsg:4326'),
               pyproj.Proj(init='epsg:2163'))

Aice_all = []
Alakes_all = []
for filename in files:
    try:
        sf = shapefile.Reader(filename)
        print filename
        shapes = sf.shapes()
        records = sf.records()
        i = 0
        Aice = 0
        Alakes = 0
        for _shape in shapes:
            if records[i][-1] == 'ICE':
                projected = transform(proj, shape(_shape))
                Aice += projected.area
            elif records[i][-1] == 'LAKE':
                projected = transform(proj, shape(_shape))
                Alakes += projected.area
            i += 1
        Aice_all.append( Aice )
        Alakes_all.append( Alakes )
    except:
        print "FAILED:", filename
        
Aice_all = np.array(Aice_all)/1E6
Alakes_all = np.array(Alakes_all)/1E6

plt.ion()
plt.figure()
plt.plot(Alakes_all, 'b-', linewidth=2)
plt.plot(np.diff(Aice_all), 'k-', linewidth=2)
#plt.plot(Aice_all, 'k-', linewidth=2)
