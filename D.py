nilout = input("weight nilout : ")
yui = input("weight yui : ")
nilout = int(nilout)
yui = int(yui)

if nilout > yui:
    print("nilout over weight")
elif nilout < yui:
    print("yui over weight")
else :
    print("nilout=yui")
