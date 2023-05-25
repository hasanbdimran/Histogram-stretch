## Loading 2023 images
rasterName_2023 = r'/Users/ihasan/Downloads/Baki sir/downloadedImage/L9T1_2022/mosaic14Nov22.tif'
raster23 = rasterio.open(rasterName_2023)
nir = raster23.read(5)
red = raster23.read(4)
green = raster23.read(3)
# Normalize bands into 0.0 - 1.0 scale
def normalize(array):
    #array_min, array_max = np.nanmin(array), np.nanmax(array)
    std = np.nanstd(array)
    mean = np.nanmean(array)
    fc = 3
    array_min, array_max = mean - (std*fc), mean+ (std*fc)
    return (array - array_min) / (array_max - array_min)

# Stack bands
nrg = np.dstack((normalize(nir), normalize(red), normalize(green)))
plt.imshow(nrg)
