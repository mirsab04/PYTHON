
a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))
c = int(input("Enter Third Number : "))
r = (b**2) - 4*a*c

root_1 = (-b + (r)**(1/2)) / (2*a)
root_2 = (-b - (r)**(1/2)) / (2*a)

print(f' x = {root_1} & x = {root_2}')



