import pandas as pd
from PIL import Image

# 生成裁剪后的照片data，供训练使用

df = pd.read_csv("../label.csv")

for i in df.index:
    imgname = df['filename'][i]
    label = df['number'][i]
    xmin = df['xmin'][i]
    xmax = df['xmax'][i]
    ymin = df['ymin'][i]
    ymax = df['ymax'][i]
    img = Image.open('../data/'+imgname)

    # 正常拆分数据集
    cropped = img.crop((xmin, ymin, xmax, ymax))
    if i < 640:
        cropped.save('../data_CRNN/train1/' + format(int(label * 10), "06d") + '_' + str(i) + '.jpg')
    else:
        cropped.save('../data_CRNN/test1/' + format(int(label * 10), "06d") + '_' + str(i) + '.jpg')

    # 增加数据集的不确定性（生成不完全的裁剪）
    # height = ymax - ymin
    # cropped = img.crop((xmin,ymin+height*0.4,xmax,ymax))
    # if i < 740:
    #     cropped.save('../data_CRNN/append_transform/' + format(int(label * 10), "06d") + '_' + str(i) + '.jpg')

