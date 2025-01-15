from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import webbrowser
from PIL import Image, ImageTk
from tkinter import filedialog as fd

import sqlite3

from tkcalendar import Calendar, DateEntry
from datetime import date
from criardb import *


#cores
cor1 = "#87c7f5"
cor2 = "#a5d5f7"
cor3 = "#c3e3fa"
cor4 = "#e1f1fc"
cor5 = "#ffffff" 
cor6 = "#000000"

#FONTES --------------------------------

# Criar a janela principal
janela = Tk()
janela.title('')
janela.geometry('1040x600')
janela.configure(background=cor1)
janela.resizable(False, False)

# Configurar o tema antes de criar os widgets ttk
style = ttk.Style(janela)
style.theme_use("clam")

frame_logo = Frame(janela, width=1020, height=60, bg=cor1)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW, columnspan=5)

frame_details = Frame(janela, width=1020, height=211, bg=cor4, relief=SOLID)
frame_details.grid(row=1, column=0, pady=1, padx=10, sticky=NSEW)

frame_tabela = Frame(janela, width=950, height=200, bg=cor5, relief=SOLID)
frame_tabela.grid(row=2, column=0, pady=0, padx=10, sticky=NSEW, columnspan=5)

frame_button = Frame(janela, width=120, height=72, bg=cor4, relief=RAISED)
frame_button.grid(row=3, column=0, pady=2, padx=10, sticky=NSEW)

#Manipulando logo

global imagem, imagem_string, l_imagem

app_lg = Image.open('Cadastro.png')
app_lg = app_lg.resize((45,45))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, text= "    SISTEMA DE CADASTRO MORADORES ", image=app_lg, width=700, compound=LEFT, anchor=NW, font=('Montserrat', 18, 'bold'), bg=cor1, fg=cor5)
app_logo.place(x=3, y=3)


#ABRIR IMAGEM
# 
imagem = Image.open('cadastro.png')
imagem = imagem.resize((145,145))
imagem = ImageTk.PhotoImage(imagem)
l_imagem = Label(frame_details, image=imagem, bg=cor5, fg=cor3)
l_imagem.place(x=780, y=27)

#CRUD FUNÇÕES ------------------------------------------------------------------------------------------------------------------------------

def adicionar():
    global imagem, imagem_string, l_imagem
    
    nome = e_nome.get()
    email = e_email.get()
    tel = e_tel.get()
    bloco = e_bloco.get()
    apto = e_apto.get()
    data = e_dat_recebimento.get_date()
    dat = e_dat_entrega.get_date()
    responsavel = e_responsavel.get()
    status = c_status.get()
    img = imagem_string
    
    lista = [nome, email, tel, bloco, apto,  data, dat, responsavel, status, img]
    
    for i in lista:
        if i== '':
            messagebox.showerror('Erro', 'Prencha todos os campos')
            
            return
    sistema_de_resgitro.register_resident(lista)
    
    e_nome.delete(0, END)
    e_email.delete(0, END)
    e_tel.delete(0, END)
    e_bloco.delete(0, END)
    e_apto.delete(0, END)
    e_dat_recebimento.delete(0, END)
    e_dat_entrega.delete(0, END)
    e_responsavel.delete(0, END)
    c_status.delete(0, END)
    
    mostrar_moradores()
    
    
def procurar():
    
    global imagem, imagem_string, l_imagem
    
    #obter o ID
    id_morador = int(e_procurar.get())
    dados = sistema_de_resgitro.search_resident(id_morador)
    
    e_nome.delete(0, END)
    e_email.delete(0, END)
    e_tel.delete(0, END)
    e_bloco.delete(0, END)
    e_apto.delete(0, END)
    e_dat_recebimento.delete(0, END)
    e_dat_entrega.delete(0, END)
    e_responsavel.delete(0, END)
    c_status.delete(0, END)
    
    
    ##inserindo valores nos campo de entrada
    
    e_nome.insert(0, dados[1])
    e_email.insert(0, dados[2])
    e_tel.insert(0, dados[3])
    e_bloco.insert(0, dados[4])
    e_apto.insert(0, dados[5])
    e_dat_recebimento.insert(0, dados[6])
    e_dat_entrega.insert(0,dados[7])
    e_responsavel.insert(0, dados[8])
    c_status.insert(0, dados[9])
    
    imagem = dados[10]
    imagem_string = imagem
    
    imagem = Image.open(imagem)
    imagem = imagem.resize((145,145))
    imagem = ImageTk.PhotoImage(imagem)
    l_imagem = Label(frame_details, image=imagem, bg=cor5, fg=cor3)
    l_imagem.place(x=780, y=27)
    
    mostrar_moradores()
    
def atualizar():
    
    global imagem, imagem_string, l_imagem
    
    #obter o ID
    id_morador = int(e_procurar.get())
    
    nome = e_nome.get()
    email = e_email.get()
    tel = e_tel.get()
    bloco = e_bloco.get()
    apto = e_apto.get()
    data = e_dat_recebimento.get_date()
    dat = e_dat_entrega.get_date()
    responsavel = e_responsavel.get()
    status = c_status.get()
    
    img = imagem_string
    
    lista = [nome, email, tel, bloco, apto, data, dat,  responsavel, status, img, id_morador]
    
    for i in lista:
        if i== '':
            messagebox.showerror('Erro', 'Prencha todos os campos')
            
            return
    sistema_de_resgitro.update_resident(lista)
    #LIMPAR OS CAMPOS
    e_nome.delete(0, END)
    e_email.delete(0, END)
    e_tel.delete(0, END)
    e_bloco.delete(0, END)
    e_apto.delete(0, END)
    e_dat_recebimento.delete(0, END)
    e_dat_entrega.delete(0, END)
    e_responsavel.delete(0, END)
    c_status.delete(0, END)
    
    #ABRIR A IMAGEM
    
    imagem = Image.open('Cadastro.png')
    imagem = imagem.resize((145,145))
    imagem = ImageTk.PhotoImage(imagem)
    
    l_imagem = Label(frame_details, image=imagem, bg=cor5, fg=cor3)
    l_imagem.place(x=780, y=27)
    
    mostrar_moradores()

def deletar():
    
    global imagem, imagem_string, l_imagem
    
    
    id_morador = int(e_procurar.get())
    
    sistema_de_resgitro.delete_resident(id_morador)
    
    e_nome.delete(0, END)
    e_email.delete(0, END)
    e_tel.delete(0, END)
    e_bloco.delete(0, END)
    e_apto.delete(0, END)
    e_dat_recebimento.delete(0, END)
    e_dat_entrega.delete(0, END)
    e_responsavel.delete(0, END)
    c_status.delete(0, END)
     
    e_procurar.delete(0, END)
     
    imagem = Image.open('Cadastro.png')
    imagem = imagem.resize((145,145))
    imagem = ImageTk.PhotoImage(imagem)
    l_imagem = Label(frame_details, image=imagem, bg=cor5, fg=cor3)
    l_imagem.place(x=780, y=27)
    
    #Adicionar mensagem de erro.
    
    mostrar_moradores()

#FRAMES DETAILS
l_nome = Label(frame_details, text="Nome: * ", anchor=NW, font=('Montserrat', 12), bg=cor4, fg=cor6)
l_nome.place(x=15, y=10)
e_nome = Entry(frame_details, width=35, justify='left', relief="solid")
e_nome.place(x=18, y=35)

l_email = Label(frame_details, text="Email: * ", anchor=NW, font=('Montserrat', 12), bg=cor4, fg=cor6)
l_email.place(x=260, y=10)
e_email = Entry(frame_details, width=29, justify='left', relief="solid")
e_email.place(x=264, y=35)

l_tel = Label(frame_details, text="Telefone: * ", anchor=NW, font=('Montserrat', 12), bg=cor4, fg=cor6)
l_tel.place(x=315, y=70)
e_tel = Entry(frame_details, width=20, justify='left', relief="solid")
e_tel.place(x=320, y=95)

l_bloco = Label(frame_details, text="Bloco: * ", anchor=NW, font=('Montserrat', 12), bg=cor4, fg=cor6)
l_bloco.place(x=15, y=70)
e_bloco = Entry(frame_details, width=18, justify='left', relief="solid")
e_bloco.place(x=18, y=95)

l_apto = Label(frame_details, text="Apartamento: * ", anchor=NW, font=('Montserrat', 12), bg=cor4, fg=cor6)
l_apto.place(x=167, y=70)
e_apto= Entry(frame_details, width=18, justify='left', relief="solid")
e_apto.place(x=169, y=95)

l_responsavel = Label(frame_details, text="Responsável: * ", anchor=NW, font=('Montserrat', 12), bg=cor4, fg=cor6)
l_responsavel.place(x=15, y=145)
e_responsavel = Entry(frame_details, width=18, justify='left', relief="solid")
e_responsavel.place(x=18, y=175)

c_status = Label(frame_details, text="STATUS: *", anchor=NW, font=('Montserrat', 12), bg=cor4, fg=cor6)
c_status.place(x=167, y=145)
c_status = ttk.Combobox(frame_details, width=20, font=('Ivy 8 bold'),  justify='center')
c_status ['values'] = ('PENDENTE', 'ENTREGUE', 'AGUARDANDO', 'N/A')
c_status.place(x=170, y=175)

l_dat_recebimento = Label(frame_details, text="Data chegada: * ", anchor=NW, font=('Montserrat', 12), bg=cor4, fg=cor6)
l_dat_recebimento.place(x=316, y=145)
e_dat_recebimento = DateEntry(frame_details, width=17, justify='center', relief="solid")
e_dat_recebimento.place(x=320, y=175)

l_dat_entrega = Label(frame_details, text="Entrega cliente: * ", anchor=NW, font=('Montserrat', 12), bg=cor4, fg=cor6)
l_dat_entrega.place(x=476, y=145)
e_dat_entrega = DateEntry(frame_details, width=17, justify='center', relief="solid")
e_dat_entrega.place(x=480, y=175)

#FUÇÃO ESCOLHER IMAGEM

def escolher_imagem():
    global imagem, imagem_string, l_imagem


    imagem = fd.askopenfilename()
    imagem_string = imagem
    
    imagem = Image.open(imagem)
    imagem = imagem.resize((145,145))
    imagem = ImageTk.PhotoImage(imagem)
    l_imagem = Label(frame_details, image=imagem, bg=cor5, fg=cor3)
    l_imagem.place(x=780, y=27)
    
    botao_carregar['text'] = 'TROCAR DE FOTO'
    
botao_carregar = Button(frame_details, command=escolher_imagem, text='Carregar Foto'.upper(), width=23, compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 7 bold'), bg=cor1, fg=cor5)
botao_carregar.place(x=780, y=180)

# tabela morador
def mostrar_moradores():
    
    list_header = ['id', '     Nome', '      Email', ' Telefone', '   Bloco', 'Apto' ,' Data de Recebimento', '   Data de Entrega', '  Responsável', '  Status']
    
    #view all moradores
    df_list = sistema_de_resgitro.view_all_residents()
    
    tree_morador = ttk.Treeview(frame_tabela, selectmode="extended", columns=list_header, show="headings")
    #vertical scrolbar
    vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command= tree_morador.yview)
    #horizontal scrolbar
    hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command= tree_morador.xview)
    
    tree_morador.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree_morador.grid(column=0, row=1, sticky='nsew')
    vsb.grid(column=1, row=1, sticky='ns')
    hsb.grid(column=0, row=2, sticky='ew')
    frame_tabela.grid_rowconfigure(0, weight=12)
    
    hd=["nw","nw","center","center","center","center","center","center","center","center"]
    h=[40,140,120,70,71,70,150,110,120,110]
    n=0
    
    for col in list_header:
        tree_morador.heading(col, text=col.title(), anchor=NW)
        
        tree_morador.column(col, width=h[n], anchor=hd[n])
        
        n+=1
        
    for item in df_list:
        tree_morador.insert('', 'end', values=item)

frame_button = Frame(frame_button, width=120, height=72, bg=cor4, relief=RAISED)
frame_button.grid(row=3, column=0, pady=2, padx=10, sticky=NSEW)
 
l_nome = Label(frame_button, text="Procurar morador: ", anchor=NW, font=('Montserrat', 12), bg=cor4, fg=cor6)
l_nome.grid(row=0, column=3,padx=100, pady=20, sticky=NSEW)
e_procurar= Entry(frame_button, width=15, justify='left', relief="solid")
e_procurar.place(x=680, y=25)

app_procurar = Button(frame_button, command=procurar, text="  Procurar", width=10, relief=GROOVE, compound=LEFT, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
app_procurar.grid(row=0, column=15,padx=20, pady=20, sticky=NSEW)

#FRAMES BOTÕES ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

app_img_adicionar = Image.open('add.png')
app_img_adicionar = app_img_adicionar.resize((20,20))
app_img_adicionar =ImageTk.PhotoImage(app_img_adicionar)
app_adicionar = Button(frame_button, command=adicionar, text="  Adicionar", width=100, image=app_img_adicionar, relief=GROOVE, compound=LEFT, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
app_adicionar.grid(row=0, column=0, padx=20, pady=20, sticky=NSEW)

app_img_atualizar = Image.open('atualiza.png')
app_img_atualizar = app_img_atualizar.resize((25,25))
app_img_atualizar =ImageTk.PhotoImage(app_img_atualizar)
app_atualizar = Button(frame_button, command=atualizar, text="  Atualizar", width=100, image=app_img_atualizar, relief=GROOVE, compound=LEFT, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
app_atualizar.grid(row=0, column=1,padx=20, pady=20, sticky=NSEW)

app_img_delete = Image.open('lixeira.png')
app_img_delete = app_img_delete.resize((20,20))
app_img_delete =ImageTk.PhotoImage(app_img_delete)
app_delete = Button(frame_button, command=deletar, text="  Deletar ", width=100, image=app_img_delete, relief=GROOVE, compound=LEFT, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
app_delete.grid(row=0, column=2,padx=20, pady=20, sticky=NSEW)


def send_whatsapp_message():
    # Mensagem pré-definida (encoding URL necessário)
    message = 'Olá! Você possui um produto para entrega.'
    # Criar URL do WhatsApp
    url = f'https://wa.me/?text{message.replace(" ", "%20")}'
    # Abrir URL no navegador padrão
    webbrowser.open(url)
    
## BOTAO WHSATAPP
app_img_whatsapp= Image.open('whatsapp.png')
app_img_whatsapp = app_img_whatsapp.resize((20,20))
app_img_whatsapp =ImageTk.PhotoImage(app_img_whatsapp)
app_whatsapp = Button(frame_details, command=send_whatsapp_message, image=app_img_whatsapp, text='  Whatsapp ',  relief=GROOVE, width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor2, fg=cor5)
app_whatsapp.place(x=500, y=90)
mostrar_moradores()


janela.mainloop()