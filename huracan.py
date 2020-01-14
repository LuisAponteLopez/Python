# El trabajo de este programa es ayudar a las personas a saber por lo viento si el fenomeno atmoferico es deprecio , tormenta o huracan y si es hurancan nos dira la categoria .


print("Esta en un medidor de categoria de huracanes\n Ingresa la velocidad de los viento ")
viento= int(input())

if viento<35:
               print("Es deprecion tropical")
elif viento<74:
               print("Es una tormenta tropical")
elif viento<96:
              print ("Es categoria 1")
elif viento<111:
              print("Es categoria 2")
elif viento<131:
              print("Es categoria 3")
elif viento<156:
              print("Es categoria 4")
else :
                  print("Es categoria 5 ")
                  
