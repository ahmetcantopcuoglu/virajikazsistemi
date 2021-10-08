import cv2
import numpy as np 
import serial
import time
ser1 = serial.Serial(port="COM3",baudrate=9600)
time.sleep(2)
img=cv2.imread("C:/Users/PC/Desktop/Yolo/custom yolo model/viraj_data/viraj_images/127.jpg")


img_widht = img.shape[1]
img_height =img.shape[0]

img_blob =cv2.dnn.blobFromImage(img,1/255,(416,416),swapRB=True,crop=False)

labels = ["saga keskin viraj","sola keskin viraj","saga viraj","sola viraj"]

colors=["0,255,255","255,0,0","154,78,156","178,250,100"]

colors=[np.array(color.split(",")).astype("int")for color in colors]


model=cv2.dnn.readNetFromDarknet("C:/Users/PC/Desktop/Yolo/custom yolo model/yolov4/darknet/viraj_yolov4.cfg","C:/Users/PC/Desktop/Yolo/custom yolo model/code/viraj_yolov4_last.weights")

layers = model.getLayerNames()

output_layer = [layers[layer[0]-1] for layer in model.getUnconnectedOutLayers()]

model.setInput(img_blob)

detection_layers = model.forward(output_layer)

ids_list = []
boxes_list = []
confidences_list = []


for detection_layer in detection_layers:
  for object_detection in detection_layer:
        
    
     scores = object_detection[5:]
     predicted_id = np.argmax(scores)
     confidence = scores[predicted_id]
      
      
     if confidence > 0.10:
       
       label=labels[predicted_id]

       bounding_box = object_detection[0:4] * np.array([img_widht,img_height,img_widht,img_height])
    
       (box_center_x, box_center_y, box_widht, box_height) = bounding_box.astype("int")
    
       start_x  = int(box_center_x - (box_widht/2))
       start_y = int(box_center_y - (box_height/2))
    
       ids_list.append(predicted_id)
       confidences_list.append(float(confidence))
       boxes_list.append([start_x, start_y, int(box_widht), int(box_height)])
  
max_ids = cv2.dnn.NMSBoxes(boxes_list, confidences_list, 0.5, 0.4)

for max_id in max_ids:
    max_class_id = max_id[0]
    box = boxes_list[max_class_id]
    
    start_x = box[0]
    start_y = box[1]
    box_widht = box[2]
    box_height = box [3]

    predicted_id = ids_list[max_class_id]
    label = labels[predicted_id]
    confidence = confidences_list[max_class_id]

end_x = start_x + box_widht
end_y = start_y + box_height
    
box_color = colors[predicted_id]
box_color = [int(each) for each in box_color]
    
    
    
sag = "saga keskin viraj"
sol = "sola keskin viraj"
sa = "saga viraj"
so = "sola viraj"
    
if(confidence > 0.20 and label == sag):
    ser1.write("1".encode())
    time.sleep(1)
    ser1.close()
if(confidence > 0.20 and label == sol):  
    ser1.write("2".encode())
    time.sleep(1)
    ser1.close()
if(confidence > 0.20 and label == sa):  
    ser1.write("3".encode())
    time.sleep(1)
    ser1.close()
if(confidence > 0.20 and label == so):  
    ser1.write("4".encode())
    time.sleep(1)
    ser1.close()

label = "{}: {:.2f}%".format(label, confidence*100)
print("predicted object {}".format(label))
cv2.rectangle(img,(start_x,start_y),(end_x,end_y),box_color,2)
cv2.putText(img,label,(start_x,start_y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, box_color, 2)

cv2.imshow("Detection Window",img)
    
cv2.waitKey(0)
cv2.destroyAllWindows()
    
    
     
     
