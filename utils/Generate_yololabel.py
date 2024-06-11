import pandas as pd

# 图片大小
width = 400
height = 296
# 生成用于yolo训练的标签
df = pd.read_csv("../label.csv") # 原标签目录
print(df.info())

for i in df.index:
    txtname = df['filename'][i].replace('.jpg','.txt')
    xcenter = ((df['xmin'][i] + df['xmax'][i]) / 2.0)/width
    ycenter = ((df['ymin'][i] + df['ymax'][i]) / 2.0)/height
    data_width = (df['xmax'][i] - df['xmin'][i])/width
    data_height = (df['ymax'][i] - df['ymin'][i])/height
    with open("./labels/"+txtname, "w+") as f:
        print(0, "%.6f %.6f %.6f %.6f" % (xcenter,ycenter,data_width,data_height), file=f)

