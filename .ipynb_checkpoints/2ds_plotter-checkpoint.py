import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import random

# functions
def im2dec(arr):
    """takes in an n-by-8 array of 16-bit compressed representation of 2ds pixels and returns an n-by-128 array 
    of the expanded visual field
    """
    def dec2binarr(arr):
        return np.array(list(''.join([bin(int(i))[2:].zfill(16) for i in arr]))).astype(int)
    
    assert arr.shape[1] == 8
    return np.array([dec2binarr(i) for i in arr])


# loading data
sample_file = r'/home/disk/eos4/jkcm/Data/mntr/phase/2DS.20151205_subset.V.cdf'
sample_data = xr.open_dataset(sample_file)
processed_file = r'/home/disk/eos4/jkcm/Data/mntr/phase/proc2DS.20151205_subset.V.cdf'
proc_data = xr.open_dataset(processed_file)

#plot 40 random images
fig, axg = plt.subplots(nrows=8, ncols=5, figsize=(10,10))
axl = axg.flatten()
for i in range(40):
    random_particle = random.choice(proc_data.time)  # pick a random particle from the processed file
    particle_frame = proc_data.parent_rec_num[random_particle].values
    [slice_start, slice_end] = proc_data.position[random_particle].values
    image_data = sample_data['data'].isel(time=particle_frame-1, ImgBlocklen=slice(slice_start-1, slice_end)).values
    axl[i].imshow(~im2dec(image_data))
for ax in axl:
    ax.axis('off')