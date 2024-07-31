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


# USAGE
- Usage:
  
  ```python generate.py -d <path> -s <path> -f <format>```
- Options:
  
	-d, --data_path		指明数据路径
  
	-s, --save_path		指明存放路径
  
	-f, --format		指明处理文件类型，备选格式{bench, aig}

- Note:

.aiger格式的文件需要转化成.aig格式的文件才可以使用

参考转化指令：```for file in *.aiger; do mv -- "$file" "${file%.aiger}.aig"; done```

# EXAMPLE
```python generate.py -d ~/AIGDataset/all_case/aig -s ~/AIGDataset/all_case -f aig```
Description: 此命令将读取~/AIGDataset/all_case/aig/xxx.aig所有文件，并将结果存储在~/AIGDataset/all_case/xxx/counting/中
其中在counting目录下有：
.
├── signed_edge.csv
├── node-type.csv
└── label.csv

# File Description
- signed_edge.csv: 每一行表示{起始id, 终点id, 1/-1}，其中1表示没有not的边，-1表示有not的边
- node-type.csv: 0-PI, 1-AND, 2-PO，按节点id排列
- label.csv: 第一行表示{FA个数，HA个数}；其后每一行表示对应节点是否为{FAin,FAout,HAin,HAout}，按节点id排列
