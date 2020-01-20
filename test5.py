#Το πρόγραμμα θα λειτουργήσει σωστά,
#αν το κειμενο του αρχείου έχει μόνο κενά
#και όχι σύμβολα ή αλλαγή γραμμής
list1=list2=[]
f = open('text.txt','r')
for line in f:
    list1 = line.split()
f.close()
for i in list1:
    if len(i)>3:
        x = i[1:len(i)]    
        i = x+i[0]+'ay'
        list2.append(i)
print (list2)
