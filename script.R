#pegando csv q tem o nome e id de tds os q responderam aos 4 foruns da disciplina
dados2 = read.csv2('C:\\Users\\Pamella\\Documents\\PIC Pamella\\PIC2020\\moodle\\Parte2\\informaticaAplicada\\info_qmrespondeu_4foruns.csv' , sep=';', dec='.')

#passo 1: adicionando nome e id

#pegando a coluna userid
id = dados2[5]
#pegando a coluna nome
nome = dados2[6]
#dataframe c nome e userid
infoidenome <- data.frame(id,nome)

#passo 2: ADICIONAR AS METRICAS
#RODA CINCO VEZES DE ACORDO C AS METRICAS E MUDAS O INDICE DA COLUNA NO FOR
#LEMBRAR MUDAR OS DIRETORIOS !!!!!!

metforum = read.csv2('C:\\Users\\Pamella\\Documents\\PIC Pamella\\PIC2020\\moodle\\Parte2\\informaticaAplicada\\forum58\\metricas_forum58.csv' , sep=';', dec='.')
#pegando os user id do dados2 e colocando em teste2
teste2 = dados2[2]


#criando as colunas  refreentes as metricas 
#MUDAR O EACH DE ACORDO C A QUANTIDADE DO DADOS2
indegree <- rep(c(0),each=175)
outdegre <- rep(c(0),each=175)
degre <- rep(c(0),each=175)
closenes <- rep(c(0),each=175)
betwenes <- rep(c(0),each=175)

#adicionando as colunas ao o dataframe
teste2$indegre <- indegree
teste2$outdegre <- outdegre
teste2$degre <- degre
teste2$closenes <- closenes
teste2$betwenes <- betwenes


#percorrer o csv metFORUM p achar as metricas e colocar no data frame metrica
for(i in 1:176){#mudar de acordo c o csv METFORUM IMPORTADO
  for(j in 1:175){ #mudar de acordo c o csv infoidnome "DADOS2" IMPORTADO
    if (teste2[j,1] == metforum[i,1]){#mudar a coluna aqui
        teste2[j,6] <- metforum[i,6]#mudar a coluna aqui #a partir da COLUNA DOIS 2 ATE A SEIS!!!!!
    }
  
  }}

#passo 3 adicionar notas

infonota = read.csv2('C:\\Users\\Pamella\\Documents\\PIC Pamella\\PIC2020\\moodle\\Parte2\\informaticaAplicada\\forum58\\info_qmrespondeu.csv' , sep=';', dec='.')
nota <- rep(c(0),each=175) #MUDAR DE ACORDO C A QUATIDADE DO CSV "DADOS2"
teste2$nota <- nota


for(i in 1:117){#mudar de acordo c o csv INFONOTA
  for(j in 1:175){ #mudar de acordo c o csv infoIDENOME
    if (teste2[j,1] == infonota[i,4]){#mudar a coluna aqui
      teste2[j,7] <- infonota[i,8]#mudar a coluna aqui
    }
    
  }}

#PASSO 4 EXPORTAR O CSV
write.csv2(teste2, "C:\\Users\\Pamella\\Documents\\PIC Pamella\\PIC2020\\moodle\\Parte2\\informaticaAplicada\\forum58\\infonomenotametrica-forum58final.csv", row.names = TRUE)