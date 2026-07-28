from django.shortcuts import render
import cv2

# Create your views here.


def process_image():
    file="test_open_cv/yellow.jpeg"
    image_file=cv2.imread(file)
        
    image=cv2.cvtColor(image_file,cv2.COLOR_BGR2RGB)
    image2=cv2.cvtColor(image_file,cv2.COLOR_BGR2LAB)
    image3=cv2.cvtColor(image_file,cv2.COLOR_BGR2GRAY)
    image4=cv2.cvtColor(image_file,cv2.COLOR_BGR2HSV)
    cv2.imshow("Origina BGR",image_file)
    cv2.imshow("RGB",image)
    cv2.imshow("LAB",image2)
    cv2.imshow("GRAY",image3)
    cv2.imshow("HSV",image4)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
        
process_image()