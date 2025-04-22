from tkinter import Tk, filedialog
from draw_boundary import define_intrusion_zone
from detect_intrusion import run_intrusion_detection

def select_video_file():
    root = Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(
        title="Select Video File",
        filetypes=[("MP4 files", "*.mp4"), ("All files", "*.*")]
    )
    return file_path

def main():
    video_path = select_video_file()
    if not video_path:
        print("No file selected. Exiting.")
        return

    print("[INFO] Step 1: Define intrusion zone...")
    zone_path = define_intrusion_zone(video_path)

    print("[INFO] Step 2: Running intrusion detection...")
    run_intrusion_detection(video_path, zone_path)

if __name__ == "__main__":
    main()
