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

# Usage
- Usage:
  ```
  python generate_labels.py -d <path> -s <path> -f <format>
  ```
- Options:
  
	-d, --data_path		Specifies the path where the data is stored.
  
	-s, --save_path		Specifies the path where the output will be saved.
  
	-f, --format		Specifies the file format to process, supported formats: {bench, aig}.

- Note: Files in .aiger format must be converted to .aig format before use.

	Conversion command example：
	```
	for file in *.aiger; do mv -- "$file" "${file%.aiger}.aig"; done
	```

# Example
```
python generate_labels.py -d ~/AIGDataset/all_case/aig -s ~/AIGDataset/all_case -f aig
```

Explanation: This command reads all files in ''~/AIGDataset/all_case/aig''（including all corresponding files in subdirectories, e.g., '~/AIGDataset/all_case/aig[/a/b/xxx.aig]'）and saves the results in '~/AIGDataset/all_case[/a/b/xxx/counting_simplify_PO/]'. Meanwhile, an 'abc.log' file will be created in the specified save_path to record the output logs of abc.

In the counting_simplify_PO directory, the following files will be generated:
```
.
├── signed_edge.csv
├── node-type.csv
└── label.csv
```

## File Description
- signed_edge.csv: Each row represents "**start_id, end_id, 1/-1**", where 1 indicates an edge without a not, and -1 indicates an edge with a not.
- node-type.csv: The rows are ordered by node IDs. Each row indicates the type of the node, where 0 represents a primary input (PI), and 1 represents an AND gate. 
- label.csv: The first row indicates "number of FA, number of HA" (FA: Full Adder, HA: Half Adder). Subsequent rows, ordered by node IDs, indicate whether the corresponding node is "FAin, FAout, HAin, HAout", represented as boolean values.

