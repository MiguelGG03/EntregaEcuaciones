from clases.ejercicio1 import main1
from clases.ejercicio2 import main2
from clases.ejercicio3 import main3
from clases.ejercicio4 import main4


def main():
    sigue=True
    while(sigue==True):
        pr1=input('Consulte el numero de ejercicio en el readme y elija uno\n>>>')
        print('\n\n')
        if(pr1=='1'):
            main1()
        elif(pr1=='2'):
            main2()
        elif(pr1=='3'):
            main3()
        elif(pr1=='4'):
            main4()
        else:
            print('SOLO NUMEROS DEL 1 AL 4')
        print('\n\n')
        pr2=input('Desea continuar (s)(n)\n>>>')
        if(pr2=='s' or pr2=='S'):
            sigue=True
        elif(pr2=='n' or pr2=='N'):
            sigue=False
            print('\n\nApagando...')
        else:
            return Exception('La respuesta debe ser una S o una N')