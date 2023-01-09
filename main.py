import cv2
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt 
 
def median(src: str, dst: str, edge: int):
    image = Image.open(src)
    img = np.array(image)
    img_r = img[:, :, 0]
    img_g = img[:, :, 1]
    img_b = img[:, :, 2]
 
    height, width = img_r.shape
 
    new_array_r = np.zeros((height, width), dtype=int)
    new_array_g = np.zeros((height, width), dtype=int)
    new_array_b = np.zeros((height, width), dtype=int)
 
    pad = int((edge - 1)/2)
 
    for i in range(pad, height-pad):
        for j in range(pad, width - pad):
            new_array_r[i, j] = np.median(img_r[i - pad:i + pad + 1, j - pad:j + pad + 1])
            new_array_g[i, j] = np.median(img_g[i - pad:i + pad + 1, j - pad:j + pad + 1])
            new_array_b[i, j] = np.median(img_b[i - pad:i + pad + 1, j - pad:j + pad + 1])
 
    new_array = np.array([new_array_r, new_array_g, new_array_b])
    new_array = np.transpose(new_array, (1, 2, 0))
    img = Image.fromarray(np.uint8(new_array))
    img.save(dst)
    print(new_array_r)
 
 
src = "D://erweima//lvbo//zhongzhi//lena.jpg"
dst = "D://erweima//lvbo//zhongzhi//lena1.jpg"
median(src, dst, 5)
img = cv2.imread("D://erweima//lvbo//zhongzhi//lena1.jpg")
cv2.imshow('1',img)
cv2.waitKey()