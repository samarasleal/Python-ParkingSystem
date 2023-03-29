#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 18:19:21 2017

@author: samara
"""
import Banco

class Taxa:
    def __init__(self, nomeEstacionamento, taxa15minC, taxaDiariaC, taxaMensalC, taxa15minM, taxaDiariaM, taxaMensalM):
        self.nomeEstacionamento = nomeEstacionamento
        self.taxa15minC = taxa15minC
        self.taxaDiariaC = taxaDiariaC
        self.taxaMensalC = taxaMensalC
        self.taxa15minM = taxa15minM
        self.taxaDiariaM = taxaDiariaM
        self.taxaMensalM = taxaMensalM
        self.banco = Banco.Banco()
        
    def inserirTaxa(self):
        self.banco.criarTabelaTaxa()
        c = self.banco.conexao.cursor()
        c.execute("insert into taxa (nomeEstacionamento, taxa15minC, taxaDiariaC, taxaMensalC, taxa15minM, taxaDiariaM, taxaMensalM) values ('" + self.nomeEstacionamento + "','" + self.taxa15minC + "', '" + self.taxaDiariaC + "', '" + self.taxaMensalC + "', '" + self.taxa15minM + "', '" + self.taxaDiariaM + "', '" + self.taxaMensalM + "')")        
        self.banco.conexao.commit()
        c.close()
    
    def alterarTaxa(self):
        c = self.banco.conexao.cursor()
        self.nomeEstacionamento = str(self.nomeEstacionamento)
        self.taxa15minC = str(self.taxa15minC)
        self.taxaDiariaC = str(self.taxaDiariaC)
        self.taxaMensalC = str(self.taxaMensalC)
        self.taxa15minM = str(self.taxa15minM)
        self.taxaDiariaM = str(self.taxaDiariaM)
        self.taxaMensalM = str(self.taxaMensalM)
        #c.execute("update taxa set taxa15minC = '" + self.taxa15minC + "', taxaDiariaC = '" + self.taxaDiariaC + "', taxaMensalC = '" + self.taxaMensalC + "', taxa15minM = '" + self.taxa15minM + "', taxaDiariaM = '" + self.taxaDiariaM + "', taxaMensalM = '" + self.taxaMensalM + "' where nomeEstacionamento = " + self.nomeEstacionamento + " ")
        c.execute (""" UPDATE taxa SET taxa15minC=%s, taxaDiariaC=%s, taxaMensalC=%s, taxa15minM=%s, taxaDiariaM=%s, taxaMensalM=%s WHERE nomeEstacionamento=%s""", (self.taxa15minC, self.taxaDiariaC, self.taxaMensalC, self.taxa15minM, self.taxaDiariaM, self.taxaMensalM, self.nomeEstacionamento))
        self.banco.conexao.commit()
        c.close()
    
    def visualizarTaxas(self):
        c = self.banco.conexao.cursor()
        c.execute("select * from taxa")
        for linha in c:
            # liinha[0] contém idTaxa
            self.nomeEstacionamento = linha[1]
            self.taxa15minC = linha[2]
            self.taxaDiariaC = linha[3] 
            self.taxaMensalC = linha[4]
            self.taxa15minM = linha[5]
            self.taxaDiariaM = linha[6]
            self.taxaMensalM = linha[7]
        c.close()
        