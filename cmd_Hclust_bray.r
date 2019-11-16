library(ape)
library(vegan)

####Read table####
data<-read.table(file="otu_table.xls",head=T,sep="\t",check.names=FALSE,quote="\"")
rownames(data)<-data[,1]
data<-data[,-1]

####Read group####
grp<-"groupall.txt"
group<-read.table(file="groupall.txt",header=T,sep="\t",colClasses=c('character','character'))
gp<-as.character(group$group)
gp_len<-length(unique(gp))
names(gp)<-as.character(group$sample)
sns<-as.character(group[,1])
data<-data[,sns]
data<-data[rowSums(data)>0,]

ms<-length(colnames(data))
if(ms<=40){
  Tsize<-1
}else if(ms>40 && ms<=100){
  Tsize=round(-0.66*log(ms)+3.5,2)
}else if(ms<=350){
  Tsize=-0.0033*ms + 1.21
}

data<-t(data)
dm<-vegdist(data, method="bray",diag=TRUE, upper=TRUE)
df<-paste("Hclust_bray/groupall/","dist_matrix",".xls",sep="")
dir.create("Hclust_bray")
dir.create("Hclust_bray/groupall")
dm2<-as.matrix(dm)
write.table(dm2,df,sep="\t",quote=F,row.names=T,col.names=NA)
dm<-as.dist(dm)

pdfname<-paste("Hclust_bray/groupall/","hclust_tree.pdf",sep="")
if(ms<=10){
	  pdf(pdfname,height=6,width=5)
	  par=par(mar=c(5,4,4,8),xpd=T)
	}else if(ms>10 && ms<=40 ){
	  pdf(pdfname,height=8,width=6)
	  par=par(mar=c(4,4,4,8),xpd=T)
	}else if(ms>40 && ms<=100){
	  pdf(pdfname,height=10,width=8)
	  par=par(mar=c(4,4,4,8),xpd=T) 
	}else{
	  pdf(pdfname,height=16,width=11)
	  par=par(mar=c(4,4,2,6),xpd=T)
	}

tree<-hclust(dm,method="complete")
dendro <- as.dendrogram(tree)
tr <-as.phylo.hclust(tree)
nwk <-paste("Hclust_bray/groupall/","hclust",".tre",sep="")
write.tree(tr,nwk)

mcol<-c("#458b00","#ee3b3b","#005eff","#8a2be2","#e6b735","#009999","#ff9933","#ff6600","#3399ff","#ff6699","#00cc33","#cc3366","#ccaa99","#ff3366","#3366ff","#99cc66","#66cdaa","#632b28", "#006538","#4693ec","#ff0000")
require("RColorBrewer")
col1<-brewer.pal(8,"Set2")
col2<-brewer.pal(8,"Dark2")
col3<-brewer.pal(12,"Paired")
labelColors<-rep(unique(c(mcol,col3,col2,col1)),10)

##get edge color
labelColors<-rep(c(mcol,col3,col2,col1),10)
names(labelColors)<-unique(group[,2])
colLab <- function(n) {
	if(is.leaf(n)) {
		a <- attributes(n)
		labCol<-labelColors[as.character(group[which(group$sample==as.character(a$label)),2])]
		attr(n, "nodePar")<-list(lab.cex=ifelse(0,0,Tsize),lab.col=labCol,pch=21:22,cex = c(0, 0),lwd=0.7)
		attr(n,"edgePar") <- list(col = labCol)
	}else{
	attr(n, "edgePar") <- list(co1="black",lwd=0.8)
	}
	n
}

clusDendro <- dendrapply(dendro, colLab)	
plot(clusDendro,main="Cluster",ann = FALSE, type="rectangle",horiz=TRUE,cex.axis=0.8)
legend('topleft',legend=unique(group$group),col=labelColors,pt.bg=labelColors,pch = 22,border=NA,bty="n", cex = 1,text.col="grey5", inset =-0.1)
dev.off()



