from PIL import Image
import numpy as np

# Load image
im = Image.open('input_filename')                                     

# Convert to format that cannot store IPTC/EXIF or comments, i.e. Numpy array
na = np.array(im)                                                                       

# Create new image from the Numpy array
result = Image.fromarray(na)

# Copy forward the palette, if any
palette = im.getpalette()
if palette != None:
    result.putpalette(palette)

# Save result
result.save('output_filename')