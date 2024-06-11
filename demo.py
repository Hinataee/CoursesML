import os
import torch
from PIL import Image
from CRNN import params,utils,dataset
from CRNN.models import crnn
from torch.autograd import Variable
import csv

"""*****************************yolo*********************************"""
yolo_path = r'./yolov5'
img_path = './data1/'

yolo_model = torch.hub.load(yolo_path, 'custom', path=r'./weights/yolov5_best.pt', source='local')
yolo_model.to("cpu")

pics = os.listdir(img_path)
for i in pics:
    img = img_path + i

    img = Image.open(img)
    results = yolo_model(img)
    detection = results.xyxy[0]
    *xyxy, conf, cls = detection[0]
    x1, y1, x2, y2 = map(int, xyxy) # 转化为整数
    crop_img = img.crop((x1, y1, x2, y2))
    crop_img.save("./temp/"+i)


"""********************************CRNN******************************"""

model_path = r"./CRNN/expr2/best.pth"
image_path = r"./temp"

# net init
nclass = len(params.alphabet) + 1
model = crnn.CRNN(params.imgH, params.nc, nclass, params.nh)
if torch.cuda.is_available():
    model = model.cuda()

# load model
print('loading pretrained model from %s' % model_path)
if params.multi_gpu:
    model = torch.nn.DataParallel(model)
model.load_state_dict(torch.load(model_path))

converter = utils.strLabelConverter(params.alphabet)

transformer = dataset.resizeNormalize((200, 32))
pics = os.listdir(image_path)
for i in pics:
    image = Image.open(image_path+'/'+i).convert('L') # 加载成灰度图像-->只有一个通道
    image = transformer(image)

    if torch.cuda.is_available():
        image = image.cuda()
    image = image.view(1, *image.size())  # 相当于batchsize为1
    image = Variable(image)

    model.eval()
    preds = model(image)

    _, preds = preds.max(2)
    preds = preds.transpose(1, 0).contiguous().view(-1)

    preds_size = Variable(torch.LongTensor([preds.size(0)]))
    raw_pred = converter.decode(preds.data, preds_size.data, raw=True)
    sim_pred = converter.decode(preds.data, preds_size.data, raw=False)
    print('%-20s => %-20s' % (raw_pred, sim_pred))

    print("%.1f" % (float(sim_pred)/10))

    with open("result.csv","a+",newline='') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow([i,"%.1f" % (float(sim_pred)/10)])
