import os
import cv2 as cv
cv.utils.logging.setLogLevel(cv.utils.logging.LOG_LEVEL_ERROR)
def decode_qr_from_image(image):
    detector = cv.QRCodeDetector()
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    try:
        data, points, _ = detector.detectAndDecode(gray)
    except cv.error:
        data, points = "", None

    if data:
        return (data, points)
    
    gray2 = cv.resize(gray, None, fx=2.0, fy=2.0, interpolation=cv.INTER_LINEAR)

    try:
        data2, points2, _ = detector.detectAndDecode(gray2)
    except cv.error:
        data2, points2 = "", None

    if data2:
        return (data2, points2)
        
    return (None, None)
def scan_image_flow():
    
    print("=== Scan QR from Image ===")
    
    while True:
        path = input("Enter image path: ").strip().strip('"').strip("'")
        path = os.path.normpath(path)
        if not path:
            print("Path cannot be empty")
            continue
        break
    
    if not os.path.exists(path):
        print("File not found")
        return
    
    image = cv.imread(path)
    if image is None:
        print("Could not read image")
        return
        
    data, points = decode_qr_from_image(image)
    if data is None:
        print("No QR Found")
    else:
        print("QR Data:",data)