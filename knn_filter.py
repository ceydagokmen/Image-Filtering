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
    k_neighbors = 5
    padded = np.pad(img, ((1, 1), (1, 1)), mode='constant', constant_values=0)
    output = np.zeros_like(img)

    # MANUAL KNN FILTERING
    for i in range(h):
        for j in range(w):
            region = padded[i:i+3, j:j+3].flatten()
            center_val = int(img[i, j])
            
            # Compute absolute differences
            diffs = np.abs(region.astype(int) - center_val)
            # Find indices of the k closest intensities
            closest_indices = np.argsort(diffs)[:k_neighbors]
            output[i, j] = np.mean(region[closest_indices])

    plt.figure("KNN Filter Result", figsize=(10, 5))
    plt.subplot(1, 2, 1); plt.imshow(img, cmap='gray'); plt.title('Original')
    plt.axis('off')
    plt.subplot(1, 2, 2); plt.imshow(output, cmap='gray'); plt.title(f'KNN (k={k_neighbors})')
    plt.axis('off')

    plt.savefig(os.path.join(output_dir, 'knn_result.png'))
    print("Success: KNN result saved in 'results' folder.")
    plt.show(block=True)