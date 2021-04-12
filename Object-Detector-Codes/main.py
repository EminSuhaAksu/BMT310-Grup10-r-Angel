import cv2

thres = 0.53# Threshold to detect object

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
cap.set(10,70)
cap.set(32,50)

classNames= []
classFile = 'coco.names'
with open(classFile,'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(False)

while True:
    success,img = cap.read()
    classIds, confs, bbox = net.detect(img,confThreshold=thres)



    if len(classIds) != 0:


            for classId, confidence,box  in zip(classIds.flatten(),confs.flatten(),bbox):
                 if classId == 1 :
                    #print((box))
                    #print(classId, box)
                    #print(len(box))
                    middlex=box[0] + int(box[2]/2)
                    middley=box[1] + int(box[3]/2)
                    print(box)
                    print(middlex)
                    print(middley)
                    cv2.rectangle(img,box,color=(0,0,255),thickness=2)
                    cv2.putText(img,classNames[classId-1].upper(),(box[0]+10,box[1]+30),
                                cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
                    cv2.putText(img,"%"+str(round(confidence*100,2)),(box[0]+200,box[1]+30),
                                cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
                    cv2.putText(img, "eslesme", (box[0] + 200, box[1] + 60),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

                    cv2.putText(img, "X",  (middlex, middley),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
                 break


    cv2.imshow("Output",img)
    cv2.waitKey(1)
