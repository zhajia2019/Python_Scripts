#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 13:47:01 2018

@author: zhaoyanjiang
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 22:49:25 2018

@author: zhaoyanjiang
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 22:13:10 2018

@author: zhaoyanjiang
"""

import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

# set color palette
sns.set_style("ticks")
flatui = ["#FF9900","#99FFFF"]
colorset = sns.color_palette(flatui)
sns.set_palette(colorset)


#load file
LDabx = pd.read_csv("/Users/zhaoyanjiang/Desktop/GM_GS_201807/Data/HuFMT/Bile_acids/HuFMT_BAs.csv")


# subplot size, length*width
plt.figure(figsize=(12, 4))

#subplots row*column 2*4(#)
# boxplot, showmeans,notch=True

plt.subplot(241)
sns.despine()
sns.swarmplot(x="Group", y="TBA",order=("FMT.GS","FMT.GSF"),data=LDabx,palette= sns.light_palette("red", reverse=True),size=5);
sns.barplot(x="Group", y="TBA",order=("FMT.GS","FMT.GSF"),data=LDabx,capsize=0.2,ci=68,errwidth=1);
plt.xlabel(" ")
plt.ylabel("TBA (umol/L)")
plt.title(" ",size=10)
# set y axis range min-max:0~80000 
plt.ylim(0, 400000)

plt.subplot(242)
sns.despine()
sns.swarmplot(x="Group", y="TauroBA",order=("FMT.GS","FMT.GSF"),data=LDabx,palette= sns.light_palette("red", reverse=True),size=5);
sns.barplot(x="Group", y="TauroBA", order=("FMT.GS","FMT.GSF"),data=LDabx,capsize=0.2,ci=68,errwidth=1);
plt.xlabel(" ")
plt.ylabel("TauroBA (umol/L)")
plt.title(" ",size=10)
plt.ylim(0, 400000)

plt.subplot(243)
sns.despine()
sns.swarmplot(x="Group", y="GlycoBA",order=("FMT.GS","FMT.GSF"),data=LDabx,palette= sns.light_palette("red", reverse=True),size=5);
sns.barplot(x="Group", y="GlycoBA", order=("FMT.GS","FMT.GSF"),data=LDabx,capsize=0.2,ci=68,errwidth=1);
plt.xlabel(" ")
plt.ylabel("GlycoBA (umol/L)")
plt.title(" ",size=10)
plt.ylim(0, 60000)

plt.subplot(244)
sns.despine()
sns.swarmplot(x="Group", y="ucBA",order=("FMT.GS","FMT.GSF"),data=LDabx,palette= sns.light_palette("red", reverse=True),size=5);
sns.barplot(x="Group", y="ucBA", order=("FMT.GS","FMT.GSF"),data=LDabx,capsize=0.2,ci=68,errwidth=1);
plt.xlabel(" ")
plt.ylabel("ucBA (umol/L)")
plt.title(" ",size=10)
plt.ylim(0, 6000)



# seperate subplots space,ws(wide),hs(height)
plt.subplots_adjust(wspace=0.9,hspace=0.5)

# save high quality figure to filename
plt.savefig("HuFMT_GB_totalBA.png",dpi=600,papertype="A4") 
plt.show()



