import cv2
import numpy as np
import os
from skimage.metrics import structural_similarity as ssim


def calculate_metrics(image_path_1, image_path_2):
    img1 = cv2.imread(image_path_1)
    img2 = cv2.imread(image_path_2)

    img1 = cv2.resize(img1, (400, 400))
    img2 = cv2.resize(img2, (400, 400))

    gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    
    psnr_value = cv2.PSNR(img1, img2)
    ssim_value = ssim(gray_img1, gray_img2)
       
    return psnr_value, ssim_value

folder1 = 'logs/original/real_test_images'
folder2 = 'logs/flower_test/testset_200000'

image_files = os.listdir(folder1)

all_psnr = []
all_ssim = []

for filename in image_files:
    image_path_1 = os.path.join(folder1, filename)
    image_path_2 = os.path.join(folder2, filename)

    psnr_value, ssim_value = calculate_metrics(image_path_1, image_path_2)
    
    all_psnr.append(psnr_value)
    all_ssim.append(ssim_value)

    print(f'Image: {filename} - PSNR: {psnr_value:.2f}, SSIM: {ssim_value:.4f}')

print(f'Average PSNR: {np.mean(all_psnr):.2f}, Average SSIM: {np.mean(all_ssim):.4f}')
