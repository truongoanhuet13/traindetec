import cv2
import os
import matplotlib.pyplot as plt
path = os.listdir()
file_count = len(path)
i = 0
for i in range(file_count - 1):
    img = cv2.imread(path[i])
    #print(path[i], img.shape)
    new_width = 102
    new_height = 71
    img_resize = cv2.resize(src = img, dsize = (new_width, new_height))
    resize_img_name = '%s' % path[i]
    #plt.imshow(img_resize)
    status = cv2.imwrite('/home/pi/train-detector/resize/' + resize_img_name, img_resize)

    print (status)
    print (resize_img_name, img_resize.shape)