# PariDispari
# scrivere un programma che chiede in ingresso un numero naturale e stampa a video se è pari o dispari
n=int(input("immetti un numero naturale: "))
resto=n%2
if resto==0:
    print("il numero é pari")
else:
    print("il numero é dispari")