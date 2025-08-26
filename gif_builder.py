from PIL import Image
import os

# Path to folder containing images
folder = "cat"

# Collect all image files (PNG/JPG)
images = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith((".png", ".jpg"))]
images.sort()  # ensure correct order (frame1, frame2, ...)

# Open images
frames = [Image.open(img) for img in images]

# Save as GIF
frames[0].save("output.gif",
               save_all=True,
               append_images=frames[1:], 
               duration=100,   # speed in ms (300 = 0.3 sec per frame)
               loop=0)         # infinite loop

print("✅ GIF created successfully! Check output.gif")
