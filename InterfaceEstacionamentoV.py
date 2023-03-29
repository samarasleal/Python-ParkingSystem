#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 02:35:41 2017

@author: samara
"""

from tkinter import *
import Estacionamento

class InterfaceV():
    def __init__(self):
        self.janela = Toplevel()
        self.janela.configure(bg="navy")
        self.janela.title("Visualizar Dados do Estacionamento")
        self.cont1 = Frame(self.janela, pady =10, bg="navy")
        self.cont1.pack()
        self.cont2 = Frame(self.janela, pady =10, bg="navy")
        self.cont2.pack()
        self.cont3 = Frame(self.janela, pady =10, bg="navy")
        self.cont3.pack()
        self.cont4 = Frame(self.janela, pady =10, bg="navy")
        self.cont4.pack()
        self.cont5 = Frame(self.janela, pady =10, bg="navy")
        self.cont5.pack()
        self.cont6 = Frame(self.janela, pady =10, bg="navy")
        self.cont6.pack()
        
        self.lblNome = Label(self.cont1, text="Nome: ", bg="navy", fg="white")
        self.lblNome.pack(side=LEFT) 
        self.txtNome = Entry(self.cont1, bg="navy", fg="white")
        self.txtNome.pack(side=RIGHT)
        
        self.lblQtdeVagasDispCarro = Label(self.cont2, text="Quantidade de vagas para carro: ", bg="navy", fg="white").pack(side=LEFT)
        self.txtQtdeVagasDispCarro = Entry(self.cont2, bg="navy", fg="white")
        self.txtQtdeVagasDispCarro.pack(side=LEFT)
        
        self.lblQtdeVagasDispMoto = Label(self.cont2, text="Quantidade de vagas para moto: ", bg="navy", fg="white").pack(side=LEFT)
        self.txtQtdeVagasDispMoto = Entry(self.cont2, bg="navy", fg="white")
        self.txtQtdeVagasDispMoto.pack(side=LEFT) 
        
        self.lblCarro = Label(self.cont3, text="Carro: ", bg="navy", fg="white").pack(side=LEFT)
        self.lblTaxa15minC = Label(self.cont3, text="Taxa 15min: ", bg="navy", fg="white").pack(side=LEFT)
        self.txtTaxa15minC = Entry(self.cont3, bg="navy", fg="white")    
        self.txtTaxa15minC.pack(side=LEFT) 
        
        self.lblTaxaDiariaC = Label(self.cont3, text="Taxa Diária: ", bg="navy", fg="white").pack(side=LEFT)
        self.txtTaxaDiariaC = Entry(self.cont3, bg="navy", fg="white")
        self.txtTaxaDiariaC.pack(side=LEFT)
        
        self.lblTaxaMensalC = Label(self.cont3, text="Taxa Mensal: ", bg="navy", fg="white").pack(side=LEFT)
        self.txtTaxaMensalC = Entry(self.cont3, bg="navy", fg="white")
        self.txtTaxaMensalC.pack(side=LEFT)
        
        self.lblMoto = Label(self.cont4, text="Motos: ", bg="navy", fg="white").pack(side=LEFT)
        self.lblTaxa15minM = Label(self.cont4, text="Taxa 15min: ", bg="navy", fg="white").pack(side=LEFT)
        self.txtTaxa15minM = Entry(self.cont4, bg="navy", fg="white")   
        self.txtTaxa15minM.pack(side=LEFT)
        
        self.lblTaxaDiariaM = Label(self.cont4, text="Taxa Diária: ", bg="navy", fg="white").pack(side=LEFT)
        self.txtTaxaDiariaM = Entry(self.cont4, bg="navy", fg="white")
        self.txtTaxaDiariaM.pack(side=LEFT)
        
        self.lblTaxaMensalM = Label(self.cont4, text="Taxa Mensal: ", bg="navy", fg="white").pack(side=LEFT)
        self.txtTaxaMensalM = Entry(self.cont4, bg="navy", fg="white")
        self.txtTaxaMensalM.pack(side=LEFT)
        
        self.bntSair = Button(self.cont5, text="Sair", bg="navy", command=self.sairDaInterface).pack(side=RIGHT)
        
        self.visualizarDadosEstacionamento()
        
    def visualizarDadosEstacionamento(self):
        estacionamento = Estacionamento.Estacionamento("","","")
        estacionamento.visualizarDadosEstacionamento()
        taxa = estacionamento.visualizarTaxasEstacionamento()
        
        self.txtNome.insert(INSERT, estacionamento.nome)
        self.txtQtdeVagasDispCarro.insert(INSERT, estacionamento.qtdeVagasDispCarro)
        self.txtQtdeVagasDispMoto.insert(INSERT, estacionamento.qtdeVagasDispMoto)
        
        self.txtTaxa15minC.insert(INSERT, taxa.taxa15minC)
        self.txtTaxaDiariaC.insert(INSERT, taxa.taxaDiariaC)
        self.txtTaxaMensalC.insert(INSERT, taxa.taxaMensalC)
        self.txtTaxa15minM.insert(INSERT, taxa.taxa15minM)
        self.txtTaxaDiariaM.insert(INSERT, taxa.taxaDiariaM)
        self.txtTaxaMensalM.insert(INSERT, taxa.taxaMensalM)
        
    def sairDaInterface(self):
        self.janela.destroy()
    
        
        
        