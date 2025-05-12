#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 16:46:56 2017

@author: samara
"""
# For mac: 
# brew install mysql
# brew services start mysql
# mysql_secure_installation 
# senha: 1234@Feliz 
# mysql -u root -p
# CREATE DATABASE estacionamentoX;

import pymysql
class Banco:    
    def __init__(self):
        self.conexao = pymysql.connect(host="localhost", user="root", passwd="1234@Feliz", db="estacionamentoX")
    def criarTabelaEstacionamento(self):       
        c = self.conexao.cursor()
        c.execute("""CREATE TABLE if not exists estacionamento(
                    nome VARCHAR(45) NOT NULL,
                    qtdeVagasDispCarro INT NOT NULL,
                    qtdeVagasDispMoto INT NOT NULL,
                    PRIMARY KEY (nome))""")           
        self.conexao.commit()
        self.conexao.close
    def criarTabelaVaga(self):       
        c = self.conexao.cursor()
        c.execute("""CREATE TABLE if not exists vaga(
                    idVaga INT NOT NULL AUTO_INCREMENT,
                    nomeEstacionamento VARCHAR(45) NOT NULL,
                    tipoServico VARCHAR(45) NOT NULL,
                    tipoVeiculo VARCHAR(45) NOT NULL,
                    dataEntrada VARCHAR(45) NOT NULL,
                    status VARCHAR(45) NOT NULL,
                    PRIMARY KEY (idVaga),
                    FOREIGN KEY (nomeEstacionamento) REFERENCES estacionamento (nome))""")           
        self.conexao.commit()
        self.conexao.close
    def criarTabelaTaxa(self):       
        c = self.conexao.cursor()
        c.execute("""CREATE TABLE if not exists taxa(
                    idTaxa INT NOT NULL AUTO_INCREMENT,
                    nomeEstacionamento VARCHAR(45) NOT NULL,
                    taxa15minC REAL NOT NULL,
                    taxaDiariaC REAL NOT NULL,
                    taxaMensalC REAL NOT NULL,
                    taxa15minM REAL NOT NULL,
                    taxaDiariaM REAL NOT NULL,
                    taxaMensalM REAL NOT NULL,
                    PRIMARY KEY (idTaxa),
                    FOREIGN KEY (nomeEstacionamento) REFERENCES estacionamento (nome))""")
    def criarTabelaVeiculo(self):       
        c = self.conexao.cursor()
        c.execute("""CREATE TABLE if not exists veiculo(
                    idVeiculo INT NOT NULL AUTO_INCREMENT,
                    idVaga INT NOT NULL,
                    placa VARCHAR(45) NOT NULL,
                    modelo VARCHAR(45) NOT NULL,
                    tipoVeiculo VARCHAR(45) NOT NULL,                
                    PRIMARY KEY (idVeiculo),
                    FOREIGN KEY (idVaga) REFERENCES vaga (idVaga))""")            
        self.conexao.commit()
        self.conexao.close
    def criarTabelaHistoricoVeiculo(self):       
        c = self.conexao.cursor()
        c.execute("""CREATE TABLE if not exists historicoVeiculo(
                    idVeiculo INT NOT NULL AUTO_INCREMENT,
                    idVaga INT NOT NULL,
                    placa VARCHAR(45) NOT NULL,
                    modelo VARCHAR(45) NOT NULL,
                    tipoVeiculo VARCHAR(45) NOT NULL,
                    valor REAL NOT NULL,                 
                    dataSaida VARCHAR(45) NOT NULL,                 
                    PRIMARY KEY (idVeiculo),
                    FOREIGN KEY (idVaga) REFERENCES vaga (idVaga))""")            
        self.conexao.commit()
        self.conexao.close
    def apagarTabelaVeiculo(self):
        c = self.conexao.cursor()
        c.execute("drop table veiculo")
        self.conexao.commit()
        self.conexao.close
    def apagarTabelaHistoricoVeiculo(self):
        c = self.conexao.cursor()
        c.execute("drop table historicoVeiculo")
        self.conexao.commit()
        self.conexao.close
