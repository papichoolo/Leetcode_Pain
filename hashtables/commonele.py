#common interview Q finding common element in 2 lists

def item(list1,list2):
    dicty={}
    for i in list1:
        dicty[i]=True

    for j in list2:
        if j in dicty:
            return True
    return False