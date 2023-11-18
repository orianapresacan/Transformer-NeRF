import cv2
import numpy as np
import os

real_images_dir = 'data/x'
output_dir = 'logs'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for image_file in os.listdir(real_images_dir):
    if not (image_file.lower().endswith('.png') or image_file.lower().endswith('.jpg')):
        continue

    real_image_path = os.path.join(real_images_dir, image_file)
    real_image = cv2.imread(real_image_path, cv2.IMREAD_UNCHANGED)

    has_alpha = real_image.shape[2] == 4

    if has_alpha:
        foreground, alpha_channel = real_image[..., :3], real_image[..., 3]
    else:
        foreground = real_image
        alpha_channel = np.all(real_image != [0, 0, 0], axis=2).astype(np.uint8) * 255

    white_background = np.ones_like(foreground, dtype=np.uint8) * 255

    alpha_factor = alpha_channel[..., np.newaxis] / 255
    foreground = alpha_factor * foreground
    background = (1 - alpha_factor) * white_background
    combined_image = cv2.convertScaleAbs(foreground + background)

    output_image_path = os.path.join(output_dir, image_file)
    cv2.imwrite(output_image_path, combined_image)

    print(f"Processed {image_file}")
