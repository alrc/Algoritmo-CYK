# Algoritmo-CYK
grammar1 = dict(
S = ['AB', 'BC'],
A = ['BA','a'],
B = ['CC', 'b'],
C = ['AB','a']
)

import fileinput
def find(element):
    list1 = []
    for rule in fileinput.input():
        for production in fileinput[rule]:
            if production.count(element) == 1:
                list1.append(rule)
    #print(list1)
    s = set(list1)
    return(s)
def productions(set1, set2):
    aux = set ()
    for v1 in set1:
        for v2 in set2:
            aux = aux | find(v1+v2)
    return aux
def cyk(cadena):
    m = []
    a = []
    for c in cadena:
        a.append(find(c))
    m.append(a)

    n = len(cadena)
    for i in range(2, n + 1):
        m.append([])
        for j in range(1, n - i + 2):
            aux = set ()
            #print (m)
            for k in range(1, i):
                #print("P(%d %d, A) = P(%d %d, B) + P(%d %d, C)" % (i - 1, j - 1, k - 1, j - 1, i - k - 1, j + k - 1))
                aux = aux | productions(m[k - 1][j - 1], m[i - k - 1][j + k - 1])
            m[i - 1].append(aux)
        #print()
    #print (m)
    return m

def show_m(m, cadena):
    n = len(cadena)
    for i in range(n - 1, -1, -1):
        for j in m[i]:
            if(len(j) == 0):
                print("%10s " % ("0"), end='')
            else:
                print("%10s " % (','.join(j)), end='')
        print()
    print("-----------" * n)
    for i in cadena:
        print("%10s " % (i), end='')
    print()

def check(m):
    n = len(m)
    print(m[n-1][0])
    if 'S' in m[n-1][0]:
        print("Se acepta")
    else:
        print("Se rechaza")


s = 'AB'
p = productions({'A' , 'C'},{'C'})

#print(p)
c = "bbaba"
res = cyk(c)
show_m(res, c)
print()
check(res)

