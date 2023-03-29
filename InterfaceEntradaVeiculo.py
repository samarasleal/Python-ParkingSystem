#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 21:39:29 2017

@author: samara
"""
import Estacionamento
import datetime
from tkinter import *

class InterfaceEV():
    def __init__(self):
        self.janela = Toplevel()
        self.janela.configure(bg="navy")
        self.janela.title("Registrar Entrada de Veículo")
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
        
        self.lblPlaca = Label(self.cont1, text="Placa: ", bg="navy", fg="white").pack(side=LEFT)
        self.txtPlaca = Entry(self.cont1)
        self.txtPlaca.pack(side=LEFT, padx=30)
        
        self.lblModelo = Label(self.cont1, text="Modelo: ", bg="navy", fg="white").pack(side=LEFT)
        self.txtModelo = Entry(self.cont1)
        self.txtModelo.pack(side=LEFT, padx=30) 
        
        self.lblTipoV = Label(self.cont2, text="Tipo de Veículo: ", bg="navy", fg="white").pack(side=LEFT)         
        self.varTipoV = StringVar(self.cont2)
        self.varTipoV.set("selecionar...") 
        self.wTipoV = OptionMenu(self.cont2, self.varTipoV, "carro", "moto")
        self.wTipoV.config(bg="navy")
        self.wTipoV.pack(side=LEFT)
        
        self.lblTipoS = Label(self.cont3, text="Tipo de Serviço: ", bg="navy", fg="white").pack(side=LEFT)         
        self.varTipoS = StringVar(self.cont3)
        self.varTipoS.set("selecionar...") 
        self.wTipoS = OptionMenu(self.cont3, self.varTipoS, "hora", "diaria", "mensal")
        self.wTipoS.config(bg="navy")
        self.wTipoS.pack(side=LEFT)
        
        self.bntIns = Button(self.cont4, text="Registrar", command=self.registrarEntradaDeVeiculo, bg="navy").pack(side=LEFT,padx=30)
        
        self.bntS = Button(self.cont4, text="Sair", bg="navy", command=self.sairDaInterface).pack(side=LEFT)
        
        self.lblmsg = Label(self.cont5, text="", bg="navy", fg="white")
        self.lblmsg.pack()
        
    def registrarEntradaDeVeiculo(self):
        placa = self.txtPlaca.get()
        modelo = self.txtModelo.get()
        tipoVeiculo = self.varTipoV.get()
        tipoServico = self.varTipoS.get()
        dataEntrada = datetime.datetime.now()
        sDataEntrada = dataEntrada.strftime('%Y-%m-%d %H:%M:%S')
        
        estacionamento = Estacionamento.Estacionamento("", "", "") 
        retorno = estacionamento.registrarEntradaVeiculo(placa, modelo, tipoVeiculo, tipoServico, sDataEntrada)
        
        self.lblmsg["text"] = retorno

    def sairDaInterface(self):
        self.janela.destroy()