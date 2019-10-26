import random
from datetime import date
import os
import Calculate.Calculate as cal
def GenerateCodFact():
    numcode= random.randint(1000, 999999)
    today = date.today()
    today = today.strftime('%d-%m-%Y')
    value= 'FACT'+str(numcode)+today+'.txt'
    return value

def Generate_Comprobante(lodata):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname+r'\Comprobante\\')
    print('Su orden esta disponible en:',filename)
    f= open(filename+GenerateCodFact(),'w+')
    for idx, sizes in enumerate(lodata):
        f.writelines('PIZZA #'+str(idx+1)+'\n')
        f.writelines(sizes.get('size').get('descrip')+' = '+str(sizes.get('size').get('precio'))+'\n')
        for add in sizes.get('addon'):
             f.writelines(' *'+add.get('descrip')+' = '+str(add.get('precio'))+'\n')
        f.write('\n')
        f.write(cal.CalcularTotal_fact(lodata))
    f.close()