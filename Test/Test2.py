
import matplotlib.pyplot as plt

img = plt.imread("blue.jpg")
print(type(img))
print(img.shape)
print((img))

output = img.copy()  # The original image is read-only!
output[:, :, :1] = 0
plt.imsave("blue.jpg", output)

fig = plt.figure()
ax = fig.subplots()
ax.imshow(img)

plt.figure(figsize = (7,7))
plt.imshow(img[:, :, 1], aspect = 'equal', cmap = 'gray', alpha = 0.5)
plt.show()


import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Load image
img = plt.imread('kitty.jpg')

# Create figure and axes objects
fig, ax = plt.subplots()

# Display the image on the axes
ax.imshow(img)

# Create a rectangle patch
rect = patches.Rectangle((50, 50), 200, 300, linewidth=1, edgecolor='r', facecolor='none')

# Add the patch to the axes
ax.add_patch(rect)

# Save the figure
plt.savefig('cropping.jpg')


import matplotlib.pyplot as plt
import numpy as np

# Create a 2x2 grid of subplots
fig, axs = plt.subplots(2, 2)

# Load four sample images
img1 = np.random.rand(100, 100)
img2 = np.random.rand(100, 100)
img3 = np.random.rand(100, 100)
img4 = np.random.rand(100, 100)

# Plot each image in a different subplot
axs[0, 0].imshow(img1)
axs[0, 1].imshow(img2)
axs[1, 0].imshow(img3)
axs[1, 1].imshow(img4)

# Show the plot
plt.show()