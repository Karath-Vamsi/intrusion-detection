# main.py

from draw_boundary import define_intrusion_zone
from detect_intrusion import run_intrusion_detection

def main():
    video_path = input("Enter path to video (e.g., videos/your_video.mp4): ").strip()
    print("Step 1: Define intrusion zone on the first frame...")
    zone_path = define_intrusion_zone(video_path)

    print("Step 2: Running intrusion detection...")
    run_intrusion_detection(video_path, zone_path)

if __name__ == "__main__":
    main()
