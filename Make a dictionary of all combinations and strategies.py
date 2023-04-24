# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 23:09:01 2021

@author: mzm0181
"""
# Make a dictionary of all combinations and strategies
####### all combinations for example for z1,z2 means all combinatrions of z1,z2

def make_dict_comb_stra(fuop,opt_dict):   #fuop is the output of the experiment
    # relate the strategies to the keys
    ldk=list(fuop.keys())  #list of dictionary keys

    NN1=[]
    NG1=[]
    GN1=[]
    GG1=[]
    NB1=[]
    BN1=[]
    BB1=[]
    SN1=[]
    SG1=[]
    SB1=[]
    GB1=[]
    BG1=[]

    for key in ldk:
        #NN
        if fuop[key] in opt_dict['No-No']:
            NN1.append(key)
        #NG
        elif fuop[key] in opt_dict['No-Gel']:
            NG1.append(key)
        #GN
        elif fuop[key] in opt_dict['Gel-No']:
            GN1.append(key)
        #GG
        elif fuop[key] in opt_dict['Gel-Gel']:
            GG1.append(key)
        #NB
        elif fuop[key] in opt_dict['No-Bio']:
            NB1.append(key)
        #BN
        elif fuop[key] in opt_dict['Bio-No']:
            BN1.append(key)
        #BB
        elif fuop[key] in opt_dict['Bio-Bio']:
            BB1.append(key)
        #SN
        elif fuop[key] in opt_dict['Seq-No']:
            SN1.append(key)
        #SG
        elif fuop[key] in opt_dict['Seq-Gel']:
            SG1.append(key)
        #SB
        elif fuop[key] in opt_dict['Seq-Bio']:
            SB1.append(key)
        #GB
        elif fuop[key] in opt_dict['Gel-Bio']:
            GB1.append(key)
        #BG
        elif fuop[key] in opt_dict['Bio-Gel']:
            BG1.append(key)

        else:
            print("The keys in the results of the main functions which we have not grouped them properly {}".format(key))
            
            
    # make a dictionary of all combinations and strategies
    #'No-No','No-Gel','Gel-No','Gel-Gel','No-Bio','Bio-No','Bio-Bio','Seq-No','Seq-Gel','Seq-Bio','Bio-Gel','Gel-Bio'
    valueNN='No-No'
    dict_NN=dict.fromkeys(NN1,valueNN)

    valueNG='No-Gel'
    dict_NG=dict.fromkeys(NG1,valueNG)

    valueGN='Gel-No'
    dict_GN=dict.fromkeys(GN1,valueGN)

    valueGG='Gel-Gel'
    dict_GG=dict.fromkeys(GG1,valueGG)

    valueNB='No-Bio'
    dict_NB=dict.fromkeys(NB1,valueNB)

    valueBN='Bio-No'
    dict_BN=dict.fromkeys(BN1,valueBN)

    valueBB='Bio-Bio'
    dict_BB=dict.fromkeys(BB1,valueBB)

    valueSN='Seq-No'
    dict_SN=dict.fromkeys(SN1,valueSN)

    valueSG='Seq-Gel'
    dict_SG=dict.fromkeys(SG1,valueSG)

    valueSB='Seq-Bio'
    dict_SB=dict.fromkeys(SB1,valueSB)

    valueBG='Bio-Gel'
    dict_BG=dict.fromkeys(BG1,valueBG)

    valueGB='Gel-Bio'
    dict_GB=dict.fromkeys(GB1,valueGB)


    ##conacat all strategies
    dict_NGBS={}
    dict_NGBS.update(dict_NG)
    dict_NGBS.update(dict_NN)
    dict_NGBS.update(dict_GN)
    dict_NGBS.update(dict_GG)
    dict_NGBS.update(dict_NB)
    dict_NGBS.update(dict_BG)
    dict_NGBS.update(dict_BB)
    dict_NGBS.update(dict_BN)
    dict_NGBS.update(dict_SN)
    dict_NGBS.update(dict_SG)
    dict_NGBS.update(dict_SB)
    dict_NGBS.update(dict_GB)
    
    return dict_NGBS