import torch.nn as nn


# class CropModel(nn.Module):
#     def __init__(self):
#         super().__init__()
#
#     def forward(self):
#         pass

import torch

yolo_path = r'C:\Users\Solitary\Desktop\yolov5'
img_path = '../data/'

yolo_model = torch.hub.load(yolo_path, 'custom', path=r'../weights/yolov5_best.pt', source='local')

img = img_path + 'hefei_3188.jpg'
results = yolo_model(img)
detection = results.xyxy[0].cpu().numpy()
print(detection)