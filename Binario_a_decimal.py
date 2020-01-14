# =============================================================================
# convierte de binario a enteros
# =============================================================================



def Decimal():
   
    #the usuario enter number
    
    numeroBin = input("Enter de number in binary: ")
    lennumber = len(numeroBin)
    numeroBin.split()
    
    decimal = 0
    exp = lennumber -1
    
    for i in range(lennumber):
        
        decimal = decimal + int(numeroBin[i])*2**exp
        exp-=1
    
    print(decimal)
   
    
    
    
    
Decimal()
    
