# Importando quatro bibliotecas, 
# de variacao uniforme
# de biblioteca de random inteiro
# de datas
# de arquivos

from random import uniform
from random import randint
import datetime
import os

texto = []

# Gerador de 100 valores de altura e peso
# A altura varia de 1.5 a 2.2
# O peso varia de 50 a 120
# Temos um inteiro aleatorio de 0 a 10

def obterTexto():
      for x in range(1,100):
            texto.append(str(uniform(1.50, 2.20)) + ';\t' + str(uniform(50, 120)) + ';\t' + str(randint(0, 10)) + '\n')
      return texto


# Pegamos o diretorio
# Damos a entrada a o lugar de gravar, permissoes, e codificacao
# O codigo de diretorio foi corrigido para aceitar Windows, Mac e Linux

def criarArquivo(ano, mes, dia, hor, minu):
      try: 
            nomeArquivo = ano+mes+dia+hor+minu+'.txt'
            arquivoAberto = open(nomeArquivo, 'w+')
            return arquivoAberto
      except IOError:
            deletar = input('Já existe um arquivo com o mesmo nome, deseja deletar (s/n)?')
            if(deletar == 's'):
                os.remove('')
                criarArquivo(ano, mes, dia, hor, minu)
            else:
                  print('Não podem haver dois arquivos com o mesmo nome. Encerrando programa!')
                  exit()

def gerarArquivo():
      # diretorio = r'%s' % os.getcwd().replace('\\','/')
      # entrada = open(diretorio, 'w+', encoding = 'UTF-8')
      completo = datetime.datetime.now()
      ano = completo.strftime('%Y')
      mes = completo.strftime('%m')
      dia = completo.strftime('%d')
      hor = completo.strftime('%H')
      minu = completo.strftime('%m')
      arquivo = criarArquivo(str(ano), str(mes), str(dia), str(hor), str(minu))
      arquivo.writelines(obterTexto())
      arquivo.close()
      return

if __name__ == '__main__':
      gerarArquivo()
      exit()
