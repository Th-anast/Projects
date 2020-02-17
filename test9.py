x = int(input("Δώσε έναν αριθμό: "))
s = x*3+1
while len(str(s))!=1:
  x1 = s//100
  y = s%100
  x2 = y//10
  x3 = y%10
  s = x1+x2+x3
print(s)
