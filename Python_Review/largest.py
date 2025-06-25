print("Enter three numbers:")
a,b,c = int(input()), int(input()), int(input())
if a >b and a >c:
    print("Largest number is:", a)
elif b >a and b >c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)