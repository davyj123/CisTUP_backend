#Flask App for Object detection from Images.

Local Installation :
Step 1:
  pip install requirements.txt
Step 2:
  1. Create a folder 'dnn_model' in root folder of this project
  2. Download yolov4.cfg  from https://github.com/Tianxiaomo/pytorch-YOLOv4/blob/master/cfg/yolov4.cfg
  3. Download yolov4.weights from https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.weights
  4. Add yolov4.cfg file in 'dnn_model'
  5. Add yolov4.weights file in 'dnn_model'
     

Step 3:
  1. To Start Flask App: Run
     python server.py
