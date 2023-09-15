
r = dict(apple="red",orange="orange",banana="yellow")
txt = ''
for each in r:
    print("the color of",each,"is",r[each],txt)
    txt = txt + "the color of "+ each+" is "+r[each] + '\n'
    
with open("bruh_dictionary.txt",'w') as fo:
    fo.write(txt)
    
    