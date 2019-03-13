from sympy import *
def getstart(str):
    i=0
    while i<len(str):
        if str[i] in {'1','2','3','4','5','6','7','8','9','0','-'}:
            break
        else:
            i=i+1
    if i == len(str):
        return -1
    else:
        return i

def getend(str,start):
    i = start
    while i < len(str):
        if not(str[i]  in {'1','2','3','4','5','6','7','8','9','0','-'}):
            break
        else:
            i = i + 1

    return i-1


def wordcutter(stroka):
    str=stroka
    mass = []
    while getstart(str)>=0:
        start = getstart(str)
        end = getend(str,start)
        mass.append(str[start:end+1])
        str = str[end+1:]
    return mass

def zerocontrol(mass):
    i=0
    while i < len(mass):
        e=0
        while mass[i][e]=='0' and e<len(mass[i])-1:
            e = e + 1
        mass[i] = mass[i][e:]
        i = i +1

def is35(str):
    if is3(str) == 1 and is5(str) == 1:
        return 3
    if is3(str) == 1 and is5(str) == 0:
        return 1
    if is3(str) == 0 and is5(str) == 1:
        return 2
    return 0

def is3(stri):
    summ = 0
    if stri[0] == '-':
        i = 1
    else:
        i = 0
    while i < len(stri):
        summ = summ + (int)(stri[i])
        i= i + 1
    if summ > 9:
        return is3(str(summ))
    else:
        if summ in {0,3,6,9}:
            return 1
        else:
            return 0
def is5(stri):
    if stri[len(stri)-1] in {'0','5'}:
        return 1
    else:
        return 0
def fizz(stroka):
    res = ''
    mass = wordcutter(stroka)
    zerocontrol(mass)
    type(mass[0])
    for i in range(len(mass)):
        k = is35(mass[i])
        if k == 0:
            res=res+mass[i]
        if k == 1:
            res = res + 'fizz'
        if k == 2:
            res = res + 'buzz'
        if k == 3:
            res = res + 'fizzbuzz'
        if (i<(len(mass))):
            res += ' '
       # else:
           # res += '\n'
    return res
