'''
Conversion de temperaturas de grados 
Fahrenheit a Celsius y viseversa
F=(C*1.8)+32 /// C=(F-32)/1.8
'''
def Fa_a_Cels(Fa):#Convertir de Fahrenheit a Celsius
    Cels=(Fa-32)/1.8
    print("La cantidad es: ",Cels," grados Celsius")#Impresion de resultado
    return Cels

def Cels_a_Fa(Cel):#Convertir de Celsius a Fahrenheit 
    Fah=(Cel*1.8)+32
    print("La cantidad es: ",Fah," grados Fahrenheit")#Impresion de resultado
    return Fah

#Ingreso de los datos
print(Fa_a_Cels)
Fa_a_Cels(Fa=float(input("Por favor ingrese los grados Fahrenheit: ")))

print(Cels_a_Fa)
Cels_a_Fa(Cel=float(input("Por favor ingrese los grados Celsius: ")))
