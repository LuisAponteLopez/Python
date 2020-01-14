print("__________________________________________________________")
print("\nEste programa calcula el promedio de la suma de numeros")
print("__________________________________________________________")

numeroSuma = 0 #se empieza en 0 para que la variable se pueda sumar cuando le ingresemo los numero que se desea sacar promedio
cantidad = eval(input("A cuanto numero usted quiere calcularle el promedio: "))#le pregunta al usuario cuanto numero quiere calcular para asi poder definir el rango de ciclo y el numero que va a dividir la suma de los numero ingresado.
contador = 1 #esta variable ayuda al usuario a saber por cual numero va.

for i in range (cantidad ):
    numero=eval(input("Ingres el numero " + str(contador) +" : "))# + str(contador) le dice al usuario el por que numero va 
    numeroSuma=numeroSuma + numero # suma todos los numeros ingresado por el usuario y lo guarda en la variable numeroSuma
    contador = contador + 1 #ante de terminar el ciclo el contador aumenta un valor 


promedio = numeroSuma/cantidad 
print("\nEl promedio de los" ,cantidad," numero es ",round(promedio,2),".")# se utiliza el round(promedio,2) por si el promedio no es un entero no  los de a 2 espacio decimal
print("\nGacias por utilzar el programa.Regrese pronto.")
