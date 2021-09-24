n=int(input('Dati numarul de elemente din vector='))
a=[]
print('Introduceti ',n,' elemente pentru vectorul creat')
if n<10:
    for i in range(0,n):
        x=int(input('Dati elementul='))
        a.extend([x])
print('a) afiseaza pe ecran componentele tabloului la un interval de 5 pozitii')
print(a[::5])
print('b) afiseaza pe ecran numerele in ordinea inversa a introducerii in calculator')
print(a[::-1])
print('c) sorteaza componentele tabloului in ordine descrescatoare')
b=sorted(a)
b.sort(reverse=True)
print(b)
print('d) afiseaza pe ecran doar componentele pare')
pare=[]
for i in range(0,len(a)):
        if a[i]%2==0:
            x=a[i]
            pare.extend([x])
print(pare)
print('e) afişează pe ecran media aritmetică a componentelor pare', sum(pare) / len(pare))
print('f) afiseaza pe ecran doar componentele impare')
impare=[]
for i in range(0,len(a)):
    if a[i]%2!=0:
        ia=a[i]
        impare.extend([ia])
        print(impare)
print('g) afişează pe ecran doar componentele care sunt mai mari ca x şi nu sunt divizibile cu y (valorile x şi y se citesc de la tastatură)')
x=int(input("x="))
y=int(input("y="))
v=[]
for i in a:
    if((i>x)and(i%y!=0)):
        g=i
        v.extend([g])
print(v)
print('h)  afişează pe ecran doar componentele care sunt mai mari ca x şi mai mici decât y (valorile x şi y se citesc de la tastatură)')
vl=[]
for i in a:
    if ((i>x)and(i<y)):
        z=i
        vl.extend([z])
print(vl)
print('i) afiseaza pe ecran pozitiile(indicii) componentelor impare negative')
u=[]
for i in impare:
    if i<0:
        u.extend([a.index(i)])
print(u)
print('j)  afişează pe ecran poziţiile (indicii) componentelor ce conţin doar două cifre semnificative')
l=[]
for i in range(0,n):
    if ((a[i]>9)and(a[i]<100))or((a[i]>-100)and(a[i]<-9)):
     l.extend([i])  
print(l) 
print('k)  înlocuieşte prima componentă a tabloului cu componenta de valoare minimă din tabloul respectiv')
w=[]
for i in range(0,len(a)):
    y=a[i]
    w.extend([y])
t=min(w)
w[0]=t
print(w)
print('l)  înlocuieşte componenta de valoare minimă din tabloul respectiv cu prima componentă a acestuia')
z=[]
for i in range(0,len(a)):
    y=a[i]
    z.extend([y])
t=min(z)
z[z.index(min(z))]=z[0]
print(z)
print('m)  creează un tablou nou, format doar din componentele pare ale tabloului introdus de la tastatură')
s=[]
for i in range(0,len(a)):
    if a[i]%2==0:
        y=a[i]
        s.extend([y])
print(s)
print('n)  creează un tablou nou, format doar din componentele divizibile cu 3 ale tabloului introdus de la tastatură')
divizibile=[]
for i in range(0,len(a)):
    if a[i]%3==0:
        y=a[i]
        divizibile.extend([y])
print(divizibile)
print('o)  creează un tablou nou, format doar din acele componente ale tabloului introdus de la tastatură care au cel mult patru divizori')
k=[]
for i in a:
    if i>0:
        n=0
        for q in range(1,i+1):
            if (i%q==0):
               n+=1
        if n<=4:
            k.extend([i])
print(k)