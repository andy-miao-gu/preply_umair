import tkinter as tk
# Create the main window
root = tk.Tk()
root.title("Andys calculator")

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
mys_result.grid(row=4, column=0)


def andycalculate():
    ms1 = mys_ent.get()
    ms2 = mys_ent2.get()
    mso = mys_op.get()
    f = eval(ms1+mso+ms2)

    mys_result.config(text= "the result is "+str(f))


    print("huhuhuhuhuhahahahagrhyhahahyhyhyhyhths",f)

# Create the buttons for calculating area and perimeter
area_button = tk.Button(root, text="Mr. Andy calculator power!!!", command=andycalculate)
area_button.grid(row=5, column=0)





# Start the main event loop
root.mainloop()