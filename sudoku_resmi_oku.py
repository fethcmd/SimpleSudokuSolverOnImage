# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 19:51:32 2022

@author: feth
"""

def resmi_listeye_cevir(resim_ismi=str()):
    import cv2 as cv
    import numpy as np
    from tensorflow.keras.models import load_model
    sudoku=cv.imread(resim_ismi,0)
    heightImg=450
    widthImg=450
    sudoku=cv.resize(sudoku,(widthImg,heightImg))
    def splitBoxes(img):
        rows = np.vsplit(img,9)
        boxes=[]
        for r in rows:
            cols=np.hsplit(r,9)
            for box in cols:
                boxes.append(box)
        return boxes
    boxes=splitBoxes(sudoku)
    model=load_model("myModel.h5")
    def getPrediction(boxes,model):
        result=[]
        for image in boxes:
            img=np.asarray(image)
            img=img[4:img.shape[0]-4,4:img.shape[1]-4]
            img=cv.resize(img,(28,28))
            img=img/255
            img=img.reshape(1,28,28,1)
            predictions=model.predict(img)
            classIndex=np.argmax(predictions,axis=-1)
            probabilityValue=np.amax(predictions)
            if probabilityValue >0.8:
                result.append(classIndex[0])
            else:
                result.append(0)   
        return result
    numbers=getPrediction(boxes, model)
    sudoku_penceresi=list()
    for f in range(0,73,9):
        sudoku_penceresi.append(numbers[f:f+9])
        
    return sudoku_penceresi
    





    