import numpy as np

def reduce(A, rozmiar):
    #rozmiar - m x n czy n x n
    if isinstance(rozmiar, tuple) or isinstance(rozmiar, list):
        nx, ny = rozmiar
    elif isinstance(rozmiar, int):
        nx = rozmiar
        ny = nx
    else:
        print "Blad"
        return

    #wymiary wejsciowe
    sx=len(A)
    sy=len(A[0])

    if (nx>sx) or (ny>sy):
        print "Blad"
        return

    a_x = sx/nx
    a_y = sy/ny

    macierz = [[0. for i in range(nx)] for j in range(ny)]      #zerowanie nowej macierzy

    for i in range(nx):
        for j in range(ny):
            x = int(i*a_x)
            y = int(j*a_y)

            k = 1
            s = A[x][y]
            for xi in range(-1, 2, 2):
                for yj in range(-1, 2, 2):
                    ii = x + xi
                    jj = y + yj

                    #brzegowe elementy
                    if 0 <= ii < sx and 0 <= jj < sy:
                        s += A[x + xi][y + yj]
                        k += 1

            macierz[i][j] = s / k
    return macierz

# m = [[float(i*j) for i in range(5)] for j in range(5)]
#
# print np.array(m)
#
# print np.array(reduce(m, (3, 3)))