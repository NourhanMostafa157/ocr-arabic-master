from pytesseract.pytesseract import image_to_string
from ArabicOcr import arabicocr
import cv2
import numpy as np
im_gray = cv2.imread('temp_front.jpg', cv2.IMREAD_GRAYSCALE)
#im_gray = cv2.cvtColor('front10.jpg', cv2.COLOR_BGR2GRAY)
#im_gray = cv2.bilateralFilter(im_gray ,11,18,18)
#im_gray = cv2.GaussianBlur(im_gray,(5,5), 0)
#im_gray = cv2.imread('id_nmf.png', cv2.IMREAD_GRAYSCALE)
im_bw = im_gray
thresh = 90
#im_bw= cv2.adaptiveThreshold(im_bw,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
im_bw = cv2.threshold(im_bw, thresh, 255, cv2.THRESH_BINARY)[1]


#im_bw = cv2.threshold_eng_num(im_bw)

pic = im_gray[50:350, 50:275]
cv2.imwrite('pic.jpg', pic)
Name = im_bw[150:310, 400:1000]
address = im_bw[300:450, 400:1000]
ID = im_bw[500:560, 400:1000]


name=image_to_string(Name,lang="ara")
add=image_to_string(address,lang="ara")
IDNumber=image_to_string(ID,lang="arabic_numbers")
#IDNumber= arabicocr.arabic_ocr(ID)
print(IDNumber)


IDNumber= ''.join(IDNumber.split())


if IDNumber[0]=='2': 
	year = '19' + IDNumber[1:3]
else:
	year = '20' + IDNumber[1:3]
month = IDNumber[3:5]
day = IDNumber[5:7]
BDate = year + '/' + month + '/'+ day


ocr_output = open("out.json","w+",encoding='utf-8')
ocr_output.write(name)
ocr_output.write('\n')
ocr_output.write(add)
ocr_output.write('\n')
ocr_output.write(IDNumber)
ocr_output.write('\n')
ocr_output.write(BDate)
ocr_output.close()
