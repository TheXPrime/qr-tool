def get_menu_choice():
    valid_choices = [1,2,3,4]
    while True:
        raw = input("Select: ").strip()
        
        if not raw.strip():
            print("Please enter a number")
            continue
        
        if not raw.isdigit():
            print("Invalid input: enter a number")
            continue
        
        choice = int(raw)
        
        if choice not in valid_choices:
            print("Invalid option. Please choose 1, 2, 3, or 4")
            continue
        
        return choice