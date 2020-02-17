def convert(x):
  n =  ''
  for i in x:
    a = ord(i)
    n += str(a)
  num = int(n)
  print (num)
  for i in range(2,num): 
    if num%i != 0:
      print ("Το",num,"ειναι πρώτος αριθμός.")
    else:
      print ("Το",num,"δεν ειναι πρώτος αριθμός.")
    break

convert('dog')
