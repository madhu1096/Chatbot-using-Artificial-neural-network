import numpy as np
from keras.models import load_model
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
import keras

import cv2


model_0 = load_model('models/natural_categories.v1.0.h5')
model_1 = load_model('models/natural_categories.v1.1.h5')
model_2 = load_model('models/natural_categories.v1.2.h5')
model_3 = load_model('models/natural_categories.v1.3.h5')
model_4 = load_model('models/natural_categories.v1.4.h5')
model_5 = load_model('models/natural_categories.v1.5.h5')
model_6 = load_model('models/natural_categories.v1.6.h5')
model_7 = load_model('models/natural_categories.v1.7.h5')

cap = cv2.VideoCapture(0)
while(True):
  
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    img_item = 'my-image.jpg'
    cv2.imwrite(img_item,frame)

    path='my-image.jpg'
    test_image = image.load_img(path, target_size=(32,32))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    a = model_0.predict_classes(test_image)
    b = model_1.predict_classes(test_image)
    c = model_2.predict_classes(test_image)
    d = model_3.predict_classes(test_image)
    e = model_4.predict_classes(test_image)
    f = model_5.predict_classes(test_image)
    g = model_6.predict_classes(test_image)
    h = model_7.predict_classes(test_image)
    
    
    result=[a,b,c,d,e,f,g,h]
    counter={'c0':0,'c1':0,'c2':0,'c3':0,'c4':0,'c5':0,'c6':0,'c7':0}
    
    for i in range(0,7):
        if(result[i]==0):
                  counter['c0']=counter.get('c0')+1
        if(result[i]==1):
                  counter['c1']=counter.get('c1')+1
        if(result[i]==2):
                  counter['c2']=counter.get('c2')+1
        if(result[i]==3):
                  counter['c3']=counter.get('c3')+1
        if(result[i]==4):
                  counter['c4']=counter.get('c4')+1
        if(result[i]==5):
                  counter['c5']=counter.get('c5')+1
        if(result[i]==6):
                  counter['c6']=counter.get('c6')+1
        if(result[i]==7):
                  counter['c7']=counter.get('c7')+1
    
    pred=sorted(counter, key=counter.get, reverse=True)[:3]
                 
    prob1=counter.get(pred[0])
    prob2=counter.get(pred[1])
    prob3=counter.get(pred[2])
    
    prob1_f=(prob1/prob1)*100
    prob2_f=(prob2/prob1)*100
    prob3_f=(prob3/prob1)*100
    output_prob=[prob1_f,prob2_f,prob3_f]
    output=[]
    for i in range(0,3):
        if(pred[i]=='c0'):
            output.append('Chair')
        if(pred[i]=='c1'):
            output.append('Clock')
        if(pred[i]=='c2'):
            output.append('Door')
        if(pred[i]=='c3'):
            output.append('Fridge')
        if(pred[i]=='c4'):
            output.append('Helmet')
        if(pred[i]=='c5'):
            output.append('Key')
        if(pred[i]=='c6'):
            output.append('Motorcycle')
        if(pred[i]=='c7'):
            output.append('Window')
    
    print(output)
    print(output_prob)
    print('++++++++++++++++++++++++++++++++++++')     
    
    if cv2.waitKey(20) & 0xFF == ord('q'):
            break


cap.release()
cv2.destroyAllWindows()   
