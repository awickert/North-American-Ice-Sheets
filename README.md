# North American Ice Sheets
History of ice sheets and ice caps from the Last Glacial Maximum to present in North America, as produced by Dyke et al. (2003)

### Ice sheet GIS Files

The folder "ProjectedOriginal" contains the original GIS shapefiles published by Dyke et al. (2003). These have been renamed by A. Wickert to a standard format that is:

```
iceXXXXXX.*
```

where "XXXXXX" corresponds to an age in RADIOCARBON years BP that is zero-padded for easier machine reading and sorting. Because these ages are in radiocarbon years, one must use a converter (such as [IntCal13](http://calib.qub.ac.uk/calib/calib.html)) to obtain the proper calendar ages.

The folder "WGS84" contains versions of the maps that were unprojected back into WGS84 lat/lon; the above notes on naming convention applies, and the only difference is that here, each of the different time slices has its own folder for its shapefiles.

### Purpose

This Geological Survey of Canada Open File Report was previsouly available online, but as it does not seem to be any longer, I am copying the core GIS files and description here, and also include a version that is projected to WGS84 and includes only ice and proglacial lakes (as land and ocean will change via sea level change and glacial isostatic adjustment, which is not represented here).

I am currently not including the paleogeographic map images that were part of the original open-file report, as the purpose of this repository is to share the data rather than to reproduce the publication.

### Citation

Users of this data set should reference:

* Dyke, A. S., A. Moore, and L. Robertson (2003), *Deglaciation of North America*, Open File 1574, Natural Resources Canada, Ottawa.

An additional paper that could be useful to read and reference is:

* Dyke, A. (2004), An outline of North American deglaciation with emphasis on central and northern Canada, in *Quaternary Glaciations--Extent and Chronology --- Part II: North America*, vol. 2, edited by J. Ehlers and P. L. Gibbard, pp. 373–424.

It is available from http://academic.macewan.ca/furzem/files/2011/10/Dyke-2004.pdf. These paleogeographic maps and the base data were also published in a CD companion to this volume.

### Notes
* While all of the GIS files are called "ice...", they really contain:
** (Original projected) Ice, modern ocean, modern continent, lakes
** (WGS84 unprojected by A. Wickert) Ice, lakes
* The unprojected versions seem to be good, but have not been extensively tested; please alert A. Wickert if there is a problem with them, as he would be to blame!
* The GIS maps created by Dyke et al. (2003) are *not* topologically correct. That is, there are some tiny gaps and overlaps between the ice and the lakes. *If anyone would like to correct these such that these lines are snapped onto each other, please do and let me know!*
* There is an ongoing project called MOCA that should lead to an update of these maps, eventually: http://www.physics.mun.ca/~lev/MOCA.html
* Send a message if these are useful to you!

### Copyright

The original GIS files (in folder "ProjectedOriginal", about to be uploaded at the time of writing) is copyrighted property of the Geological Survey of Canada, made available for the purposes of study, teaching and research.

Within the provisions of the copyright of GSC, I make any reprojections and derivative works freely available to the global community.
