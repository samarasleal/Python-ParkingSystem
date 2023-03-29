# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 14:46:48 2016
@author: samara
"""
import Vaga
import Taxa
import Banco
import datetime

class Estacionamento:
    def __init__(self, nome, qtdeVagasDispCarro, qtdeVagasDispMoto):
        self.nome = nome
        self.qtdeVagasDispCarro = qtdeVagasDispCarro
        self.qtdeVagasDispMoto = qtdeVagasDispMoto
        self.banco = Banco.Banco()
        
    def inserirDadosEstacionamento(self, taxa15minC, taxaDiariaC, taxaMensalC, taxa15minM, taxaDiariaM, taxaMensalM):
        res = self.visualizarDadosEstacionamento()
        if res == 0:
            c = self.banco.conexao.cursor()
            c.execute("insert into estacionamento (nome, qtdeVagasDispCarro, qtdeVagasDispMoto) values ('" + self.nome + "', '" + self.qtdeVagasDispCarro + "', '" + self.qtdeVagasDispMoto + "')")        
            self.banco.conexao.commit()
            c.close()
            # Inserir vagas vazias
            servico = ""
            dataEntrada = "" 
            status = "disponivel"
            for i in range(0,int(self.qtdeVagasDispCarro)):
                tipoVeiculo = "carro" 
                vaga = Vaga.Vaga(self.nome, servico, dataEntrada, tipoVeiculo, status)
                vaga.inserirVagaVazia()
                
            for i in range(0,int(self.qtdeVagasDispMoto)):
                tipoVeiculo = "moto" 
                vaga = Vaga.Vaga(self.nome, servico, dataEntrada, tipoVeiculo, status)
                vaga.inserirVagaVazia()
            taxa = Taxa.Taxa(self.nome, taxa15minC, taxaDiariaC, taxaMensalC, taxa15minM, taxaDiariaM, taxaMensalM)       
            taxa.inserirTaxa()
            retorno = "Dados do Estacionamento inseridos com sucesso."
        else:
            retorno = "Operação não pode ser realizada. Os dados já estão cadastrados."
        return retorno
    
    def alterarDadosEstacionamento(self):
        c = self.banco.conexao.cursor()
        self.nome = str(self.nome)
        self.qtdeVagasDispCarro = str(self.qtdeVagasDispCarro)
        self.qtdeVagasDispMoto = str(self.qtdeVagasDispMoto)
        c.execute (""" UPDATE estacionamento SET qtdeVagasDispCarro=%s, qtdeVagasDispMoto=%s WHERE nome=%s""", (self.qtdeVagasDispCarro, self.qtdeVagasDispMoto, self.nome))
        self.banco.conexao.commit()
        c.close()
        servico = ""
        dataEntrada = "" 
        status = "disponivel"
        # Apagar vagas existentes
        vaga = Vaga.Vaga(self.nome, servico, dataEntrada, "carro", status)
        vaga.excluirTodasVagasVazias()
        # Inserir novas vagas de acordo com a nova quantidade informada
        for i in range(0,int(self.qtdeVagasDispCarro)):
            tipoVeiculo = "carro" 
            vaga = Vaga.Vaga(self.nome, servico, dataEntrada, tipoVeiculo, status)
            vaga.inserirVagaVazia()
            
        for i in range(0,int(self.qtdeVagasDispMoto)):
            tipoVeiculo = "moto" 
            vaga = Vaga.Vaga(self.nome, servico, dataEntrada, tipoVeiculo, status)
            vaga.inserirVagaVazia()
        retorno = "Dados do Estacionamento alterados com sucesso."
        return retorno
    
    def alterarTaxasEstacionamento(self, nome, taxa15minC, taxaDiariaC, taxaMensalC, taxa15minM, taxaDiariaM, taxaMensalM):
        taxa = Taxa.Taxa(nome, taxa15minC, taxaDiariaC, taxaMensalC, taxa15minM, taxaDiariaM, taxaMensalM)       
        taxa.alterarTaxa()
    
    def visualizarDadosEstacionamento(self):
        c = self.banco.conexao.cursor()
        r = c.execute("select * from estacionamento")
        for linha in c:
            self.nome = linha[0]
            self.qtdeVagasDispCarro = linha[1]
            self.qtdeVagasDispMoto = linha[2]          
        c.close()
        return r
    
    def visualizarTaxasEstacionamento(self):
        taxa = Taxa.Taxa(self.nome, "", "", "", "", "", "")       
        taxa.visualizarTaxas()
        return taxa        
            
    def visualizarVagasOcupadas(self):
        self.banco.criarTabelaEstacionamento()
        vaga = Vaga.Vaga(self.nome, "", "", "", "ocupada")
        retorno = vaga.buscarVagasOcupadas()
        return retorno
     
    def registrarEntradaVeiculo(self, placa, modelo, tipoVeiculo, tipoServico, dataEntrada):
        self.visualizarDadosEstacionamento()
        vaga = Vaga.Vaga(self.nome, tipoServico, dataEntrada, tipoVeiculo, "disponivel")
        retorno = vaga.verificarServicoEDataEntrada(placa, tipoServico)
        valor = 0.0
        if (retorno == "OK"):
            idVaga = vaga.buscarVagaDisponivel()
            if (idVaga == ""):
                retorno = "Não há vagas disponíveis!"
            else:
                if (tipoVeiculo=="carro"):            
                    if (tipoServico=="diaria") or (tipoServico=="mensal"):
                        valor = self.calcularValor(tipoServico, tipoVeiculo, dataEntrada, "")
                        retorno = "O carro pode ser estacionado na vaga %d. Serviço Diaria ou Mensal: receber pgto antecipado." %(idVaga)      
                    else:
                        retorno = "O carro pode ser estacionado na vaga %d. Serviço Hora: receber pgto na saída." %(idVaga)                 
                else:
                    if (tipoServico=="diaria") or (tipoServico=="mensal"):
                        valor = self.calcularValor(tipoServico, tipoVeiculo, dataEntrada, "")
                        retorno = "A moto pode ser estacionada na vaga %d. Serviço Diária ou Mensal: receber pgto antecipado." %(idVaga)       
                    else:
                        retorno = "A moto pode ser estacionada na vaga %d. Serviço Hora: receber pgto na saída." %(idVaga)                 
                vaga.registrarEntradaVeiculo(idVaga, placa, modelo, valor)
        print(retorno)
        return retorno
    
    def calcularValor(self, tipoServico, tipoVeiculo, dataEntrada, dataSaida):
        taxa = Taxa.Taxa(self.nome, "", "", "", "", "", "")  
        taxa.visualizarTaxas()
        if (tipoVeiculo == "carro"):
            if (tipoServico == "diaria"):
                retorno = taxa.taxaDiariaC
            elif (tipoServico == "mensal"):
                retorno = taxa.taxaMensalC
            else:
                res = dataSaida-dataEntrada                
                tempo_s = res.seconds
                #segundos = tempo_s % 60
                tempo_m = tempo_s / 60
                minutos = tempo_m % 60
                horas = int(tempo_m / 60)
                taxaHoras = taxa.taxa15minC*4
                precoHoras = taxaHoras*horas
                if (minutos <= 15):
                    precoMinutos = taxa.taxa15minC
                elif (15 < minutos <= 30):
                    precoMinutos = taxa.taxa15minC*2
                elif (30 < minutos <= 45):
                    precoMinutos = taxa.taxa15minC*3
                else:
                    precoMinutos = taxa.taxa15minC*4
                retorno = precoHoras + precoMinutos                    
        else:
            if (tipoServico == "diaria"):
                retorno = taxa.taxaDiariaM
            elif (tipoServico == "mensal"):
                retorno = taxa.taxaMensalM
            else:
                res = dataSaida-dataEntrada                
                tempo_s = res.seconds
                #segundos = tempo_s % 60
                tempo_m = tempo_s / 60
                minutos = tempo_m % 60
                horas = int(tempo_m / 60)
                #print( horas,'horas',minutos, 'minutos e',segundos,'segundos')
                taxaHoras = taxa.taxa15minM*4
                precoHoras = taxaHoras*horas
                if (minutos <= 15):
                    precoMinutos = taxa.taxa15minM
                elif (15 < minutos <= 30):
                    precoMinutos = taxa.taxa15minM*2
                elif (30 < minutos <= 45):
                    precoMinutos = taxa.taxa15minM*3
                else:
                    precoMinutos = taxa.taxa15minM*4
                retorno = precoHoras + precoMinutos 
        return retorno
                
    def registrarSaidaVeiculo(self, placa, tipoServico, dataSaida, disponibilizarVaga):
        vaga = Vaga.Vaga(self.nome, tipoServico, "", "", "")
        idVaga = vaga.buscarVagaOcupada(placa, tipoServico)
        if idVaga!="":
            dataEntradaD = datetime.datetime.strptime(vaga.dataEntrada, '%Y-%m-%d %H:%M:%S') 
            dataSaidaD = datetime.datetime.strptime(dataSaida, '%Y-%m-%d %H:%M:%S')
            if (tipoServico == "hora"): 
                valor = self.calcularValor(tipoServico, vaga.tipoVeiculo, dataEntradaD, dataSaidaD)
                retorno = "Valor a ser pago: %f. Veículo estacionado na vaga %d." %(valor, idVaga)
                vaga.registrarSaidaVeiculo(idVaga, valor, dataSaida)
            else: 
                retorno = "Valor já foi pago na entrada. Veículo estacionado na vaga %d." %(idVaga)
                if (disponibilizarVaga == "Sim"):
                    vaga.registrarSaidaVeiculo(idVaga, "", dataSaida)
        else:
            retorno = "Veículo não deu entrada."
        return retorno  
        
  