
import os 

#Funcion que permite seleccionar el tamaño de la pizza
def SeleccionarTamaño():
    Titulo()

    print ('Pizza #',len(orderListAdd_Total)+1)
    print('Seleccione tamaño:')

    for tam in lSize:
        print("-",tam.get('descrip'),"(",tam.get('cod'),")")

    stam_pizza = input()
    findSize = list(filter(lambda tam: tam['cod'] == stam_pizza.upper(), lSize))
    if findSize:
      print('Seleccionado pizza',findSize[0].get('descrip'))
      objadd = SeleccionarAdicional(1)

      thisobject = {
    "size": findSize[0], 
    "addon": objadd.copy(),
    }
      CalcularSubTotal(thisobject.copy())
      orderListAdd_Total.append(thisobject.copy())

    else:
        print('Debe seleccionar un tamaño valido.. Presione una tecla para continuar')
        input()
        LimpiarPantalla()
        SeleccionarTamaño()

    antoher = input("Desea Agregar otra pizza? (S/N..)")
    if (antoher.upper()=='S'):
        objadd.clear()
        SeleccionarTamaño()
    else:
       CalcularTotal(orderListAdd_Total)
       #print(orderListAdd_Total)




def SeleccionarAdicional(menu=0):
    #LimpiarPantalla()
    print('Seleccione Adicional o Enter para seguir:')

    if (menu):
      for add in lAddons:
            print("-",add.get('descrip'),"(",add.get('cod'),")")
    sadic_pizza = input()

   
   
    if sadic_pizza !='':
        findAdd = list(filter(lambda add: add['cod'] == sadic_pizza.upper(), lAddons))
        if findAdd: 
            orderListAdd.append(findAdd[0])
           
            print('Ingredientes adicionales elegidos:') 
            for det in orderListAdd:
              print(det.get('descrip'))

            SeleccionarAdicional()
        else:
                print('Debe seleccionar un adcional valido.. Presione una tecla para continuar')
                input()
                SeleccionarAdicional()
    else:
        pass
    return orderListAdd


def CalcularSubTotal(odata):
    subTotal_tam = odata.get('size').get('precio')
    sdescrip    =  odata.get('size').get('descrip')
    laddon = odata.get('addon')
    subTotal_add = sum(item['precio'] for item in laddon)
    subTotal = subTotal_tam + subTotal_add
    print ("Subtotal a pagar por una pizza",sdescrip.strip(),":",subTotal)

def CalcularTotal(lodata):
    total_addon = 0
    total_tam = 0
    total_tam = sum(sizes.get('size').get('precio') for sizes in lodata)

    for sizes in lodata:
      total_addon += sum(sizes.get('precio') for sizes in sizes.get('addon'))
    
    total = total_addon + total_tam
    print ("Total a pagar por",len(lodata),"pizza(s):",total)
       

     
#Funcion que limpia pantalla para sistemas windows
def LimpiarPantalla():
     clear = lambda: os.system('cls')
     clear()

lSize = [
{
  "cod": "G",
  "descrip": "Grande   ",
  "precio": 580.0
},
{
  "cod": "M",
  "descrip": "Mediana  ",
  "precio": 430.0
},
{
  "cod": "P",
  "descrip": "Personal ",
  "precio": 280.0
}]

lAddons = [
{
  "cod": "JA",
  "descrip": "Jamon      ",
  "precio": 40.0
},
{
  "cod": "CH",
  "descrip": "Champiñones",
  "precio": 35.0
},
{
  "cod": "PI",
  "descrip": "Pimenton   ",
  "precio": 30.0
},
{
  "cod": "DQ",
  "descrip": "Doble Queso",
  "precio": 40.0
},
{
  "cod": "AC",
  "descrip": "Aceitunas  ",
  "precio": 58.0
},
{
  "cod": "PP",
  "descrip": "Pepperoni  ",
  "precio": 38.5
},
{
  "cod": "SA",
  "descrip": "Salchichon ",
  "precio": 62.5
}]
def Titulo():
   LimpiarPantalla()
   print('''  
db       .d8b.  
88      d8' `8b 
88      88ooo88 
88      88~~~88 
88booo. 88   88 
Y88888P YP   YP 
                
                
d8888b. d888888b d88888D d88888D d88888b d8888b. d888888b  .d8b.  
88  `8D   `88'   YP  d8' YP  d8' 88'     88  `8D   `88'   d8' `8b 
88oodD'    88       d8'     d8'  88ooooo 88oobY'    88    88ooo88 
88~~~      88      d8'     d8'   88~~~~~ 88`8b      88    88~~~88 
88        .88.    d8' db  d8' db 88.     88 `88.   .88.   88   88 
88      Y888888P d88888P d88888P Y88888P 88   YD Y888888P YP   YP 
   ''')
orderListAdd = []
orderListAdd_Total = []
SeleccionarTamaño()


#documentar 
#modular
#trabajo