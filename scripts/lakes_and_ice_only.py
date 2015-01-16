from grass import script as grass

#! written by ADW on 16 Jan 2015
#  Released to the public domain

### NOTE! This file was in the iceWGS84 directory when it was run
### Well, actually was all just copy/pate-run through ipython

# Note: before writing or using this script, I had:
# (1) Renamed the Dyke et al. (2003) files
# (2) Imported them into a GRASS GIS location with a projection given by the original files
# (3) Projected these to this location

# The land and water boxes were just really messy in their projection to 
# WGS84 (well, their unprojection) and they weren't so necessary. So I 
# remove them here after projecting and leave only the ice and the lakes

icenames = grass.read_command('g.list', type='vect', pattern='ice??????').split('\n')[:-1]

for icename in icenames:
  orig_new_name = 'ice_with_land_ocean_'+ icename[-6:]
  grass.run_command('g.rename', vector=icename+','+orig_new_name)

for icename in icenames:
  orig_new_name = 'ice_with_land_ocean_'+ icename[-6:]
  grass.run_command('v.extract', input=orig_new_name, output=icename, where="SYMB='LAKE' OR SYMB='ICE'", overwrite=True)
  
# Some seams have appeared at particular lines of latitude. Hm. Well, let's 
# just dissolve these boundaries between contigious areas with the same
# category value
for icename in icenames:
  grass.run_command('g.rename', vector=icename+',tmp', overwrite=True)  
  grass.run_command('v.dissolve', input='tmp', output=icename)

# And now to export all of them
for icename in icenames:
  grass.run_command('v.out.ogr', input=icename, output=icename)
  
  
# Creating a raster grid of ice only at 10 arcminute resolution
# for later use to project to new locations
# Coarse resolution is because I have modeling work in mind, which hasn't
# gotten fine enough yet!
# because vector around the poles and meridians -- not working so well
grass.run_command('g.region', flags='p', n=85, s=35, w=-170, e=0, res='0:10')
for icename in icenames:
  grass.run_command('v.to.rast', input=icename, output=icename, use='val', val=1, where="SYMB='ICE'", overwrite=True)
  
