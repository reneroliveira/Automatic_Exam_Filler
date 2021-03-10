import io
import os
import pdfrw
import time
import glob
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm,mm
from functions import split,transform

space = 2.4*mm
space_q = (2.6*mm,4.5*mm)
max_h = 296.93*mm
w = -38.6*mm + 42.7*mm#-0.02*mm
h = (125.7*mm - 121.9*mm)#+1*mm
# print(h,w)
start_id = (35.7*mm, max_h-135.3*mm+0.45*mm)
start_q = (36.8*mm,max_h-208.3*mm+0.45*mm)
error = 0.25*mm
x_name = 110*mm
y_name = 171*mm

parameters = [space,space_q,max_h,w,h,start_id,start_q,error,x_name,y_name,y_name]

def run():
    cwd = os.getcwd()
    print("Selecionando pdf mais recente ...")
    time.sleep(1.5)
    files = glob.glob(cwd+"/*.pdf")
    files.sort(key=os.path.getmtime, reverse=True)
    arq = files[0]
    print(f"{arq[len(cwd):]} selecionado!")
    time.sleep(.5)
    
    while True:
        try:
            page = int(input("Página do Seu Gabarito: "))
            break
        except:
            print("Digite um número!!\n")

    
    while True:
        try:
            id = input("Matrícula: ")
            int(id)
            break
        except:
            print("Digite apenas números")
    while True:
        quest = input("Gabarito (sem espaços):")
        quest = quest.split()
        if len(quest)==1:
            quest=quest[0]
            break
        else:
            print("Digite suas Respostas sem espaços!!")

    
    name = input("Nome e Sobrenome: ")
    output = "Gabarito_"+"_".join(name.split())
    split(arq, page, output+".pdf")
    transform(id,quest,output,name,parameters)
    
    




# if __name__ == '__main__':
run()
