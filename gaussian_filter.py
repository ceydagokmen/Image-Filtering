import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# DIRECTORY CONFIGURATION
input_dir = 'images'
output_dir = 'results'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

image_path = os.path.join(input_dir, 'landscape.gif')
img = cv2.imread(image_path, 0)

# LOAD AND PROCESS IMAGE
if img is None:
    print(f"Error: Could not find {image_path}")
    print("Please ensure the 'images' folder contains 'landscape.gif'")
else:
    height, width = img.shape
    
    # Zero Padding
    padded_img = np.pad(img, ((1, 1), (1, 1)), mode='constant', constant_values=0)
    output_img = np.zeros_like(img)

    # 3x3 Gaussian Kernel
    # Center pixel (4) has the highest weight; total sum is 16
    kernel = np.array([[1, 2, 1], 
                       [2, 4, 2], 
                       [1, 2, 1]]) / 16

    # MANUAL FILTERING PROCESS
    for i in range(height):
        for j in range(width):
            # Extract the 3x3 neighborhood region
            region = padded_img[i:i+3, j:j+3]
            
            # Perform Convolution/Correlation (Multiply and Sum)
            value = np.sum(region * kernel)
            output_img[i, j] = value

    # VISUALIZATION AND SAVING
    plt.figure("Gaussian Filter Result", figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(output_img, cmap='gray')
    plt.title('Gaussian Blur (3x3)')
    plt.axis('off')

    save_path = os.path.join(output_dir, 'gaussian_result.png')
    plt.savefig(save_path)
    
    print(f"Success: Gaussian result saved to {save_path}")
    
    plt.show(block=True)
    input("Press Enter to close the program...")