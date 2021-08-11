class Transicao:
  def __init__(self, origem, leitura, destino):
    self.origem=origem
    self.leitura=leitura
    self.destino=destino
  def __str__(self):
    return self.origem + ' '+ self.leitura + ' '+self.destino + ' '


class Automato:
  def __init__(self,caminho,entrada):
    linhas = open(caminho,'r').readlines()
    self.entrada=entrada[0:len(entrada)-1]
    self.est_inicial=linhas[0][0]
    self.atual=[self.est_inicial]
    finais = linhas[1].split(',')
    finais[len(finais) - 1] = finais[len(finais) - 1][0]
    self.est_final = finais

    transicoes= linhas[2].split(',')
    self.transicoes=[]
    for i in range(len(transicoes)):
      origem=transicoes[i][1]
      leitura=transicoes[i][3]
      destino=transicoes[i][5]
      self.transicoes.append(Transicao(origem, leitura,destino))
  def processar(self):
    for i in range(len(self.entrada)):
      simbolo=self.entrada[i]
      estado_atual=[]
      for j in range(len(self.transicoes)):
        if self.transicoes[j].origem in self.atual and self.transicoes[j].leitura==simbolo:
          estado_atual.append(self.transicoes[j].destino)
      self.atual=estado_atual
    flag_pertence = False
    for i in self.atual:
      if i in self.est_final:
        return 1
    if not flag_pertence:
      return 0      


saida=open('saida.txt','w') 
entradas=open('entrada.txt','r').readlines()
for entrada in entradas:
  automato=Automato('automato.txt',entrada)
  resultado=automato.processar()
  saida.write(str(resultado)+'\n')
saida.close()