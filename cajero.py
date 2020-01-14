a = 50*str("*")





print(a)
print("\nBIENVENIDO\n")

print("\nEsta usando el cajero python\n")
print(a)

intruccion = "si"
while intruccion == "si":
#lo que el usuario tiene que pagar
    total = float(input("Ingrese el total: "))
    
    #la cantidad que da
    cantidad = float(input("Ingrese el total: "))
    
    #el cambio con condiciones
    
    cambio = cantidad - total
    print("\nSe le debe devolver al cliente un total de: " , cambio)
    
    dolar = 0
    peceta = 0
    dime = 0
    vellon = 0
    peni = 0




    while cambio > 0:
        
        if cambio >= 1:
            dolar = dolar + 1
            cambio = cambio-1
            
            
        elif cambio >= .25:
            peceta = peceta + 1
            cambio  =cambio - .25
            
        
        elif cambio >= .10:
            dime =  dime + 1
            cambio = cambio - .10
        
        elif cambio >= .05:
            vellon = vellon + 1
            cambio = cambio - .05
       
        elif cambio >= .01:
            peni = peni + 1
            cambio = cambio - .01
        
        else:
            break
    



    
#lo que nos devulve
    

    print("\ndolar: "+str(dolar)+"\npeceta: "+str(peceta)+"\ndime: "+str(dime)+"\nvellon: "+str(vellon)+"\npeni: "+str(peni))
    
    intruccion = input("Repetir(si /no): ")
    

print("\nGracias por utilizar el programa.\nRegrese pronto.")
