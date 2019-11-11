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
GBA = pd.read_csv("/Users/zhaoyanjiang/Desktop/GM_GS_201807/Data/coH/Bile_acids/coH_GB_BA.csv")

# subplot size, length*width
plt.figure(figsize=(12, 4))

#subplots row*column 2*4(#)
# boxplot, showmeans(show an additional green dot for means),notch=True

plt.subplot(241)
sns.despine()
sns.swarmplot(x="group", y="TBA",order=("C","coH.C","coH.A","A"),data=GBA,palette= sns.light_palette("red",reverse=True),size=5);
sns.barplot(x="group", y="TBA", order=("C","coH.C","coH.A","A"),data=GBA,capsize=0.1,ci=68,errwidth=1,edgecolor=sns.light_palette("gray",reverse=True));

plt.xlabel(" ")
plt.ylabel("TBA(umol/L)")
plt.title(" ",size=10)
# set y axis range min-max:0~80000 
plt.ylim(0, 600000)

plt.subplot(242)
sns.despine()
sns.swarmplot(x="group", y="TauroBA",order=("C","coH.C","coH.A","A"),data=GBA,palette= sns.light_palette("red",reverse=True),size=5);
sns.barplot(x="group", y="TauroBA", order=("C","coH.C","coH.A","A"),data=GBA,capsize=0.1,ci=68,errwidth=1,edgecolor=sns.light_palette("gray",reverse=True));

plt.xlabel(" ")
plt.ylabel("TauroBA(umol/L)")
plt.title(" ",size=10)
# set y axis range min-max:0~80000 
plt.ylim(0, 600000)

plt.subplot(243)
sns.despine()
sns.swarmplot(x="group", y="GlycoBA",order=("C","coH.C","coH.A","A"),data=GBA,palette= sns.light_palette("red",reverse=True),size=5);
sns.barplot(x="group", y="GlycoBA", order=("C","coH.C","coH.A","A"),data=GBA,capsize=0.1,ci=68,errwidth=1,edgecolor=sns.light_palette("gray",reverse=True));

plt.xlabel(" ")
plt.ylabel("GlycoBA(umol/L)")
plt.title(" ",size=10)
# set y axis range min-max:0~80000 
plt.ylim(0, 60000)



plt.subplot(244)
sns.despine()
sns.swarmplot(x="group", y="ucBA",order=("C","coH.C","coH.A","A"),data=GBA,palette= sns.light_palette("red",reverse=True),size=5);
sns.barplot(x="group", y="ucBA", order=("C","coH.C","coH.A","A"),data=GBA,capsize=0.1,ci=68,errwidth=1,edgecolor=sns.light_palette("gray",reverse=True));

plt.xlabel(" ")
plt.ylabel("ucBA(umol/L)")
plt.title(" ",size=10)
# set y axis range min-max:0~80000 
plt.ylim(0, 150000)



# seperate subplots space,ws(wide),hs(height)
plt.subplots_adjust(wspace=0.5,hspace=0.5)

# save high quality figure to filename
plt.savefig("coH_GBA_TBA.png",dpi=600,papertype="A4") 
plt.show()



