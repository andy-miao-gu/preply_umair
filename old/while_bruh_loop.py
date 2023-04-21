txt = ""
while(True):
    input_bruh = input("bruh why do you like programing.")
    if "q" in input_bruh and "u" in input_bruh and "i"  in input_bruh and "t"  in input_bruh:
        break
    txt = txt  + input_bruh + "\n"
    
    
    
    
with open("apple.txt", 'w') as file_object:
    file_object.write(txt)