import os 
import shutil

def comprobar(archivo):
    tamano=len(archivo)
    for x in range(tamano):
        if archivo[x]=='(' and archivo[x+1]=='C' and archivo[x+2]==')':
            shutil.move('/Users/artur/Downloads/'+archivo, '/Users/artur/Desktop/UNIVERSIDAD/Q2/Calcul 2')
            print(archivo)
        if archivo[x]=='(' and archivo[x+1]=='D' and archivo[x+2]==')':
            shutil.move('/Users/artur/Downloads/'+archivo, '/Users/artur/Desktop/UNIVERSIDAD/Q2/DibujoTecnico')
            print(archivo)
        if archivo[x]=='(' and archivo[x+1]=='E' and archivo[x+2]==')':
            shutil.move('/Users/artur/Downloads/'+archivo, '/Users/artur/Desktop/UNIVERSIDAD/Q2/Espcacio aereo y navegacion')
            print(archivo)
        if archivo[x]=='(' and archivo[x+1]=='F' and archivo[x+2]==')':
            shutil.move('/Users/artur/Downloads/'+archivo, '/Users/artur/Desktop/UNIVERSIDAD/Q2/Fisica2')
            print(archivo)
        if archivo[x]=='(' and archivo[x+1]=='Q' and archivo[x+2]==')':
            shutil.move('/Users/artur/Downloads/'+archivo, '/Users/artur/Desktop/UNIVERSIDAD/Q2/quimica')
            print(archivo)
while True:
    lista=(os.listdir('/Users/artur/Downloads'))
    for x in lista:
        comprobar(x)
        
       