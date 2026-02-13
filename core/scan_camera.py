import cv2 as cv

def scan_camera_flow():
    print("=== Scan QR from Camera ===")
    print("Press 'q' to quit")

    raw = input("Camera Index (Default 0): ").strip()
    if not raw:
        cam_index = 0
    elif raw.isdigit():
        cam_index = int(raw)
    else:
        print("Invalid camera index, using 0")
        cam_index = 0

    cap = cv.VideoCapture(cam_index)

    cap.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, 720)

    if not cap.isOpened():
        print("Camera not accessible")
        return

    detector = cv.QRCodeDetector()
    last_data = None

    while True:
        ok, frame = cap.read()
        if not ok:
            print("Failed to read frame")
            break

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        try:
            data, points, _ = detector.detectAndDecode(gray)
        except cv.error:
            data, points = "", None

        used_scale = 1.0

        if not data:
            gray2 = cv.resize(gray, None, fx=2.0, fy=2.0, interpolation=cv.INTER_LINEAR)
            try:
                data2, points2, _ = detector.detectAndDecode(gray2)
            except cv.error:
                data2, points2 = "", None

            if data2:
                data, points = data2, points2
                used_scale = 2.0

        if data:
            if data != last_data:
                print("QR DATA:", data)
                last_data = data

            if points is not None:
                pts = points.reshape(-1, 2)

                if used_scale != 1.0:
                    pts = pts / used_scale

                pts = pts.astype(int).reshape(-1, 1, 2)

                cv.polylines(frame, [pts], True, (0, 255, 0), 2)

        cv.imshow("QR Scanner", frame)

        key = cv.waitKey(1) & 0xFF
        if key == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()
