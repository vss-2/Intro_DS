library(XML)
library(xlsx)
library(csv)

arquivo1 <- 'https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2Fss06hid.csv'
arquivo2 <- 'https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2FDATA.gov_NGAP.xlsx'
arquivo2 <- 'https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2Frestaurants.xml '

if(!file.exists('casa.csv')){
    # Fontes de estudo: https://r4ds.had.co.nz/data-import.html
    # https://swcarpentry.github.io/r-novice-inflammation/11-supp-read-write-csv/
    
    download.file(arquivo1, destfile='./casa.csv', method='curl')
    
    # Importar com primeira linha de colunas nomeadas
    read_csv("casa.csv", col_names = c("coluna1", "coluna2", "coluna3"))
    
    casas <- read.csv(file='casa.csv', stringsAsFactors=FALSE)
    # Os stringsAsFactores impede que ao performar alguma atividade 
    # os valores sejam convertidos de strings para fator
    # Por exemplo:
    casas$RT <- ifelse(casas$RT == 'P', 'G', casas$RT)
    # Ele converterá todos os P em G, mas o tipo str 
    # será convertido para fator caso stringsAsFactors=TRUE
    # Caso contrário, teríamos que fazer:
    casas$RT <- ifelse(as.character(casas$RT) == 'P', 'G', as.character(casas$RT))
    # Caso queira gravar um novo arquivo sem que 
    # a primeira coluna ser composta por números:
    write.csv(casas$RT, file='casasRT.csv', row.names = FALSE)
    # Caso queria definir uma regra para substituir valores NA, faça:
    write.csv(casas$RT, file='casasRT.csv', row.names = FALSE, na = 'G')
}

if(!file.exists('gas.xlsx')){
    download.file(arquivo2, destfile='./gas.xlsx', method='curl')
    dat <- read.xlxs('gas.xlsx', sheetIndex=1, colIndex=NULL, rowIndex=NULL)
    # Um arquivo excel pode ter várias páginas, então especificamos a primeira
    # Os outros dois parâmetros definem os índices de 1a linha e 1a coluna a serem importadas
    # NULL indica que todas encontradas serão trazidas para dat.
    # Caso contrário, usar startRow e endRow; não existe startCol ou endCol.
    # dat[18,23]
    (sum(dat$Zip*dat$Ext,na.rm=T)
}

if(!file.exists('restaurante.xml')){
    download.file(arquivo3, destfile='./restaurante.xml', method='curl')
    restaurantes = XMLParse(file = 'restaurante.xml')
    
    # Exibindo o código postal de cada restaurante, para encontrar devo ir: response->row->row->zipcode
    codigoPostal = setNames(XMLtoDataFrame(node = getNodes(restaurantes, '//response//row//row//zipcode')), 'Código Postal')
    nomeRest = setNames(XMLtoDataFrame(node = getNodes(restaurantes, '//response//row//row//name')), 'Nome do Restaurante')

    # Para montar um dataframe posso fazer
    xmldf <- cbind(codigoPostal, nomeRest)
}
