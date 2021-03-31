#2. Stwórz dwie zmienne s1 i s2 przechowujące dowolne wyrazy, utwórz nowy łańcuch s3, dołączając s2 w środku s1.
s1 = "siostra"
s2 = "brat"
s3 = s1[0:3] + s2 + s1[3:]
print(s3)