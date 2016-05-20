import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

#ZAMIANA WYMIAROW
a=np.array([i**2 for i in range(16)])               #i^2 od 0 do 15

tab2D = np.reshape(a, (4,4))                        #przetworzenie na tablice 4x4
tab2D = a.reshape(4,4)                              #inna forma tego samego

# tab2D = 1                                         #zmiana typu
# tab2D[:,:] = 1                                    #przypisanie wartosci wszystkim elementom
# print tab2D

#FUNKCJE SAVE I LOAD

np.save("tab_a", a)
np.save("tab_2D", tab2D)

a = np.load("tab_a.npy")
tab2D = np.load("tab_2D.npy")

np.savetxt("tab_text", tab2D)

# print a
# print tab2D

# STRUKTURA DICTIONARY - MAPA
mapa = dict()
mapa = { "dom":1, "okno":2 }

# print mapa
# print mapa["dom"]
#
# mapa["drzwi"] = 3
# print mapa                          #mapa nie zachowuje kolejnosci, nie uzywac mapy, kiedy istotna kolejnosc elementow

# for i in mapa:
#     print i                         #domyslnie iteruje po kluczach
#
# for i in mapa.itervalues():         #iterowanie po wartosciach
#     print i

def suma (a,b):
    return a+b
def roznica(a,b):
    return a-b
def iloczyn(a,b):
    return a*b

fun_map = {"suma":suma, "roznica":roznica, "iloczyn":iloczyn}     #zmapowane

# KALKULATOR - suma 1 2
a=1
b=2
operacja = "iloczyn"

# print fun_map[operacja](a,b)
# print (5 in [4,2,4])                #czy element znajduje sie w liscie
# print "Czy jest suma w operacjach?", "suma" in fun_map

def suma_roznica(a,b):
    return a+b,a-b

# print type(suma_roznica(2,3))

x,y,z = [1,2,3]
x,y = suma_roznica(10,15)               #funkcja moze zwracac wiecej elementow
# print x
# print y
# print z

def pierwiastek(a, order=2):            #domyslna wartosc liczby
    return a**(1./order)

# print pierwiastek(2)
# print pierwiastek(2,3)                  #ale mozemy sami podac

#WYKRESY KONTUROWE

x=np.linspace(0,1,10)
y=np.linspace(0,1,10)

# plt.figure()
# plt.plot(x,y, color="red")
# plt.show()

X,Y = np.meshgrid(x,y)
Z = np.sin(X*Y)                         #element x element

plt.figure()
# cs = plt.contour(X,Y,Z)
cs = plt.contourf(X,Y,Z, 500, cmap=cm.spring)
# cs = plt.contourf(X,Y,Z, levels=[-1,-0.5,0,0.5,1], cmap=cm.winter)
plt.colorbar(cs)

plt.show()
