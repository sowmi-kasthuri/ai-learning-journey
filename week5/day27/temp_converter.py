# Simple Temperature convertor program

while True:
    user_temp = input("Enter temperature and unit (e.g. 100 F) or 'exit': ").strip()

    if user_temp.lower() in ('exit','quit'):
        break

    temp = user_temp.split()

    print(f"DEBUG: temp = {temp}")

    

    try:
        if len(temp) < 2:
            print(" Please enter values like 100 F")
            continue  

        value_temp = temp[0]
        unit_temp = temp[1]

        print(value_temp, unit_temp)

        value = float(value_temp)
        value = round(value,2)
        unit = unit_temp.strip().upper()

        if unit not in ("C","F","K"):
            print("Unknown unit. Use C, F, or K.")
        
        if unit == "C":
            f_value = round(value * 9/5 + 32, 2)
            k_value = round((value + 273.15), 2)
            print(f"{user_temp}  =  {f_value}F  = {k_value}K")
        
        if unit == "F":
            c_value = round(((value - 32) * 5/9), 2)
            k_value = round((c_value + 273.15), 2)
            print(f"{user_temp}  =  {c_value}C == {k_value}K")
        
        if unit == "K":
            c_value = round((value - 273.15), 2)
            f_value = round((c_value * 9/5 + 32), 2)
            print(f"{user_temp}  =  {c_value}C == {f_value}F") 

    except ValueError as e:
        print(f"Invalid number {user_temp}")
    
