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

test(zadanie1, [1, 2, 3, 3, 5, 68, 68, 24], [1, 2, 3, 5, 68, 24])

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

    test(zadanie2, [1, 2, 19, 'dd', ':P', ":("], [12, 'c', '5'], [1, 12, 2, 'c', 19, '5', 1, 2, 19, 'dd', ':P', ':('])

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

def zadanie3(listTuples):
    for i in range(len(listTuples)-1, 0, -1):
        for k in range (i):
            if(listTuples[k][-1] > listTuples[k+1][-1]):
                temp = listTuples[k]
                listTuples[k]=listTuples[k+1]
                listTuples[k+1]=temp
    return listTuples


test(zadanie3, [(1, 3), (3, 3, 2), (2, 1)], [(2, 1), (3, 3, 2), (1, 3)])

def zadanie4(text):
    return " ".join(word.replace("ok","") for word in text.split("$") if word.startswith("ok"))

test(zadanie4, "okmy$aiaetiaigaafbaf??a$okwatch$oafbusd$okhas$asbrsi31480$okended$aq340af", [109, 121, 32, 119, 97, 116, 99, 104, 32, 104, 97, 115, 32, 101, 110, 100, 101, 100])

from random import randint
def zadanie5():
    x=randint(1,9)
    win=0
    count=1
    while(win==0):
        a = input("Podaj liczbe: ")
        if(a==x):
            print "Zgadles! Liczba prob: ", count
            win=1
        else:
            print "Probuj dalej"
            count=count+1

zadanie5()