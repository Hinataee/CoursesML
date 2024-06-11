# Using Yolov5 + CRNN， half-finshed
## dataset
- orginal data:label.csv   ./data
- data for yolo: ./datayolo ./yolodata
- data for CRNN: ./dataCRNN  ./CRNN/lmdb*-->data turned into lmdb
    - using ./utils to generate the dataset for the two
## train
according to official github
## weight trained
- yolo:./weights/yolov5_best.pth
- CRNN:./CRNN/expr2/best.pth
## intergrated demo.py for implement
./demo.py
- input path: ./data1/
- ouput csv: ./result.csv
