from args import *
import cv2
import matplotlib.pyplot as plt
import pandas as pd

def show_cut(path, left, upper, right, lower):
    """
        原图与所截区域相比较
    :param path: 图片路径
    :param left: 区块左上角位置的像素点离图片左边界的距离
    :param upper：区块左上角位置的像素点离图片上边界的距离
    :param right：区块右下角位置的像素点离图片左边界的距离
    :param lower：区块右下角位置的像素点离图片上边界的距离
     故需满足：lower > upper、right > left
    """

    img = cv2.imread(path)

    print("This image's size: {}".format(img.shape))  # (H, W, C)

    plt.figure("Image Contrast")
    plt.subplot(1, 2, 1)
    plt.title('origin')
    plt.imshow(img)  # 展示图片的颜色会改变
    plt.axis('off')

    cropped = img[upper:lower, left:right]

    plt.subplot(1, 2, 2)
    plt.title('roi')
    plt.imshow(cropped)
    plt.axis('off')
    plt.show()

df = pd.read_csv("label.csv")
for i in df.index:
    show_cut(data_path + '/' + df['filename'][i],
             int(df['xmin'][i]), int(df['ymin'][i]), int(df['xmax'][i]), int(df['ymax'][i]))
