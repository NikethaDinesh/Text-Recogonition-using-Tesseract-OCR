import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

img = cv2.imread('trial_2.jpg')

img = cv2.resize(img, None, fx=0.25, fy=0.25)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thresh_img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 11)

hImg, wImg = thresh_img.shape
boxes = pytesseract.image_to_data(thresh_img)
for x, b in enumerate(boxes.splitlines()):
    if x != 0:
        b = b.split()
        print(b)
        if len(b) == 12:
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.rectangle(thresh_img, (x, y), (w + x, h + y), (0, 0, 255), 1)
            cv2.putText(thresh_img, b[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (50, 50, 255), 1)

cv2.imshow('Result', thresh_img)
cv2.waitKey(0)
