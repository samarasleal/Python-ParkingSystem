#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 22:25:49 2017

@author: samara
"""
import InterfaceEstacionamentoC
import InterfaceEstacionamentoA
import InterfaceEstacionamentoV
import InterfaceEntradaVeiculo
import InterfaceSaidaVeiculo
import Estacionamento

# Importar a biblioteca tkinter para criar interfaces de usuário
from tkinter import *
# Importar a biblioteca PIL para converter imagem do tipo ".jpg" para o formato do tkinter
from PIL import Image, ImageTk
# Importa a biblioteca para datas e horários
from datetime import *

class InterfaceP():
    def __init__(self, master):
        self.cont1 = Frame(master, pady =10, bg="navy")
        self.cont1.pack()
        self.cont2 = Frame(master, padx =20, pady=5, bg="navy")
        self.cont2.pack()
        self.cont3 = Frame(master, pady=15, bg="navy")
        self.cont3.pack()
        self.cont4 = Frame(master, pady=0, bg="navy")
        self.cont4.pack()
        self.cont5 = Frame(master, padx =20, pady=5, bg="navy")
        self.cont5.pack()
        self.cont6 = Frame(master, padx =20, pady=5, bg="navy")
        self.cont6.pack()
    
        self.titulo = Label(self.cont1, text="Estacionamento", bg="navy", fg="white", font=(None, 20))
        self.titulo.pack ()
        
        # Logomarca
        # Abrir imagem que desejo carregar usando Image.open()
        self.logoAberta = Image.open("carroE.jpg")
        # Converter a imagem para o formato do tkinter usando ImageTk.PhotoImage()
        self.logoConvertida= ImageTk.PhotoImage(self.logoAberta)
        # Setar o estilo image (imagem) do Label para a imagem convertida usando image=logoConvertida
        self.logo = Label(self.cont1, image=self.logoConvertida, bg="navy")
        self.logo.pack(side=TOP,anchor=W, fill=X, expand=YES)    
        
        # Data
        self.hoje = datetime.now()
        self.dia = str(self.hoje.day)
        self.mes = str(self.hoje.month)
        self.ano = str(self.hoje.year)
        self.lbldata = Label(self.cont2, text="Data: "+self.ano+"-"+self.mes+"-"+self.dia, bg="navy", fg="white")
        self.lbldata.pack(side=LEFT, padx="20") 
        
        # Hora
        self.hora = str(self.hoje.hour)
        self.minuto = str(self.hoje.minute)
        self.segundo = str(self.hoje.second)
        self.lblhora = Label(self.cont2, text="Horário: "+self.hora+":"+self.minuto+":"+self.segundo, bg="navy", fg="white")
        self.lblhora.pack(side=RIGHT, padx="20") 
        
        # Menu        
        self.mb = Menubutton(self.cont3, text="Estacionamento", relief= RAISED, bg="navy")
        self.mb.menu = Menu(self.mb, tearoff=False, bg="navy")
        self.mb["menu"] = self.mb.menu 
        self.mb.menu.add_command(label="Cadastrar", command=self.abrirInterfaceEstacionamentoC)
        self.mb.menu.add_command(label="Alterar", command=self.abrirInterfaceEstacionamentoA)
        self.mb.menu.add_command(label="Visualizar", command=self.abrirInterfaceEstacionamentoV)
        self.mb.pack(side=LEFT,padx=20)
        
        self.mb2 = Menubutton(self.cont3, text="Veículos", relief= RAISED, bg="navy")
        self.mb2.menu = Menu(self.mb2, tearoff=False)
        self.mb2["menu"] = self.mb2.menu   
        self.mb2.menu.add_command(label="Dar Entrada", command=self.abrirInterfaceEntradaVeiculo)
        self.mb2.menu.add_command(label="Dar Saída", command=self.abrirInterfaceSaidaVeiculo)
        self.mb2.pack(side=LEFT, padx=20)  
        
        self.texto = Label(self.cont4, text="Vagas ocupadas", bg="navy", fg="white", font=("Times", 16))
        self.texto.pack(side=LEFT, padx=305)        
        self.bntAtualizar = Button(self.cont4, text="Atualizar Dados", command=self.visualizarVagasOcupadas, bg="navy")
        self.bntAtualizar.pack(side=RIGHT)
    
        # Visualizar Vagas
        cabecalho = ["Vaga", "Veículo", "Placa", "Serviço", "Data Entrada"]
        for coluna in range(len(cabecalho)):
            lblC = Label(self.cont5, text="%s" % (cabecalho[coluna]), borderwidth=0, width=18, bg="gray")
            lblC.grid(row=1, column=coluna, sticky="nsew", padx=3, pady=6)          
        self.visualizarVagasOcupadas()
        
    def visualizarVagasOcupadas(self):
        estacionamento = Estacionamento.Estacionamento("", "", "") 
        vagasOcupadas = estacionamento.visualizarVagasOcupadas()
        for linha in range(len(vagasOcupadas)):
            for coluna in range(len(vagasOcupadas[linha])):
                lblTabela = Label(self.cont6, text="%s" % (vagasOcupadas[linha][coluna]), borderwidth=0, width=18)
                lblTabela.grid(row=linha, column=coluna, sticky="nsew", padx=3, pady=3)           

    def abrirInterfaceEstacionamentoC(self):
        InterfaceEstacionamentoC.InterfaceC()
    
    def abrirInterfaceEstacionamentoA(self):
        InterfaceEstacionamentoA.InterfaceA()
    
    def abrirInterfaceEstacionamentoV(self):
        InterfaceEstacionamentoV.InterfaceV()

    def abrirInterfaceEntradaVeiculo(self):
        InterfaceEntradaVeiculo.InterfaceEV()
        
    def abrirInterfaceSaidaVeiculo(self):
        InterfaceSaidaVeiculo.InterfaceSV()

raiz = Tk()
raiz.configure(bg="navy")
raiz.title("Estacionamento")
InterfaceP(raiz)
raiz.mainloop()   