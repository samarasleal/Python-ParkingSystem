#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 02:35:41 2017

@author: samara
"""

from tkinter import *
import InterfaceEstacionamentoV
import Estacionamento


class InterfaceA():
    def __init__(self):
        self.interface = InterfaceEstacionamentoV.InterfaceV()
        self.interface.janela.title("Alterar Dados do Estacionamento")
        
        self.interface.lblNome["text"]= "Nome: (Não pode ser alterado)"
        self.nomeAnterior = self.interface.txtNome.get()
        
        self.bntAlt = Button(self.interface.cont5, text="Alterar", bg="navy", command=self.alterarDadosEstacionamento).pack(side=LEFT, padx=20)
        self.lblmsg = Label(self.interface.cont6, text="", bg="navy", fg="white")
        self.lblmsg.pack()

        self.bntSair = Button(self.cont5, text="Sair", bg="navy", command=self.sairDaInterface).pack(side=RIGHT)
        
    def alterarDadosEstacionamento(self):
        qtdeVagasDispCarro = self.interface.txtQtdeVagasDispCarro.get()
        qtdeVagasDispMoto = self.interface.txtQtdeVagasDispMoto.get()
        
        taxa15minC = self.interface.txtTaxa15minC.get()
        taxaDiariaC = self.interface.txtTaxaDiariaC.get()
        taxaMensalC = self.interface.txtTaxaMensalC.get()
        
        taxa15minM = self.interface.txtTaxa15minM.get()
        taxaDiariaM = self.interface.txtTaxaDiariaM.get()
        taxaMensalM = self.interface.txtTaxaMensalM.get()
        
        estacionamento = Estacionamento.Estacionamento(self.nomeAnterior, qtdeVagasDispCarro, qtdeVagasDispMoto)
        retorno = estacionamento.alterarDadosEstacionamento()
        estacionamento.alterarTaxasEstacionamento(self.nomeAnterior, taxa15minC, taxaDiariaC, taxaMensalC, taxa15minM, taxaDiariaM, taxaMensalM)
        
        self.lblmsg["text"] = retorno
        
    def sairDaInterface(self):
        self.janela.destroy()
        

        
        
        
        
        
        