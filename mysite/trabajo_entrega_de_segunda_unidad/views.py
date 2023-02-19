from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def total1(request,*cadena,**cadenaID):
    #PROBLEMA1 DE FOR
    cont=0
    for cont in range(6):
      cont=cont+1
      


    #PROBLEMA2 DE FOR
    division=[]
    for i in range(0,20):
     if i%3==0:
        division.append(i)
       
   
    #PROBLEMA3 DE FOR

    al=[1,2,3,4,5]
    acum = 0
    for e in al:
     acum += e
    


    #PROBLEMA4 DE FOR
    multiplicandos=[]
    for i in range(11):
        multiplicandos.append(i)


    #PROBLEMA5 DE FOR
    pares=[]
    for i in range(100):
        if i%2==0 : 
         pares.append(i)
    
    
    #PROBLEMA1 DE WHILE
    suma = 0
    contador = 0
    numero = 1
    while numero <= 20:
     suma += numero
     contador += 1
     numero += 1
     promedio = suma / contador 
     print(promedio)

    
    

    #PROBLEMA2 DE WHILE
    factorial1 = 1
    i = 1
    while i <= 10:
     factorial1 =factorial1*i
     i =i+1
     print(factorial1)
    
    #PROBLEMA3 DE WHILE
    numero = 185
    inversa = 0

    while numero != 0:
     residuo = numero % 10
     inversa = (inversa * 10) + residuo
     numero //= 10

    print(inversa)

    #PROBLEMA4 DE WHILE
    i = 1
    suma = 0
    while i <= 20:
     suma += i
     i += 1
     print(suma)
    
    #PROBLEMA5 DE WHILE
    reco=[]
    i = 11
    while i >= 1:
     i -= 1
     reco.append(i)

    #PROBLEMA 1 DE DO-WHILE
    razona=[]
    i = 0
    while True:
     i =i+ 1
     if i > 10:
        break
     razona.append(i)

    #PROBLEMA 2 DE DO-WHILE
    dados=[]
    i = 0
    while True:
     i =i+ 2
     if i > 20:
        break
     dados.append(i)
    #PROBLEMA 3 DE DO-WHILE
    desce=[]
    i = 21
    while True:
     i -= 1
     if i < 0:
        break
     desce.append(i)
    #PROBLEMA 4 DE DO-WHILE
    alea=[]
    import random
    num = 0
    while True:
     num = random.randint(1, 10)
     if num == 4:
        break
     alea.append(num)
    #PROBLEMA 5 DE DO-WHILE
    suma = 0
    contador = 0
    numero = 1
    while True:
     prome=float()
     suma += numero
     contador += 1
     numero += 1
     prome = suma / contador 
     if numero== 21:
      break
     
    


     
    return render(request,'for.html',{'multiplicacion': cont,'numeros': division , 'suma': acum,'tabla': multiplicandos,'par': pares,'prom': promedio,'fac1' : factorial1,'inv': inversa,'adicion':suma,'retro':reco , 'do1':razona,'do2':dados,'do3':desce,'do4':alea,'do5':prome}) 