# detect_intrusion.py

import cv2
import numpy as np
import os
from ultralytics import YOLO
from utils import is_point_inside_polygon

def run_intrusion_detection(video_path, zone_path):
    cap = cv2.VideoCapture(video_path)
    zone = np.load(zone_path)

    video_name = os.path.splitext(os.path.basename(video_path))[0]
    os.makedirs("outputs", exist_ok=True)
    output_path = f"outputs/{video_name}_output.avi"

    width = int(cap.get(3))
    height = int(cap.get(4))
    fps = cap.get(cv2.CAP_PROP_FPS)

    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'XVID'), fps, (width, height))
    model = YOLO("yolov8n.pt")  # Use the small YOLOv8 model

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)[0]
        boxes = results.boxes
        alert = False

        for box in boxes:
            cls = int(box.cls[0])
            if cls == 0:  # Person class
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                center = ((x1 + x2) // 2, (y1 + y2) // 2)

                if is_point_inside_polygon(center, zone):
                    alert = True
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                    cv2.putText(frame, "INTRUDER", (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
                else:
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        cv2.polylines(frame, [zone], isClosed=True, color=(255, 0, 0), thickness=2)

        if alert:
            cv2.putText(frame, "!!! INTRUSION ALERT !!!", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

        out.write(frame)
        cv2.imshow("Intrusion Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print(f"[INFO] Output saved to: {output_path}")
