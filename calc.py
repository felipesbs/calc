def mas(v,m):
    return v + m
def men(v,m):
    return v - m
def por(v,m):
    return v * m
def div(v,m):
    return v / m

v = int(input("Ingrese un numero entero: "))
#v= 8
m = int(input("Ingrese un numero entero: "))
#m=10
print("suma", mas(v,m))
print("resta", men(v,m))
print("multiplicacion", por(v,m))
print("division", div(v,m))