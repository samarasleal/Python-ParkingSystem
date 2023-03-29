#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 21:39:29 2017

@author: samara
"""
import Estacionamento
import datetime
from tkinter import *

class InterfaceSV():
    def __init__(self):
        self.janela = Toplevel()
        self.janela.configure(bg="navy")
        self.janela.title("Registrar Saída de Veículo")
        self.cont1 = Frame(self.janela, pady =10, bg="navy")
        self.cont1.pack()
        self.cont2 = Frame(self.janela, pady =10, bg="navy")
        self.cont2.pack()
        self.cont3 = Frame(self.janela, pady =10, bg="navy")
        self.cont3.pack()
        self.cont4 = Frame(self.janela, pady =10, bg="navy")
        self.cont4.pack()
        self.cont5= Frame(self.janela, pady =10, bg="navy")
        self.cont5.pack()
        
        self.lblPlaca = Label(self.cont1, text="Placa: ", bg="navy", fg="white").pack(side=LEFT)
        self.txtPlaca = Entry(self.cont1)
        self.txtPlaca.pack(side=LEFT, padx=50)
        
        self.lblTipoS = Label(self.cont2, text="Tipo de Serviço: ", bg="navy", fg="white").pack(side=LEFT)         
        self.varTipoS = StringVar(self.cont2)
        self.varTipoS.set("selecionar...") 
        self.wTipoS = OptionMenu(self.cont2, self.varTipoS, "hora", "diaria", "mensal")
        self.wTipoS.config(bg="navy")
        self.wTipoS.pack(side=LEFT)  
        
        self.lblRadio = Label(self.cont3, text="Disponibilizar vaga? ", bg="navy", fg="white").pack(side=LEFT) 
        self.varRadio = StringVar(self.cont3)
        self.varRadio.set("Não")            
        self.radio1 = Radiobutton(self.cont3, text="Não", variable=self.varRadio, value="Não", bg="navy").pack(side=RIGHT, anchor=W)
        self.radio2 = Radiobutton(self.cont3, text="Sim", variable=self.varRadio, value="Sim", bg="navy").pack(side=RIGHT, anchor=W)                 
               
        self.bntIns = Button(self.cont4, text="Registrar", command=self.registrarSaidaDeVeiculo, bg="navy").pack(side=LEFT,padx=30)
        
        self.bntS = Button(self.cont4, text="Sair", bg="navy", command=self.sairDaInterface).pack(side=LEFT)
        
        self.lblmsg = Label(self.cont5, text="", bg="navy", fg="white")
        self.lblmsg.pack()
        
    def registrarSaidaDeVeiculo(self):
        placa = self.txtPlaca.get()
        tipoServico = self.varTipoS.get()
        disponibilizarVaga = self.varRadio.get()
        dataSaida = datetime.datetime.now()
        sDataSaida = dataSaida.strftime('%Y-%m-%d %H:%M:%S')
        
        estacionamento = Estacionamento.Estacionamento("", "", "") 
        retorno = estacionamento.registrarSaidaVeiculo(placa, tipoServico, sDataSaida, disponibilizarVaga)
        
        self.lblmsg["text"] = retorno

    def sairDaInterface(self):
        self.janela.destroy()