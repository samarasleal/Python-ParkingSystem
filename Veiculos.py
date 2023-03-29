#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 22:27:58 2017

@author: samara
"""
import Banco

class Veiculo():
    def __init__(self, idVaga, placa, modelo, tipoVeiculo, valor, dataSaida):
        self.idVaga = idVaga
        self.placa = placa
        self.modelo = modelo
        self.tipoVeiculo = tipoVeiculo
        self.valor = valor
        self.dataSaida = dataSaida
        self.banco = Banco.Banco()
        self.banco.criarTabelaVeiculo()
        self.banco.criarTabelaHistoricoVeiculo()
        
    def inserirVeiculo(self):
        c = self.banco.conexao.cursor()
        self.idVaga = str(self.idVaga)
        self.valor = str(self.valor)
        c.execute("insert into veiculo (idVaga, placa, modelo, tipoVeiculo) values ('" + self.idVaga + "', '" + self.placa + "', '" + self.modelo + "', '" + self.tipoVeiculo + "')")        
        c.execute("insert into historicoVeiculo (idVaga, placa, modelo, tipoVeiculo, valor, dataSaida) values ('" + self.idVaga + "', '" + self.placa + "', '" + self.modelo + "', '" + self.tipoVeiculo + "', '" + self.valor + "', '" + self.dataSaida + "')")        
        self.banco.conexao.commit()
        c.close()
    
    def adicionarValor(self, idVaga, valor):
        c = self.banco.conexao.cursor()
        valor = str(valor)
        c.execute (""" update historicoVeiculo set valor=%s where idVaga=%s""", (valor, idVaga))       
        self.banco.conexao.commit()
        c.close()
        
    def adicionarDataSaida(self, idVaga, dataSaida):
        c = self.banco.conexao.cursor()
        c.execute (""" update historicoVeiculo set dataSaida=%s where idVaga=%s""", (dataSaida, idVaga))       
        self.banco.conexao.commit()
        c.close()
    
    def apagarVeículo(self, idVaga):
        c = self.banco.conexao.cursor()
        c.execute (""" delete from veiculo where idVaga=%s""", (idVaga))       
        self.banco.conexao.commit()
        c.close()
        

class Moto(Veiculo):
    def __init__(self, idVaga, placa, modelo, tipoVeiculo, valor, dataSaida):
        Veiculo.__init__(self, idVaga, placa, modelo, tipoVeiculo, valor, dataSaida)

        
class Carro(Veiculo):
    def __init__(self, idVaga, placa, modelo, tipoVeiculo, valor, dataSaida):
        Veiculo.__init__(self, idVaga, placa, modelo, tipoVeiculo, valor, dataSaida)

    