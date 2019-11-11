#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 22:13:10 2018

@author: zhaoyanjiang
"""


import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

# set color palette
sns.set_style("ticks")
flatui = ["#FF7F00","#FFFF99","#99FFFF","#38B0DE"]
colorset = sns.color_palette(flatui)
sns.set_palette(colorset)

#load file
GBA = pd.read_csv("/Users/zhaoyanjiang/Desktop/GM_GS_201807/Data/coH/Gene/coH_Liver_Gene1.csv")

# subplot size, length*width
plt.figure(figsize=(12, 4))

#subplots row*column 2*4(#)
# boxplot, showmeans(show an additional green dot for means),notch=True

plt.subplot(241)
sns.despine()
sns.swarmplot(x="Group", y="Abcg5",order=("C","coH.C","coH.A","A"),data=GBA,palette= sns.light_palette("red",reverse=True),size=5);
sns.barplot(x="Group", y="Abcg5", order=("C","coH.C","coH.A","A"),data=GBA,capsize=0.1,ci=68,errwidth=1,edgecolor=sns.light_palette("gray",reverse=True));

plt.xlabel(" ")
plt.ylabel("Abcg5 mRNA (A.U)")
plt.title(" ",size=10)
# set y axis range min-max:0~80000 
plt.ylim(0, 4)


plt.subplot(242)
sns.despine()
sns.swarmplot(x="Group", y="Abcg8",order=("C","coH.C","coH.A","A"),data=GBA,palette= sns.light_palette("red",reverse=True),size=5);
sns.barplot(x="Group", y="Abcg8", order=("C","coH.C","coH.A","A"),data=GBA,capsize=0.1,ci=68,errwidth=1,edgecolor=sns.light_palette("gray",reverse=True));

plt.xlabel(" ")
plt.ylabel("Abcg8 mRNA (A.U)")
plt.title(" ",size=10)
# set y axis range min-max:0~80000 
plt.ylim(0, 3)


plt.subplot(243)
sns.despine()
sns.swarmplot(x="Group", y="Srb1",order=("C","coH.C","coH.A","A"),data=GBA,palette= sns.light_palette("red",reverse=True),size=5);
sns.barplot(x="Group", y="Srb1", order=("C","coH.C","coH.A","A"),data=GBA,capsize=0.1,ci=68,errwidth=1,edgecolor=sns.light_palette("gray",reverse=True));

plt.xlabel(" ")
plt.ylabel("Srb1 mRNA (A.U)")
plt.title(" ",size=10)
# set y axis range min-max:0~80000 
plt.ylim(0, 2)

plt.subplot(244)
sns.despine()
sns.swarmplot(x="Group", y="Ldlr",order=("C","coH.C","coH.A","A"),data=GBA,palette= sns.light_palette("red",reverse=True),size=5);
sns.barplot(x="Group", y="Ldlr", order=("C","coH.C","coH.A","A"),data=GBA,capsize=0.1,ci=68,errwidth=1,edgecolor=sns.light_palette("gray",reverse=True));

plt.xlabel(" ")
plt.ylabel("Ldlr mRNA (A.U)")
plt.title(" ",size=10)
# set y axis range min-max:0~80000 
plt.ylim(0, 2)




plt.subplot(245)
sns.despine()
sns.swarmplot(x="Group", y="Cyp7a1",order=("C","coH.C","coH.A","A"),data=GBA,palette= sns.light_palette("red",reverse=True),size=5);
sns.barplot(x="Group", y="Cyp7a1", order=("C","coH.C","coH.A","A"),data=GBA,capsize=0.1,ci=68,errwidth=1,edgecolor=sns.light_palette("gray",reverse=True));

plt.xlabel(" ")
plt.ylabel("Cyp7a1 mRNA (A.U)")
plt.title(" ",size=10)
# set y axis range min-max:0~80000 
plt.ylim(0, 2)

plt.subplot(246)
sns.despine()
sns.swarmplot(x="Group", y="Cyp8b1",order=("C","coH.C","coH.A","A"),data=GBA,palette= sns.light_palette("red",reverse=True),size=5);
sns.barplot(x="Group", y="Cyp8b1", order=("C","coH.C","coH.A","A"),data=GBA,capsize=0.1,ci=68,errwidth=1,edgecolor=sns.light_palette("gray",reverse=True));

plt.xlabel(" ")
plt.ylabel("Cyp8b1 mRNA (A.U)")
plt.title(" ",size=10)
# set y axis range min-max:0~80000 
plt.ylim(0, 1.5)

plt.subplot(247)
sns.despine()
sns.swarmplot(x="Group", y="Cyp27",order=("C","coH.C","coH.A","A"),data=GBA,palette= sns.light_palette("red",reverse=True),size=5);
sns.barplot(x="Group", y="Cyp27", order=("C","coH.C","coH.A","A"),data=GBA,capsize=0.1,ci=68,errwidth=1,edgecolor=sns.light_palette("gray",reverse=True));

plt.xlabel(" ")
plt.ylabel("Cyp27 mRNA (A.U)")
plt.title(" ",size=10)
# set y axis range min-max:0~80000 
plt.ylim(0, 2)

plt.subplot(248)
sns.despine()
sns.swarmplot(x="Group", y="Cyp2c70",order=("C","coH.C","coH.A","A"),data=GBA,palette= sns.light_palette("red",reverse=True),size=5);
sns.barplot(x="Group", y="Cyp2c70", order=("C","coH.C","coH.A","A"),data=GBA,capsize=0.1,ci=68,errwidth=1,edgecolor=sns.light_palette("gray",reverse=True));

plt.xlabel(" ")
plt.ylabel("Cyp2c70 mRNA (A.U)")
plt.title(" ",size=10)
# set y axis range min-max:0~80000 
plt.ylim(0, 2)





# seperate subplots space,ws(wide),hs(height)
plt.subplots_adjust(wspace=0.5,hspace=0.5)

# save high quality figure to filename
plt.savefig("coH_Liver_Gene.png",dpi=600,papertype="A4") 
plt.show()



