p= input("Inserisci una parola: ")
lunghezza= len(p)
p1= p[lunghezza-1]+ p[+1:lunghezza-1]+ p[0]
print("La parola con la prima e l'ultima lettera scambiate è:", p1)