with open('my.txt') as file_object:
    
    contents = file_object.read()
    print(contents.rstrip())
    
    
    ### make another file my 2 and copy 

with open('my_2.txt') as objtect:
    
    contents = objtect.read()
    print(contents.rstrip())
    
    
filename ='my.txt'
with open(filename) as file_object:
    lines = file_object.readlines() 
    for line in lines:
        print(line.strip())
    
