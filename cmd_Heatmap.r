library(gplots)
library(RColorBrewer)
library("vegan")
library("permute")
library("lattice")

####Read table####
data<-read.table(file="genus_abundance.xls",head=T,sep="\t",row.names=1,check.names = FALSE)
data<-data[rowSums(data)>0,]

####Read group####
gs <-"groupall.txt"
group<-read.table(file="groupall.txt",header=T,sep="\t",check.names = FALSE,colClasses=c('character','character'))
sns<-as.character(group[,1])
data<-data[,sns]
data<-data[rowSums(data)>0,]

####discard the species whose total abundance in all samples is less than 0.01
data<-data[-which(apply(data,1,sum)<0.01),]
data<-as.matrix(data)

drows <-vegdist(data,method="bray")
row.clus <- hclust(drows, "aver")
dcols <-vegdist(t(data),method="bray")
col.clus <- hclust(dcols, "aver")

####cell color 
mycol<-colorRampPalette(rev(brewer.pal(11,"RdYlBu")),bias=3.5)(1000)
dir.create("Heatmap")
dir.create("Heatmap/groupall")
pdf(file="Heatmap/groupall/genus_heatmap.pdf",width=8, height=10)
par(xpd=T,mar=par()$mar+c(2,2,2,2))

heatmap.2(data, key.par=list(mgp=c(1, 0.3, 0),mar=c(5, 2.5, 1, 0)),Rowv = as.dendrogram(row.clus),lmat=rbind(c(0,0,3,3,0),c(0,2,1,1,0),c(0,0,4,0,0)),lhei=c(1.5,5,1),lwid=c(0.5,1,4,2,0.3), Colv = as.dendrogram(col.clus),dendrogram=("both"),col=mycol,scale ="none",margins=c(8,15),density.info=c("none"),trace="none",main=c("heatmap"),key.xlab="Relative abundance", vline=NA,hline=NA,cexRow = ifelse(0,0,0.2+1/(log10(nrow(data)))),cexCol =ifelse(0,0, 0.4 + 1/log10(ncol(data))),srtCol=45)
dev.off()
