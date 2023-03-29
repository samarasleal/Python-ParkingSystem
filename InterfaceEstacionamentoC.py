#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 22:25:49 2017

@author: samara
"""

from tkinter import *
import Estacionamento

class InterfaceC():
    def __init__(self):
        self.janela = Toplevel()
        self.janela.configure(bg="navy")
        self.janela.title("Cadastrar Dados do Estacionamento")
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
        
        self.lblNome = Label(self.cont1, text="Nome: ", bg="navy", fg="white").pack(side=LEFT) 
        self.txtNome = Entry(self.cont1)
        self.txtNome.pack(side=RIGHT)
        
        self.lblQtdeVagasDispCarro = Label(self.cont2, text="Quantidade de vagas para carro: ", bg="navy", fg="white").pack(side=LEFT)
        self.txtQtdeVagasDispCarro = Entry(self.cont2)
        self.txtQtdeVagasDispCarro.pack(side=LEFT)
        
        self.lblQtdeVagasDispMoto = Label(self.cont2, text="Quantidade de vagas para moto: ", bg="navy", fg="white").pack(side=LEFT)
        self.txtQtdeVagasDispMoto = Entry(self.cont2)
        self.txtQtdeVagasDispMoto.pack(side=LEFT) 
        
        self.lblCarro = Label(self.cont3, text="Carro: ", bg="navy", fg="white").pack(side=LEFT)
        self.lblTaxa15minC = Label(self.cont3, text="Taxa 15min: ", bg="navy", fg="white").pack(side=LEFT)
        self.txtTaxa15minC = Entry(self.cont3)    
        self.txtTaxa15minC.pack(side=LEFT) 
        
        self.lblTaxaDiariaC = Label(self.cont3, text="Taxa Diária: ", bg="navy", fg="white").pack(side=LEFT)
        self.txtTaxaDiariaC = Entry(self.cont3)
        self.txtTaxaDiariaC.pack(side=LEFT)
        
        self.lblTaxaMensalC = Label(self.cont3, text="Taxa Mensal: ", bg="navy", fg="white").pack(side=LEFT)
        self.txtTaxaMensalC = Entry(self.cont3)
        self.txtTaxaMensalC.pack(side=LEFT)
        
        self.lblMoto = Label(self.cont4, text="Motos: ", bg="navy", fg="white").pack(side=LEFT)
        self.lblTaxa15minM = Label(self.cont4, text="Taxa 15min: ", bg="navy", fg="white").pack(side=LEFT)
        self.txtTaxa15minM = Entry(self.cont4)   
        self.txtTaxa15minM.pack(side=LEFT)
        
        self.lblTaxaDiariaM = Label(self.cont4, text="Taxa Diária: ", bg="navy", fg="white").pack(side=LEFT)
        self.txtTaxaDiariaM = Entry(self.cont4)
        self.txtTaxaDiariaM.pack(side=LEFT)
        
        self.lblTaxaMensalM = Label(self.cont4, text="Taxa Mensal: ", bg="navy", fg="white").pack(side=LEFT)
        self.txtTaxaMensalM = Entry(self.cont4)
        self.txtTaxaMensalM.pack(side=LEFT)
        
        self.bntIns = Button(self.cont5, text="Inserir", command=self.inserirDadosEstacionamento, bg="navy").pack(side=LEFT,padx=20)
        
        self.bntS = Button(self.cont5, text="Sair", bg="navy", command=self.sairDaInterface).pack(side=LEFT)
        
        self.lblmsg = Label(self.cont6, text="", bg="navy", fg="white")
        self.lblmsg.pack()
        
    def inserirDadosEstacionamento(self):
        nome = self.txtNome.get()
        qtdeVagasDispCarro = self.txtQtdeVagasDispCarro.get()
        qtdeVagasDispMoto = self.txtQtdeVagasDispMoto.get()
        
        taxa15minC = self.txtTaxa15minC.get()
        taxaDiariaC = self.txtTaxaDiariaC.get()
        taxaMensalC = self.txtTaxaMensalC.get()
        
        taxa15minM = self.txtTaxa15minM.get()
        taxaDiariaM = self.txtTaxaDiariaM.get()
        taxaMensalM = self.txtTaxaMensalM.get()
        
        estacionamento = Estacionamento.Estacionamento(nome, qtdeVagasDispCarro, qtdeVagasDispMoto) 
        retorno = estacionamento.inserirDadosEstacionamento(taxa15minC, taxaDiariaC, taxaMensalC, taxa15minM, taxaDiariaM, taxaMensalM)
        
        
        self.lblmsg["text"] = retorno

    def sairDaInterface(self):
        self.janela.destroy()