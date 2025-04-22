# draw_boundary.py

import cv2
import numpy as np
import os

polygon_points = []

def draw_polygon(event, x, y, flags, param):
    global polygon_points
    if event == cv2.EVENT_LBUTTONDOWN:
        polygon_points.append((x, y))

def define_intrusion_zone(video_path):
    global polygon_points

    cap = cv2.VideoCapture(video_path)
    ret, frame = cap.read()
    cap.release()

    if not ret:
        raise ValueError("Could not read video.")

    clone = frame.copy()
    cv2.namedWindow("Define Zone")
    cv2.setMouseCallback("Define Zone", draw_polygon)

    print("Click to draw the intrusion zone. Press Enter or 'c' to confirm, 'r' to reset.")

    while True:
        temp = clone.copy()

        for i in range(len(polygon_points)):
            cv2.circle(temp, polygon_points[i], 5, (0, 255, 0), -1)
            if i > 0:
                cv2.line(temp, polygon_points[i-1], polygon_points[i], (255, 0, 0), 2)

        if len(polygon_points) > 2:
            cv2.line(temp, polygon_points[-1], polygon_points[0], (255, 0, 0), 2)

        cv2.imshow("Define Zone", temp)
        key = cv2.waitKey(1) & 0xFF

        if key == 13 or key == ord('c'):
            break
        elif key == ord('r'):
            polygon_points = []
        elif key == 27:
            print("Cancelled.")
            exit()

    cv2.destroyAllWindows()

    intrusion_zone = np.array(polygon_points)

    os.makedirs("zones", exist_ok=True)
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    zone_path = f"zones/{video_name}_zone.npy"
    np.save(zone_path, intrusion_zone)

    print(f"[INFO] Zone saved at: {zone_path}")
    return zone_path
