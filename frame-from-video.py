# Импорт всех необходимых библиотек

import cv2

import os

  
# Читать видео по указанному пути

cam = cv2.VideoCapture("D:\Новая папка\Sherlock Holmes.avi")

  

# try:

      

    # # создание папки с именем data

    # if not os.path.exists('data'):

        # os.makedirs('data')

  
# # если не создано, то выдайте ошибку

# except OSError:

    # print ('Error: Creating directory of data')

  
# Рамка

currentframe = 0

  

# while(currentframe < 10):

      

    # # чтение из кадра

    # ret,frame = cam.read()

  

    # if ret:

        # # если видео еще осталось, продолжайте создавать изображения

        # name = './data/frame' + str(currentframe) + '.jpg'

        # print ('Creating...' + name)

  

        # # запись извлеченных изображений

        # cv2.imwrite(name, frame)

  

        # # увеличение счетчика, чтобы оно было

        # # показать, сколько кадров создано

        # currentframe += 1

    # else:

        # break


just_frame = 345678 # номер извлекаемого кадра

while(currentframe <= just_frame):

    ret,frame = cam.read()

    if (currentframe == just_frame):
        
        name_frame = str(just_frame) + '.png'
        
        cv2.imwrite(name_frame, frame)
            
    currentframe += 1
    

# Освободить все пространство и окна, как только сделано
cam.release()
cv2.destroyAllWindows() 
