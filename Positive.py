num = input("Enter list of numbers in a,b,c format =")

list = num.split(',')

positive=[]

for n in list :
    if int(n) > 0:
     positive.append(n)

print(positive)