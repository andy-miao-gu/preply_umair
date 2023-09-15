 

import tkinter as tk
# Create the main window
root = tk.Tk()
root.title("Andys calculator")


p1 =  tk.PhotoImage(file = '/Users/andymiaogu/Desktop/preply_umair/Problem Solving/Just some random stuff/Part One/download2.png')
photo = tk.Label(root,image =p1)
photo.grid(row = 7, column =1,rowspan=  11)


# Create the length label and entry widget
mys_num = tk.Label(root, text="Mystiorious number:")
mys_num.grid(row=0, column=0)

mys_ent = tk.Entry(root)
mys_ent.grid(row=0, column=1)



mys_num2 = tk.Label(root, text="Mystiorious number 2:")
mys_num2.grid(row=1, column=0)

mys_ent2 = tk.Entry(root)
mys_ent2.grid(row=1, column=1)



mys_op = tk.Entry(root)
mys_op.grid(row=2, column=1)



mys_result = tk.Label(root, text="Mystiorious Result:")
mys_result.grid(row=16, column=0)


def andycalculate():
    ms1 = mys_ent.get()
    ms2 = mys_ent2.get()
    mso = mys_op.get()
    if mso == "^":
        mso = "**"
    elif mso == "÷":
        mso = "/"
    elif mso == "x":
        mso = "*"
    else:
        pass
    f = eval(ms1+mso+ms2)

    mys_result.config(text= "the result is "+str(f))


    print("huhuhuhuhuhahahahagrhyhahahyhyhyhyhths",f)

# Create the buttons for calculating area and perimeter
area_button = tk.Button(root, text="Mr. Andy calculator power!!!", command=andycalculate)
area_button.grid(row=6, column=0)

### make two more inputs like light and width and calculate area on same canvcas,,,\\\
mys_num3 = tk.Label(root, text="Length :")
mys_num3.grid(row=3, column=0)

mys_ent3 = tk.Entry(root)
mys_ent3.grid(row=3, column=1)



mys_num4 = tk.Label(root, text="Width :")
mys_num4.grid(row=4, column=0)

mys_ent4 = tk.Entry(root)
mys_ent4.grid(row=4, column=1)

mys_num5 = tk.Label(root, text="Height :")
mys_num5.grid(row=5, column=0)

mys_ent5 = tk.Entry(root)
mys_ent5.grid(row=5, column=1)

def andycalculator():
    lnh = mys_ent3.get()
    wdh = mys_ent4.get()
    hgt = mys_ent5.get()
    lnh,wdh,hgt = float(lnh),float(wdh),float(hgt)

    area = lnh*wdh*hgt

    mys_result.config(text= "the area is "+str(area))


area_button = tk.Button(root, text="Mr. Andy calculator area!!!", command=andycalculator)
area_button.grid(row=7, column=0)
### sin cos tan ctan

# Start the main event loop



### make a new 3 entries and a different button for calculate the area of triangle, calculate all threee angles of triangles

mys_num6 = tk.Label(root, text="tri_a :")
mys_num6.grid(row=1, column=2)

mys_ent6 = tk.Entry(root)
mys_ent6.grid(row=1, column=3)



mys_num7 = tk.Label(root, text="tri_b :")
mys_num7.grid(row=2, column=2)

mys_ent7 = tk.Entry(root)
mys_ent7.grid(row=2, column=3)

mys_num8 = tk.Label(root, text="tri_c :")
mys_num8.grid(row=3, column=2)

mys_ent8 = tk.Entry(root)
mys_ent8.grid(row=3, column=3)

def andytricalcu():
    tria = mys_ent6.get()
    trib = mys_ent7.get()
    tric = mys_ent8.get()
    tria,trib,tric = float(tria),float(trib),float(tric)

    triarea = tria*trib*tric*1/2

    mys_result.config(text= "the area of the triangle is "+str(triarea))

area_button = tk.Button(root, text="Mr. Andy calculator tri area!!!", command=andytricalcu)
area_button.grid(row=8, column=0)

### make the sqrt of a num


mys_num9 = tk.Label(root, text="sqrt :")
mys_num9.grid(row=4, column=2)

mys_ent9 = tk.Entry(root)
mys_ent9.grid(row=4, column=3)

def andysqrtcalcu():
    sqrt = mys_ent9.get()
    sqrt = float(sqrt)
    sqrt = (sqrt)**(1/2)

    mys_result.config(text= f"the sqrt of {mys_ent9.get()} is "+str(sqrt))

sqrt_button = tk.Button(root, text="Mr. Andy calculator sqrt!!!", command=andysqrtcalcu)
sqrt_button.grid(row=9, column=0)

### make the cbrt of a num


mys_num10 = tk.Label(root, text="cbrt :")
mys_num10.grid(row=5, column=2)

mys_ent10 = tk.Entry(root)
mys_ent10.grid(row=5, column=3)

def andycbrtcalcu():
    cbrt = mys_ent10.get()
    cbrt = float(cbrt)
    cbrt = (cbrt)**(1/3)

    mys_result.config(text= f"the cbrt of {mys_ent10.get()} is "+str(cbrt))

cbrt_button = tk.Button(root, text="Mr. Andy calculator cbrt!!!", command=andycbrtcalcu)
cbrt_button.grid(row=10, column=0)

## mi to km
mys_num11 = tk.Label(root, text="mile to km :")
mys_num11.grid(row=6, column=2)

mys_ent11 = tk.Entry(root)
mys_ent11.grid(row=6, column=3)

def andymikmconcalcu():
    mikmcon = mys_ent11.get()
    mikmcon = float(mikmcon)
    mikmcon = mikmcon*1.609344

    mys_result.config(text= f"{mys_ent11.get()} miles is {str(mikmcon)},kilometers")

sqrt_button = tk.Button(root, text="Mr. Andy calculator miles to km!!!", command=andymikmconcalcu)
sqrt_button.grid(row=11, column=0)

## km to yd


mys_num12 = tk.Label(root, text="km to yd :")
mys_num12.grid(row=7, column=2)

mys_ent12 = tk.Entry(root)
mys_ent12.grid(row=7, column=3)

def andykmydconcalcu():
    kmydcon = mys_ent12.get()
    kmydcon = float(kmydcon)
    kmydcon = kmydcon*1093.613298337708

    mys_result.config(text= f"{mys_ent11.get()} km is {str(kmydcon)},yards")

sqrt_button = tk.Button(root, text="Mr. Andy calculator km to yards!!!", command=andykmydconcalcu)
sqrt_button.grid(row=12, column=0)



def factorial():
    x=1
    for each in range(1,int(mys_ent14.get())+1):
        print(each,"*",x ,"= ",end="")
        x*=each
        print(x)
    mys_result.config(text= f"the factorial of {mys_ent14.get()} is {x}")
        
def convertages(rh):
    rh=float(rh)
    ans=(rh * 9/5) + 32
    rh=str(rh)
    ans=str(ans)
    print(rh,"degrees celcius = "+" "+ans,"ferinht")
    return ans
fever  = convertages(input("nummmmmmmmm degreesuesiusie")) 

fac_button = tk.Button(root, text="Mr. Andy calculator factorial!!!", command=factorial)
fac_button.grid(row=13, column=0)

mys_num14 = tk.Label(root, text="factorial :")
mys_num14.grid(row=8, column=2)

mys_ent14 = tk.Entry(root)
mys_ent14.grid(row=8, column=3)



root.mainloop()
