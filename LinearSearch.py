pos=-1
def search(list,no):
    for i in range(len(list)):
        if list[i] == no:
            globals()['pos']=i
            return True
    return False

l=[1,4,5,9,10,11]
no=10
if search(l,no):
    print("Found" +"at pos "+str(pos+1))
else:
    print("Not Found")
