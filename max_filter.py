import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

input_dir = 'images'
output_dir = 'results'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

image_path = os.path.join(input_dir, 'lena.jpg')
img = cv2.imread(image_path, 0)

if img is None:
    print(f"Error: Could not find {image_path}")
else:
    h, w = img.shape
    padded = np.pad(img, ((1, 1), (1, 1)), mode='constant', constant_values=0)
    output = np.zeros_like(img)

    # MANUAL MAX FILTERING
    for i in range(h):
        for j in range(w):
            region = padded[i:i+3, j:j+3]
            output[i, j] = np.max(region)

    plt.figure("Max Filter Result", figsize=(10, 5))
    plt.subplot(1, 2, 1); plt.imshow(img, cmap='gray'); plt.title('Original')
    plt.axis('off')
    plt.subplot(1, 2, 2); plt.imshow(output, cmap='gray'); plt.title('Max Filter (Dilation)')
    plt.axis('off')

    plt.savefig(os.path.join(output_dir, 'max_result.png'))
    print("Success: Max result saved in 'results' folder.")
    plt.show(block=True)