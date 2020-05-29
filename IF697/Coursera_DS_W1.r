library(xml)
library(xlsx)
library(csv)

arquivo1 <- 'https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2Fss06hid.csv'
arquivo2 <- 'https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2FDATA.gov_NGAP.xlsx '
arquivo2 <- 'https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2Frestaurants.xml '

if(!file.exists('casa.csv')){
    download.file(arquivo1, destfile='./casa.csv', method='curl')

}

if(!file.exists('gas.xlsx')){
download.file(arquivo2, destfile='./gas.xlsx', method='curl')
dat <- read.xlxs('gas.xlsx', sheetIndex=1, colIndex=colIndex, rowIndex=rowIndex)
# dat[18,23]
(sum(dat$Zip*dat$Ext,na.rm=T)
}

if(!file.exists('restaurante.xml')){
download.file(arquivo3, destfile='./restaurante.xml', method='curl')
}
