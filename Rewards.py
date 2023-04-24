# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 23:02:23 2021

@author: mzm0181
"""
#Rewards
import numpy as np
import pandas as pd
def rewards(RawMaterialCost=-2, PCRCost=-27, CloningCost=-54.10, SeqCost=-626,
            NoInspCost=0, GelCost=-14, BioCost=-76.25,
            LargeCost=-100000,rewardTable=False): # if you want to see rewards table keep it true, if want to return rewards array
                                           # change it to false when you call it.
    LargeCost=float(LargeCost)   
    r=np.full((19, 5), LargeCost)  # make a matrix all values are largecost
    
#     #inspection Costs
#     NoInspCost=0
#     GelCost=-14      #changing GElCost
#     BioCost=-76.25
#     #SeqCost=-626
    
    
#     #Operastion Costs
#     RawMaterialCost=-2
#     #PCRCost=-27
#     #CloningCost=-54.10
    
    
    #change values    #all costs are combinations of operation cost and corresponding inspection cost
    
    #Start Step
    r000=RawMaterialCost
    r[0][0]=r000

    #PCR Step
    r011= PCRCost+ NoInspCost
    r[1][1]=r011
    r012=PCRCost + GelCost
    r[1][2]=r012
    r013=PCRCost + BioCost
    r[1][3]=r013
    r014=PCRCost + SeqCost
    r[1][4]=r014
    
    #Cloning Step
    r021=CloningCost +  NoInspCost
    r[2][1]=r021
    r022=CloningCost +  GelCost
    r[2][2]=r022
    r023=CloningCost +  BioCost
    r[2][3]=r023

    r031=CloningCost +  NoInspCost
    r[3][1]=r031
    r032=CloningCost +  GelCost
    r[3][2]=r032
    r033=CloningCost +  BioCost
    r[3][3]=r033

    r041=CloningCost +  NoInspCost
    r[4][1]=r041
    r042=CloningCost +  GelCost
    r[4][2]=r042
    r043=CloningCost +  BioCost
    r[4][3]=r043

    r051=CloningCost +  NoInspCost
    r[5][1]=r051
    r052=CloningCost +  GelCost
    r[5][2]=r052
    r053=CloningCost +  BioCost
    r[5][3]=r053

    #Sequencing Step
    r064=SeqCost
    r[6][4]=r064
    r074=SeqCost
    r[7][4]=r074
    r084=SeqCost
    r[8][4]=r084
    r094=SeqCost
    r[9][4]=r094
    r104=SeqCost
    r[10][4]=r104
    r114=SeqCost
    r[11][4]=r114
    r124=SeqCost
    r[12][4]=r124
    r134=SeqCost
    r[13][4]=r134
    r144=SeqCost
    r[14][4]=r144
    r154=SeqCost
    r[15][4]=r154
    r164=SeqCost
    r[16][4]=r164
    r174=SeqCost
    r[17][4]=r174

    r184=0
    r[18][0]=r184



    States=['State0','State1','State2','State3','State4','State5','State6',
               'State7','State8','State9','State10','State11','State12','State13','State14',
               'State15','State16','State17','State18']
    Actions=['a0','a1','a2','a3','a4']
    rewTable=pd.DataFrame(data=r , index=States, columns=Actions)
    if rewardTable==True:
        return rewTable
    else:
        return r