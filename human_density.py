#LIBRARIES
from gettext import install
from matplotlib import cm
from matplotlib.colors import BoundaryNorm, LinearSegmentedColormap, ListedColormap
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import geopandas as gpd
import pandas as pd
from shapely.geometry import mapping
from rasterio import mask as msk
import rasterio
import numpy as np

#GETTING TIF IMAGE AND DEFINING IT
tif_file = rasterio.open('E:\\Program Files\\Faculdade\\2022\\Codes\\Human Density Map\\Population_density_with_python\\GHS_POP_E2015_GLOBE_R2019A_4326_30ss_V1_0.tif')
ghs_data = tif_file.read()

#GEOLOCATING SOUTH AMERICA FROM NATURAL EARTH SHAPEFILE
df = gpd.read_file('E:\\Program Files\\Faculdade\\2022\\Codes\\Human Density Map\\Population_density_with_python\\Natural Earth 10m Countries\\ne_10m_admin_0_countries.shp')
south_america = df.loc[df['CONTINENT'].isin(['South America'])]


#THESE ATTRIBUTES GET THE GENERAL RASTER IMAGE GRAPHIC SIZE. PRINTING IT JUST TO KNOW IF THE IMAGE IS NOT TOO BIG FOR LOCAL COMPUTER PROCESSING
print("Tiff Boundary", tif_file.bounds)
print("Tiff CRS", tif_file.crs)
print("Data shape", ghs_data.shape)
print("Max value", np.amax(ghs_data)) #GET MAXIMUM VALUE OF PEOPLE PER KILOMETER SQUARE
print("Min value", np.amin(ghs_data)) #GET MINIMUM VALUE OF PEOPLE PER KILOMETER SQUARE, -200 EQUALS NULL VALUE

#
ghs_data[0][ghs_data[0] < 0.0] = 0.0

#PLOTTING
#THIS ONE PLOT THE MAP WITH A GRADIENT BASED ON THE MAXIMUM AND MINIMUN VALUES FOUND ON THE RASTER (-200 AND 32000 FOR THIS CASE)

#THIS IS AN ADAPTION WHERE THE BANDS OF COLOR ARE DEFINED IN THE CODE. IN THIS CASE I'VE USED 17 TONES OF THE GRADIENT TO PRINT THE MAP
our_cmap = cm.get_cmap('cool', 10)
newcolors = our_cmap(np.linspace(0, 1, 10))
background_colour = np.array([0.9882352941176471, 0.9647058823529412, 0.9607843137254902, 1.0])
newcolors = np.vstack((background_colour, newcolors))
our_cmap = ListedColormap(newcolors)
bounds = [0.0, 1, 5, 10, 50, 200, 1000, 3500, 6000, 12000, 20000]
norm = colors.BoundaryNorm(bounds, our_cmap.N, clip=True)


#MAP PLOTTING
southa_array, clipped_transform = msk.mask(tif_file, [mapping(geom) for geom in south_america.geometry.tolist()], crop=True)

fig, ax = plt.subplots(facecolor='#FCF6F5FF')
fig.set_size_inches(14, 7)
ax.imshow(southa_array[0], norm=norm, cmap=our_cmap)
ax.axis('off')
plt.show()
