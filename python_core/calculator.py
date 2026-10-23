ports_list=[80, 443, 3306, 8080]
for port in ports_list:
    if port == 3306:
        print("CRITICAL: Found Database on port:", port)
    else:
        print("Normal web traffic on port:", port)