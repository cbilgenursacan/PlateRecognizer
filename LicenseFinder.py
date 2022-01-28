import cv2

def PlateDetector(image):
    imGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    imB = cv2.bilateralFilter(imGray, 11, 17, 17)
    imCan = cv2.Canny(imB, 170, 200)
    
    X, Y, W, H = 0, 0, 0, 0
    try:
        countors, hierarchy = cv2.findContours(imCan.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        countors = sorted(countors, key = cv2.contourArea, reverse = True)[:30]
        LicensePlates = None

        for countor in countors:
            perimeter = cv2.arcLength(countor, True)
            ap = cv2.approxPolyDP(countor, 0.02*perimeter, True)
            
            if(len(ap) == 4): #Searching for four courner object
                LicensePlates = ap
                x, y, w, h = cv2.boundingRect(countor)
                X, Y, W, H = x, y, w, h                
    except:
        pass
    
    return X, Y, W, H