from pickle import STOP
from tkinter import*
from tkinter  import Tk, ttk
from tracemalloc import stop
from turtle import reset


janela = Tk()
janela.title("Cronômetro")
janela.geometry('300x180')
janela.configure(background ='black')
janela.resizable(width=FALSE, height=FALSE)

global tempo
global rodar
global contador
global limitador

limitador = 59
tempo = "00:00:00"
rodar = FALSE
contador = -5 



def iniciar():
    global tempo
    global contador
    global limitador

    if rodar:
        if contador <=-1:
            inicio = 'Comecando em ' +str(contador)
            label_time['text'] = inicio
            label_time['font'] = 'verdana 10'
        else:
             label_time['font'] = 'times 50 bold'

             temporaria = str(tempo)
             h,m,s =map(int,temporaria.split(":"))
             h = int(h)
             m = int(m)
             s = int(contador)

             if (s>=limitador):
                contador = 0
                m+=1
            
             s = str(0)+str(s)
             m = str(0)+str(m)
             h = str(0)+str(h)

             temporaria = str(h[-2:])+":" + str(m[-2:]) + ":" + str(s[-2:])
             label_time['text'] = temporaria
             tempo = temporaria



        label_time.after(1000,iniciar)
        contador +=1


def star():
    global rodar
    rodar = TRUE
    iniciar()


def parar():
    global rodar
    rodar = FALSE
   
def reiniciar():
    global contador
    global tempo

    contador = 0
    tempo = "00:00:00"
    label_time['text'] = tempo
    
 

label_app= Label(janela, text='Cronômetro',  font=('verdana 10'), bg='black', fg='white')
label_app.place(x=20, y=5)

label_time= Label(janela, text=tempo, font=('times 50 bold'), bg='black', fg='green')
label_time.place(x=20, y=30)

botao_iniciar =Button(janela,command=star, text='Iniciar', width=10, height=2, bg='black', fg='white', font=('verdana 8 bold'), relief='raised', overrelief='ridge')
botao_iniciar.place(x=20, y=130)


botao_pausar =Button(janela,command=parar, text='Pausar', width=10, height=2, bg='black', fg='white', font=('verdana 8 bold'), relief='raised', overrelief='ridge')
botao_pausar.place(x=105, y=130)

botao_stop =Button(janela,command=reiniciar, text='Reiniciar', width=10, height=2, bg='black', fg='white', font=('verdana 8 bold'), relief='raised', overrelief='ridge')
botao_stop.place(x=190, y=130)



janela.mainloop ()