library(maptools)
library(RColorBrewer)

####Read table####
otu <-read.table(file="otu_table.xls",sep="\t",head=T,check.names = FALSE,quote="\"")
rownames(otu) <-as.character(otu[,1])
otu <-otu[,-1]

####Read group####
gs <-"groupall.txt"
gp<-read.table(file="groupall.txt",stringsAsFactors=T,header=T,sep="\t",colClasses=c('character','character'))
sns<-as.character(gp[,1])
otu<-otu[,sns]
otu$sum<-rowSums(otu)
otu<-otu[otu$sum>0,]
myvars<-colnames(otu) %in% "sum"
otu<-otu[,!myvars]
otu <-t(otu)

####PCA analysis####
dir.create("PCA")
dir.create("PCA/groupall")
otu.pca<- prcomp(otu,center = TRUE, scale= TRUE)
pc<-summary(otu.pca)
rotat<-paste("PCA/groupall/","pca.rotation.xls",sep="")
ord<-paste("PCA/groupall/","pca_ordination.xls",sep="")
write.table(otu.pca$rotation[,c(1,2)],rotat,sep="\t",quote=F,col.names=NA)
write.table(otu.pca$x[,c(1,2)],ord,sep="\t",quote=F,col.names=NA)
mex<-0.2*abs(max(otu.pca$x[,1])-min(otu.pca$x[,1])) 
mey<-0.1*abs(max(otu.pca$x[,2])-min(otu.pca$x[,2]))
mypch <-rep(c(21:25),5)
col0<-c("#3a89cc","#cd0000","#458b00","#ae429b","#009999","#ff9933","#ff6600","#ff6699","#00cc33","#cc3366","#ccaa99","#ff3366","#3366ff","#99cc66","#66cdaa","#632b28", "#006538","#4693ec")
col1<-brewer.pal(9,"Set1")
col2<-brewer.pal(8,"Dark2")
mycol<-unique(c(col0,col2,col1))

####plot PCA ####
PCA<-paste("PCA/groupall/","PCA.pdf",sep="")
pdf(PCA,width=6,height=6)
par(mar=c(5,5,4,4))
plot(otu.pca$x[,1],otu.pca$x[,2],tck=-0.01,las=1,cex=0.6,xlim=c(min(otu.pca$x[,1])-mex,max(otu.pca$x[,1])+mex),ylim=c(min(otu.pca$x[,2])-mey,max(otu.pca$x[,2])+mey),xlab=paste("PC1",":",round(pc[[6]][2,1]*100,2),"%",sep=""),ylab=paste("PC2",":",round(pc[[6]][2,2]*100,2),"%",sep=""),main="PCA",pch=21,col=mycol[factor(gp$group,levels=unique(gp$group))],bg=mycol[factor(gp$group,levels=unique(gp$group))]) 
abline(h=0,v=0,lty=2,col="gray")
pointLabel(otu.pca$x[,1],otu.pca$x[,2],labels=paste("\n","  ",rownames(otu),"  ","\n",sep=""),col= mycol[factor(gp$group,levels=unique(gp$group))],cex=0.6,allowSmallOverlap = FALSE)

dev.off()

