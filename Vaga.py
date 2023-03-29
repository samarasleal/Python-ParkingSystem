#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 15:43:24 2017

@author: samara
"""

import Banco
import Veiculos
import datetime

class Vaga:
    def __init__(self, nomeEstacionamento, tipoServico, dataEntrada, tipoVeiculo, status):
        self.nomeEstacionamento = nomeEstacionamento
        self.tipoServico = tipoServico
        self.dataEntrada = dataEntrada      
        self.tipoVeiculo = tipoVeiculo
        self.status = status
        self.banco = Banco.Banco()
        self.banco.criarTabelaVaga()
        
    def inserirVagaVazia(self):
        c = self.banco.conexao.cursor()
        c.execute("insert into vaga (nomeEstacionamento, tipoServico, dataEntrada, tipoVeiculo, status) values ('" + self.nomeEstacionamento + "', '" + self.tipoServico + "', '" + self.dataEntrada + "', '" + self.tipoVeiculo + "', '" + self.status + "')")        
        self.banco.conexao.commit()
        c.close()
    
    def excluirTodasVagasVazias(self):
        c = self.banco.conexao.cursor()
        self.banco.apagarTabelaVeiculo()
        self.banco.apagarTabelaHistoricoVeiculo()
        c.execute("truncate vaga") 
        self.banco.criarTabelaVeiculo()
        self.banco.criarTabelaHistoricoVeiculo()
        self.banco.conexao.commit()
        c.close()
    
    def buscarVagaDisponivel(self):
        c = self.banco.conexao.cursor()
        c.execute (""" select idVaga from vaga where status=%s and tipoVeiculo=%s limit 1""", ("disponivel", self.tipoVeiculo))
        for linha in c:
            idVaga = linha[0] 
        c.close()
        return idVaga
    
    def buscarVagaOcupada(self, placa, tipoServico):
        c = self.banco.conexao.cursor()
        idVaga = ""
        c.execute (""" select vaga.idVaga, vaga.dataEntrada, vaga.tipoVeiculo from vaga,veiculo where vaga.idVaga=veiculo.idVaga and veiculo.placa=%s and tipoServico=%s """, (placa, tipoServico))
        for linha in c:
            idVaga = linha[0]
            self.dataEntrada = linha[1]
            self.tipoVeiculo = linha[2]
        c.close()
        return idVaga
    
    def buscarVagasOcupadas(self):
        c = self.banco.conexao.cursor()
        Veiculos.Veiculo("", "", "", "", "", "")
        c.execute (""" select vaga.idVaga, vaga.tipoVeiculo, veiculo.placa, vaga.tipoServico, vaga.dataEntrada from vaga, veiculo where vaga.idVaga=veiculo.idVaga and status=%s""", ("ocupada"))
        listaVagas = []
        for linha in c:
            idVaga = linha[0]
            self.tipoVeiculo = linha[1]
            placa = linha[2]
            self.tipoServico = linha[3]
            self.dataEntrada = linha[4]
            reg = []
            reg.append(idVaga)
            reg.append(self.tipoVeiculo)
            reg.append(placa)
            reg.append(self.tipoServico)
            reg.append(self.dataEntrada)
            listaVagas.append(reg)
        c.close()
        return listaVagas
    
    def verificarServicoEDataEntrada(self, placa, tipoServico):
        retorno = "OK"      
        c = self.banco.conexao.cursor()
        c.execute (""" select vaga.idVaga, vaga.tipoServico, vaga.dataEntrada from vaga, veiculo where vaga.idVaga=veiculo.idVaga and veiculo.placa=%s""", (placa))  
        for linha in c:
            idVaga = linha[0]
            tipoServico = linha[1] 
            dataEntrada = linha[2]
            if dataEntrada!= "":
                hoje = datetime.datetime.now()
                dataEntradaD = datetime.datetime.strptime(dataEntrada, '%Y-%m-%d %H:%M:%S')
                if tipoServico == "diaria":
                    if (dataEntradaD.date() == hoje.date()):
                        retorno = "Cliente Diária dando entrada mais uma vez. Vaga: %s" %(idVaga)                    
                elif tipoServico == "mensal":
                    res = hoje - dataEntradaD
                    if (res.days <= 31):
                        retorno = "Cliente Mensalista dando entrada mais uma vez. Vaga: %s" %(idVaga)
        c.close()
        return retorno
    
    def registrarEntradaVeiculo(self, idVaga, placa, modelo, valor):
        if self.tipoVeiculo=="carro":
            veiculo = Veiculos.Carro(idVaga, placa, modelo, self.tipoVeiculo, valor, "")
        else:
            veiculo = Veiculos.Moto(idVaga, placa, modelo, self.tipoVeiculo, valor, "")
        veiculo.inserirVeiculo()
        c = self.banco.conexao.cursor()
        self.status = "ocupada"
        c.execute (""" UPDATE vaga SET tipoServico=%s, dataEntrada=%s, tipoVeiculo=%s, status=%s  WHERE idVaga=%s""", (self.tipoServico, self.dataEntrada, self.tipoVeiculo, self.status, veiculo.idVaga))
        self.banco.conexao.commit()
        c.close()

    def registrarSaidaVeiculo(self, idVaga, valor, dataSaida):
        veiculo = Veiculos.Veiculo(idVaga, "", "", "", valor, dataSaida)  
        c = self.banco.conexao.cursor()
        idVaga = str(idVaga)
        
        veiculo.apagarVeículo(idVaga)
        veiculo.adicionarDataSaida(idVaga, dataSaida)
        
        c.execute (""" UPDATE vaga SET tipoServico=%s, dataEntrada=%s, status=%s  WHERE idVaga=%s""", ("", "", "disponível", idVaga))
        if (self.tipoServico == "hora"):
            veiculo.adicionarValor(idVaga, valor)         
        self.banco.conexao.commit()
        c.close()
        
    
        