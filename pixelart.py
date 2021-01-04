import cv2
import numpy as np

img = cv2.imread("test.jpg", 1)
imgWidth =  np.shape(img)[1]
imgHeight =  np.shape(img)[0]
imgChannels = np.shape(img)[2]

KERNEL_WIDTH = int(0.02*imgWidth)
KERNEL_HEIGHT = int(0.02*imgHeight)
columnSlides = imgWidth // KERNEL_WIDTH
rowSlides = imgHeight // KERNEL_HEIGHT
resultImg = np.zeros((imgHeight, imgWidth, 3))

for channel in range(imgChannels):
    startRow = 0
    startCol = 0
    channelMap = img[:,:,channel]
    #Channel Map is 2d numpy array. 
    print("Channel: " + str(channel))
    for i in range(rowSlides): #Rows
        for j in range(columnSlides): #Columns
            receptiveField = channelMap[startRow:startRow+KERNEL_HEIGHT, startCol:startCol+KERNEL_WIDTH]
            resultImg[startRow:startRow+KERNEL_HEIGHT, startCol:startCol+KERNEL_WIDTH, channel] = round(np.median(receptiveField))
            startCol = startCol + KERNEL_WIDTH
        startCol = 0
        startRow = startRow + KERNEL_HEIGHT


cv2.imwrite('test_output.jpg', resultImg)

print("Hello world!")