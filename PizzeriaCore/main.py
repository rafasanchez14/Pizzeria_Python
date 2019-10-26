import Calculate.Calculate as calc
import Util.Util as ut
import Data.Data as dat
import Factura.GenFactura as fact
import os 

#Funcion que permite seleccionar el tamaño de la pizza
def SeleccionarTamaño():

    pizza_titulo = ''' 
____________________________
       Pizza #   @numero           
____________________________ '''
    #numero de pizza mostrado en diseño
    print (pizza_titulo.replace('@numero',str(len(orderListAdd_Total)+1)))
    print('Seleccione tamaño:')

    #Menu dinamico segun data
    for tam in dat.lSize():
        print("-",tam.get('descrip'),"(",tam.get('cod'),")")

    stam_pizza = input()
    #busca el codigo del tamaño selecionado para saber si es valido
    findSize = list(filter(lambda tam: tam['cod'] == stam_pizza.upper(), dat.lSize()))
    if findSize:
      print('Seleccionado pizza',findSize[0].get('descrip'))
      print('Seleccione Adicional o Enter para seguir:')
      objadd = SeleccionarAdicional(1)
      print('Ingredientes adicionales elegidos:') 
      for det in objadd:
        print(det.get('descrip'))


      thisobject = {
    "size": findSize[0], 
    "addon": objadd.copy(),
    }
      calc.CalcularSubTotal(thisobject.copy())
      orderListAdd_Total.append(thisobject.copy())

    else:
        print('Debe seleccionar un tamaño valido.. Presione una tecla para continuar')
        input()
        ut.LimpiarPantalla()
        SeleccionarTamaño()

    antoher = input("Desea Agregar otra pizza? (S/N..) => ")
    if (antoher.upper()=='S'):
        objadd.clear()
        SeleccionarTamaño()
    else:
        tasa = input('inserte tasa mayor a 1 para ver  en divisas=> ')
        if (tasa.isdigit()):
            if (int(tasa)>1):
                calc.CalcularTotal(orderListAdd_Total,tasa)
            else:
                calc.CalcularTotal(orderListAdd_Total)
        else:
            calc.CalcularTotal(orderListAdd_Total)
       #print(orderListAdd_Total)



#funcion que se encarga de añadir adicionales a la pizza elegida si es 1 muestra encabezado por primera vez
def SeleccionarAdicional(menu=0):

     #Menu dinamico segun data
    if (menu):
      for add in dat.lAddons():
            print("-",add.get('descrip'),"(",add.get('cod'),")")
    sadic_pizza = input('=>')

   
   
    if sadic_pizza !='':
        #busca el codigo del addon selecionado para saber si es valido
        findAdd = list(filter(lambda add: add['cod'] == sadic_pizza.upper(), dat.lAddons()))
        if findAdd: 
            orderListAdd.append(findAdd[0])
            SeleccionarAdicional()
        else:
                print('Debe seleccionar un adcional valido.. Presione una tecla para continuar')
                input()
                SeleccionarAdicional()
    else:
        pass
    return orderListAdd


def Titulo():
   ut.LimpiarPantalla()
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
88         88      d8'     d8'   88      88`8b      88    88   88 
88        .88.    d8' db  d8' db 88.     88 `88.   .88.   88   88 
88      Y888888P d88888P d88888P Y88888P 88   YD Y888888P YP   YP 
   ''')

#Variables de inicializacion y globales
Titulo()
orderListAdd = []
orderListAdd_Total = []
SeleccionarTamaño()
fact.Generate_Comprobante(orderListAdd_Total)
print('Gracias por su compra')

#documentar 
#trabajo