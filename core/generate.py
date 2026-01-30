import os
import qrcode
from qrcode.constants import ERROR_CORRECT_M, ERROR_CORRECT_Q
def generate_qr(data, out_path):
    ec_level = ERROR_CORRECT_M
    box_sz = 12
    
    n = len(data)
    
    if n <= 200:
        pass
    else:
        ec_level = ERROR_CORRECT_Q
        box_sz = 18
        
    try:
        qr = qrcode.QRCode(
            error_correction= ec_level,
            box_size= box_sz,
            border= 4
        )
        qr.add_data(data)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color = "black", back_color = "white")
        img.save(out_path)
        return True, None
    except Exception as e:
        return False, str(e)
def generate_flow():
    print("=== Generate QR ===")
    while True:
        
        data = input("Enter Text/Link: ").strip()
        
        if not data:
            print("Data cannot be empty!")
            continue
        break
    
    filename = input("Output filename (default: qr.png): ").strip().strip('"').strip("'")
    
    if not filename:
        filename = "qr.png"
        
    if filename == ".png":
        filename = "qr.png"
    
    if not filename.lower().endswith(".png"):
        filename = filename + ".png"
        
    out_dir = "data/output"
    
    os.makedirs(out_dir, exist_ok=True)
    
    out_path = os.path.join(out_dir, filename)
    
    if os.path.exists(out_path):
        answer = input("File exists. Overwrite? (y/n): ").strip().lower()
        
        if answer != "y":
            print("Canceled")
            return
    success,error = generate_qr(data, out_path)
    if success:
        print("Saved successfully in",out_path.replace("\\","/"))
    else:
        print(f"Failed to save QR: {error}")