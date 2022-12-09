from functools import reduce

with open("1.txt") as file:
    text = file.read()
    print(text)
    blocks = text.split("\n\n")
    list=[]
    for x in blocks:
        items=x.split("\n")
        total=0
        for y in items:
            print(y)
            if(y!=''):
             total=total+int(y)
     
        list.append(total)
    
    list.sort()
    print("done")    

     

     
    