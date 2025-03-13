#SLICING
str_1 = 'COMPUTERS'
A = str_1[4:8:1]
B = str_1[7:3:-1]
print(A)
print(B)

#QUESTION ABOUT SLICING
#QNO.01
#OUTPUT : 01 : CHN
#OUTPUT : 02 : 'TAVONNI'
#OUTPUT : 03 : 'NOLOGY'
#OUTPUT : 04 : 'TECH OF LOGY'
str_2 = 'TECHNOLOGYANDINNOVATION'
a = str_2[:4]
b = str_2[19:12:-1]
c = str_2[4:10]
d = str_2[:4] + ' OF ' + str_2[6:10]
print(a)
print(b)
print(c)
print(d)

#QNO.02
#OUTPUT : 1 : ‘RAH’
#OUTPUT : 2 : ‘PYWIT’
#OUTPUT : 3 : ‘WITH OF PRO’
#OUTPUT : 4 : ‘GRAMM’
str_3 = 'PROGRAMMINGWITHPYTHON'
e = str_3[4:6] + 'H'
f = str_3[15:17]+ str_3[11:14]
g = str_3[11:15] + ' OF ' + str_3[:3]
h = str_3[3:8]
#Length
print("The Length Of String Is : " , len(str_3))
print(e)
print(f)
print(g)
print(h)


#METHODS OF STRING
str_4 = 'computer'
str_5 = 'This is a Python CLass'
str_6 = 'this is python class. this is our fifth class'
list_1 = ['This', 'is', 'a', 'Python', 'CLass']
#UPPR METHOD
print(str_4.upper())
print(str_5.upper())
#LOWER METHOD
print(str_4.lower())
print(str_5.lower())
#CAPITALIZE METHOD
print(str_4.capitalize())
#TITLE METHOD
print(str_6.title())
#COUNT METHOD
print(str_6.count('s'))
#SPLIT METHOD
print(str_5.split())
#JOIN METHOD
print("_".join(list_1))
