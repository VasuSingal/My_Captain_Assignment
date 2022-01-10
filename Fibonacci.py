nterms= int(input("How many terms ? "))

n1=0 ; n2=1
count=0

if nterms<0:
    print("Enter positive value!")

elif nterms==0:
    print(n1)

elif nterms==1:
    print(n2)

else:
    while count<nterms:
        print(n1)
        n = n1 + n2
        n1 = n2
        n2 = n
        count = count + 1