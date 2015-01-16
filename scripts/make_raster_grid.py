from grass import script as grass
import numpy as np

#! written by ADW on 16 Jan 2015
#  Released to the public domain

# This is to make a raster grid of the ICE only in an arbitrary location
# and at an arbitrary resolution that you, the user, define.

# Before running this script, open a new location with your desired projection
# and regional bounds.

# Name of the source location from which you will project
SOURCE_LOCATION = 'Dyke2003_WGS84'

# Then save your desired region -- not really necessary, but was as I once envisioned it
grass.run_command('g.region', flags='p', save='Output')

icenames = grass.read_command('v.proj', flags='l', location=SOURCE_LOCATION).split('\n')[:-1]
icenames = np.array(icenames)
length = np.array([len(icename) for icename in icenames])
icenames = sorted(list(icenames[length == 9]))

for icename in icenames:
  grass.run_command('r.proj', location=SOURCE_LOCATION, input=icename, overwrite=True)
  # Vector didn't work -- lost centroids. So rasterized in lat/lon location
  # and projecting directly
  #grass.run_command('v.proj', location=SOURCE_LOCATION, input=icename, overwrite=True)

# Export
for icename in icenames:
  grass.run_command('r.out.gdal', input=icename, output=icename+'.nc', format='netCDF')

