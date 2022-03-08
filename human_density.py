from gettext import install


import rasterio
import numpy as np

#GETTING TIF IMAGE AND DEFINING IT
tif_file = rasterio.open('E:\\Program Files\\Faculdade\\2022\\Codes\\Human Density Map\\Population_density_with_python\\GHS_POP_E2015_GLOBE_R2019A_4326_30ss_V1_0_13_10.tif')
ghs_data = tif_file.read()

#THESE ATTRIBUTES GET THE GENERAL RASTER IMAGE GRAPHIC SIZE. PRINTING IT JUST TO KNOW IF THE IMAGE IS NOT TOO BIG FOR LOCAL COMPUTER PROCESSING
print("Tiff Boundary", tif_file.bounds)
print("Tiff CRS", tif_file.crs)
print("Data shape", ghs_data.shape)
print("Max value", np.amax(ghs_data)) #GET MAXIMUM VALUE OF PEOPLE PER KILOMETER SQUARE
print("Min value", np.amin(ghs_data)) #GET MINIMUM VALUE OF PEOPLE PER KILOMETER SQUARE, -200 EQUALS NULL VALUE

#DONT KNOW WHAT IS THIS
ghs_data[0][ghs_data[0] < 0.0] = 0.0