import cv2
import numpy as np


# путь до директории
image_path = '../data/room_ser.jpg'

# чтение 
img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

data = np.reshape(img, (-1,3))

print(data.shape)

data = np.float32(data)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

flags = cv2.KMEANS_RANDOM_CENTERS

compactness,labels,centers = cv2.kmeans(data,1,None,criteria,10,flags)

# отображение на консоли результата определения
print('Dominant color is: bgr({})'.format(centers[0].astype(np.int32)))