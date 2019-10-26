#Calcula subtotal por pizza elegida
def CalcularSubTotal(odata):
    #obtiene precio del la lista de tamaños
    subTotal_tam = odata.get('size').get('precio')
    #obtiene descripcion
    sdescrip    =  odata.get('size').get('descrip')
    laddon = odata.get('addon')

    #Suma los precios addons de esa lista
    subTotal_add = sum(item['precio'] for item in laddon)
    subTotal = subTotal_tam + subTotal_add
    print ("Subtotal a pagar por una pizza",sdescrip.strip(),":",subTotal)

#Funcion que reorna el total de la orden 
def CalcularTotal(lodata,factor=1.0):
    total_addon = 0
    total_tam = 0

    #Recorre la lista de diccionarios buscando y sumando para los tamañas
    total_tam = sum(sizes.get('size').get('precio') for sizes in lodata)

    #Recorre la lista de diccionarios buscando y sumando el campo precio de la lista de addons
    for sizes in lodata:
      total_addon += sum(sizes.get('precio') for sizes in sizes.get('addon'))
    
    total = total_addon + total_tam
    total = float(total)/float(factor)
    print ("Total a pagar por",len(lodata),"pizza(s):",total)

#funcion que calcula pero devuelve formato para archivo
def CalcularTotal_fact(lodata):
    total_addon = 0
    total_tam = 0

    #Recorre la lista de diccionarios buscando y sumando para los tamañas
    total_tam = sum(sizes.get('size').get('precio') for sizes in lodata)

    #Recorre la lista de diccionarios buscando y sumando el campo precio de la lista de addons
    for sizes in lodata:
      total_addon += sum(sizes.get('precio') for sizes in sizes.get('addon'))
    
    total = total_addon + total_tam
    return ("Total "+str(len(lodata))+" pizza(s): "+str(total))