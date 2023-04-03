from tkinter import *
from tkinter import Tk, ttk
from  tkinter import messagebox

#cores
co0 = "black"
co1 = "white"
co2 = "green"
co3 = "#38576b"
co4 = "#403d3d"

#Criando a janela

janela = Tk()
janela.title('Sistema de Login')
janela.geometry("310x310")
janela.config(background=co1)
janela.resizable(width=FALSE, height=FALSE) #fixa o tamanho

#Frame 1 -> Cima

frame_cima = Frame(janela, width=310, height=50, bg= co1, relief='flat')
frame_cima.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

#Frame 2 -> Baixo

frame_baixo = Frame(janela, width=310, height=250, bg= co1, relief='flat')
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

#==============================================================================
#Configurações do Frame de Cima

label_name = Label(frame_cima, text= 'Login', anchor=NE, font=('Arial', 25), bg=co1, fg=co0)
label_name.place(x=5, y=5)

label_linha = Label(frame_cima, text='', width=40, anchor=NW, bg=co2, fg=co4)
label_linha.place(x=10, y=45)

#======================================================
#configurando o frame debaixo

label_name = Label(frame_baixo, text='Nome:', anchor=NW, font=('Arial', 15), bg=co1, fg=co4)
label_name.place(x=10, y=20)

entry_name = Entry(frame_baixo, width=22, justify='left', font=(',15'),highlightthickness=1,relief='solid')
entry_name.place(x=10, y=50)

label_senha = Label(frame_baixo, text='Senha:', anchor=NW, font=('Arial', 15), bg=co1, fg=co4)
label_senha.place(x=15, y=90)

entry_senha = Entry(frame_baixo, width=22, justify='left', font=(',15'),highlightthickness=1,relief='solid')
entry_senha.place(x=15, y=115)


def muda_label():
    botao.config( text = 'Cadastro Efetuado', foreground='black', background='green', font = ('Arial', 10))

botao = Button(
    frame_baixo, width=22,
    justify='left',
    highlightthickness=1,
    relief='solid',
    text = 'Cadastrar',
    font=('Arial', 10),
    command=muda_label
)
    
botao.place(x=20, y=150)

#fazer um botão

janela.mainloop()


