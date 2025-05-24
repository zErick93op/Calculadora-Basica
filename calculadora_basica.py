print('CALCULADORA BASICA')
#definimos las variables 

num1 = float(input('Ingresa El Primer Numero: '))
operadores = input('Elige el Operador +,-,*,/: ')
num2 =float(input('Ingresa El Segundo Numero: '))

#Hacemos Practica de las condicionales if,elif,else

if operadores not in ('+','-','*','/'):  #Aqui ponemos la condicion que si la variable "operadores" 
    print('Operador Invalido')            #no contiene los siguientes volares imprima "Operador Invalido"

#Aplicamos la respectivas condiciones para que funcione correctamente la calculadores

if operadores == '+':
    print('La Suma es:', num1+num2)
elif operadores == '-':
    print('La resta es:' , num1-num2)
elif operadores == '*':
    print('La Multiplicacion es:', num1*num2)
else:
    if num2 !=0:                              #Aqui usamos !=0 ya que la division no puede ser divisible por 0
        print('La Division es:', num1 / num2)
    else:
        print('Division Invalida')

