while(True):
    x = input("please enter the integer:")
    y = input("please enter another integer:")
    z = input("please enter another another integer:")
    if x == "quit" or y == "quit" or z == "quit":
        break
    else:
        try:
            all_sum = int(x)+int(y)+int(z)
            print('sum of x, y, z is',all_sum)
        except :
            print('there is a typing error in x y and z',x,y,z)