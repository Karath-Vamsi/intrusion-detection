#  Intrusion Detection System using YOLOv8

A smart video analytics system that detects and alerts unauthorized entry across a user-defined boundary in a surveillance video using YOLOv8 object detection.

---

## Project Overview

This system allows users to upload a surveillance video, interactively define a sensitive zone, and automatically detect when any person enters that restricted area. Visual alerts and sound notifications are triggered upon intrusion, and the output video is saved with annotations.

---

## Features

- Upload any `.mp4` surveillance video
- Draw intrusion boundary on the first frame
- Detect people using **YOLOv8** object detection
- Sound and on-screen alerts for intrusions
- Save processed video with detection overlays
- Simple GUI file picker for better usability

---

## Folder Structure

```
intrusion_alert/
├── main.py                       # Entry point
├── draw_boundary.py              # User defines intrusion zone
├── detect_intrusion.py           # Core detection & alert logic
├── utils.py                      # Utility functions (polygon check, etc.)
├── sounds/
│   └── alert.wav                 # Alert sound
├── outputs/
│   └── output_intrusion.mp4      # Annotated output video
├── zones/
│   └── zone_<timestamp>.npy      # Saved boundary zone
├── requirements.txt              # Dependencies
└── README.md                     # Project overview
```

---

## Tech Stack

- **Python 3.x**
- **OpenCV** – Video processing
- **Ultralytics YOLOv8** – Person detection
- **Tkinter** – File picker GUI
- **NumPy** – Zone calculations
- **Playsound** – Intrusion audio alert

---

## How to Run

### 1. Clone the repository
```bash
git clone https://github.com/Karath-Vamsi/intrusion-detection.git
```

### 2. Install requirements
```bash
pip install -r requirements.txt
```

### 3. Run the program
```bash
python main.py
```

### 4. Select a video and draw the intrusion zone

- A window will open with the first frame of your video.
- Click to draw the polygon boundary (double-click to close the shape).
- Detection will then begin frame-by-frame.

---

## Output

- Detected intrusions are labeled and boxed in red.
- A sound alert is triggered for every new intrusion.
- Output video is saved in `outputs/output_intrusion.mp4`.

---

## Applications

- Home & Office Security
- ATMs and Banking Zones
- Airports, Factories, Schools
- Parking Lot & Warehouse Monitoring

---

## Future Enhancements

- Real-time CCTV stream support
- Multiple intrusion zones
- Face recognition logging
- SMS/email notifications
- Night vision & thermal integration

---

## Workflow

1. **User Uploads Video**
2. **Draw Intrusion Boundary** on the first frame
3. **Detect People using YOLOv8** in each frame
4. **Check if Person Enters Intrusion Zone**
   - If Yes → Trigger alert (sound + label)
   - If No → Continue monitoring
5. **Save and Display** the output video

---


