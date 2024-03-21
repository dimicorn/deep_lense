import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imsave
import cv2 as cv
import os


def draw_lense(path: str, file_name: str, img: np.array) -> None:
    img = (img / img.max() * 255).astype(np.uint8)
    # thresh, img_bw = cv.threshold(img, 0, 255, cv.THRESH_OTSU)
    imsave(f'{path}/{file_name}.png', img, cmap='magma')

def draw(path: str, new_path: str) -> None:
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    classes = os.listdir(path)
    for cls in classes:
        images = os.listdir(f'{path}/{cls}')
        if not os.path.exists(f'{new_path}/{cls}'):
            os.makedirs(f'{new_path}/{cls}')
        for image in images:
            img = np.load(f'{path}/{cls}/{image}').squeeze()
            name = image.split('.')[0]
            draw_lense(f'{new_path}/{cls}', name, img)

train_path = 'dataset/train'
val_path = 'dataset/val'

new_train_path = 'data/train'
new_val_path = 'data/val'

draw(train_path, new_train_path)
draw(val_path, new_val_path)