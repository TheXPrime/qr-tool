from utils import input_handler as inph
from core import generate, scan_image, scan_camera
def menu():
    print("=== QR TOOL ===")
    print("1) Generate QR\n2) Scan QR from image\n3) Scan QR from camera\n4) Exit")
def main():
    while True:
        menu()
        choice = inph.get_menu_choice()
        if choice == 1:
            generate.generate_flow()
        elif choice == 2:
            scan_image.scan_image_flow()
        elif choice == 3:
            scan_camera.scan_camera_flow()
        elif choice == 4:
            print("Bye")
            break
if __name__ == "__main__":
    main()