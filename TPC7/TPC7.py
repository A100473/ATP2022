import csv
from ctypes import string_at
import mathplotlib.pyplot as plt


def lerAlunos (filename):
    f = open(filename, encoding= 'utf-8')
    f.readline()
    csv_file = csv.reader(filename, delimiter=';')
    lista = []
    for alunos in csv_file:
        lista.append(tuple(alunos))
    return lista

aluno = lerAlunos("alunos.csv")

def alunoCurso(aluno):
    dici= {}
    for _,nome,curso,*_ in aluno:
        if curso in dici:
            dici [curso] += 1 
        else:
            dici [curso] = 1
    return dici

def medAlunos(aluno):
    novalista= []
    for id,nome,curso,tpc1,tpc2,tpc3,tpc4 in aluno:
        x = int(tpc1) + int(tpc2) + int(tpc3) + int(tpc4)
        media = int(x/4)
        tuplo = (id,nome,curso,tpc1,tpc2,tpc3,tpc4,media)
        novalista.append(tuplo)
    return novalista

aluno1 = medAlunos(aluno)

def escalAlunos(aluno):
    escalao = ()
    novalista1 = []
    for id,nome,curso,tpc1,tpc2,tpc3,tpc4,media in aluno:
        if media >=1 and <=4:
            escalao = ("E")
        if media >=5 and <= 8:
            escalao = ("D")
        if media >=9 and <=12:
            escalao = ("C")
        if media >=13 and <=16:
            escalao = ("B")
        if media >=17 and <=20:
            escalao = ("A")
        tuplo = (id,nome,curso,tpc1,tpc2,tpc3,tpc4,media,escalao)
        novalista1.append(tuplo)
    return novalista1

aluno2= escalAlunos(aluno1)

def distribEsc(aluno2):
    dici = {}
    for _,_,_,_,_,_,_,_,escalao in aluno2:
        if escalao in dici:
            dici[escalao] +=1
        else:
            dici[escalao] = 1
    return dici

def distribGrafico(aluno2):
    dici= {}
    for _,_,_,_,_,_,_,_,escalao in aluno2:
        if escalao in dici:
            dici[escalao] +=1
        else:
            dici[escalao] = 1

        y = dici.values()
        x = dici.keys()

    plt.plot(x,y) 
    plt.xlabel("Escalão")
    plt.ylabel("Número de Alunos")
    plt.show()


def distribTabela():
    dici = {}
    for _,_,curso,*_ in aluno2:
        if curso in dici :
            dici[curso] += 1
        else:
            dici[curso] = 1
        
    n= 0
    p = list(dici.keys())
    d = list(dici.values())
    print (f"{'Curso':20} :: {'Número de alunos no curso':10} ")
    while n < len(dici):
        print (f"{str(p[n]):20} :: {str(d[n]):26}")
        n = n + 1









    




