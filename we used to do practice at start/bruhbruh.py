import json

v = {}
while(((True))):
    u =input("what's your favorite username")
    p =input("what's your favorite password")
    v[u] = p
    if u is "quit" or "quit" in p:
        break

with open("new.json", 'w') as f_obj:
    json.dump(v, f_obj)
   
with open("new.json", 'r') as f_obj:
    new = json.load(f_obj)


if new:
    print("fav username and password is is",new.items())
else:
    print("the file has no favorite number")



