def test(fun, *args):
    print "".join(['-' for i in range(40)])
    print fun.__name__[:-1].upper()+" "+fun.__name__[-1]
    res = fun(*args[:-1])
    if isinstance(args[0], str):
        decoded = "".join([chr(i) for i in args[-1]])
        if res == decoded:
            print "Yes, "+decoded.replace("my","your")
        else:
            print "No, "+decoded.replace("my","your").replace("has","has not")+" yet"
    else:
        print "Is correct? "+ str(res == args[-1])
    print "".join(['-' for i in range(40)])

def zadanie1(listObject):
    temp=[]
    temp.append(listObject[0])
    k=0
    for i in range(1,len(listObject)):
        if(listObject[i]!=temp[k]):
            temp.append(listObject[i])
            k=k+1
    return temp

def zadanie2(list1, list2):
    sum_list=[]
    t=0
    if(len(list1)>len(list2)):
        k=len(list2)
        n=len(list1)
    else:
        k=len(list1)
        n=len(list2)
        t=1

    for i in range(k):
        sum_list.append(list1[i])
        sum_list.append(list2[i])

    if(t==0):
        for element in list1:
            sum_list.append(element)
    else:
        for element in list1:
            sum_list.append(element)
    return sum_list

test(zadanie1, [1, 2, 3, 3, 5, 68, 68, 24], [1, 2, 3, 5, 68, 24])
test(zadanie2, [1, 2, 19, 'dd', ':P', ":("], [12,'c','5'], [1, 12, 2, 'c', 19, '5', 1, 2, 19, 'dd', ':P', ':('])


