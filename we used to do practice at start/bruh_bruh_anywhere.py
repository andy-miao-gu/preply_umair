try:
    file = "cat2s.txt"
    x = open(file)
    cats= x.readlines()
except:
    print("file",file,"not found")





try:
    y = open("dogDs.txt")
    dogs= y.readlines()
except FileNotFoundError:
    pass
print("file not found but we tried our best to find it")
#####This Code is to Try to Read What a Txt File But Using a 
#####Try-Except Loop so it Will Print that There is not file
#####that is Name the File in the Code 
