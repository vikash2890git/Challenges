import json


def extract_values(object1, key) :
    list1=key.split("/")
    Obj=json.loads(object1)
    c=0
    for ind in (list1):
        c=c+1
        val=Obj.get(ind)
        if val: 
           if c < len(list1) :
               if isinstance(val,dict):
                 Obj=dict(val).copy()
               else:
                   print("key mapping doesn't exist")
                   exit()
        else:
            print ("key mapping doesn't exist")
            exit() 
    print (val)

if __name__== '__main__':
    key =input("Key:")
    object1=(input("Enter object:"))
    extract_values(object1,key)
