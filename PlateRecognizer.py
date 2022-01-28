# author cbn
# date : 25.12.2021
#implementing needed modules
import cv2
import LicenseFinder
import easyocr
import sys
#import DatabaseConnection
counter = 1
easyreader = easyocr.Reader(['en'])
capture = cv2.VideoCapture(0)
while True:
    success, image = capture.read()
    Lx, Ly, Lw, Lh = LicenseFinder.PlateDetector(image)
    if (Lx != 0):
        try:
            LicensePlate = image[Lx:Lx+Lw, Ly:Ly+Lh]
            LicenseNumber = easyreader.readtext(LicensePlate)
            LicenseNumber = LicenseNumber[0][1]
            cv2.rectangle(image, (Lx,Ly), (Lx+Lw, Ly+Lh), (15,225,145), 2)
            cv2.putText(image, text = LicenseNumber ,org = (Lx, Ly), fontFace = cv2.FONT_HERSHEY_PLAIN, fontScale= 1, color=(15,225,145), thickness=2)
        except:
            LicensePlate = image
            pass
        
    cv2.imshow("Live Camera", image)
    cv2.imshow("License Plate", LicensePlate)
    
    waitkey = cv2.waitKey(1)
    if  waitkey & 0xFF == ord('q'):
        capture.release()
        cv2.destroyAllWindows()
        sys.exit()
        break
    elif  waitkey & 0xFF == ord('s'):
        try:
            print("License Number "+ LicenseNumber+" succesfully saved to database.")
        except:
        #Save the license number to database with owner information and other essentials still in progres...
            pass
            
