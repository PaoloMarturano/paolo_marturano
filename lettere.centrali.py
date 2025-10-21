# Estrai le lettere centrali di una parola data dall'utente
p=input("Inserisci una parola: ")
lunghezza=len(p)
if lunghezza%2==0:
    metà=lunghezza//2
    p1= p[:metà-1]+ p[metà+1:]
    print("La parola senza le lettere centrali è:", p1)
else:
    metà=lunghezza//2
    p1= p[:metà]+ p[metà+1:]
    print("La parola senza la lettera centrale è:", p1)
    