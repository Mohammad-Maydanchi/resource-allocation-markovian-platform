# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 23:05:10 2021

@author: mzm0181
"""
# Find Optimal Policies
def find_optimal_policies(fuop):
    #Finding uniqe optimal policy variable


    # list of all policies
    x=[]
    for i in fuop.keys():
        x.append(fuop[i])

    #list of uniqe policies
    z=[]
    for i in x:
        if i not in z:
            z.append(i)
    #automation of finding uniqe optimal policy

    strategy=['No-No','No-Gel','Gel-No','Gel-Gel','No-Bio','Bio-No','Bio-Bio','Seq-No','Seq-Gel','Seq-Bio','Bio-Gel','Gel-Bio']#keys
    value2=[] #empty list for values
    opt_dict=dict.fromkeys(strategy,value2) #make dictionary

    NN=[]
    NG=[]
    GN=[]
    GG=[]
    NB=[]
    BN=[]
    BB=[]
    SN=[]
    SG=[]
    SB=[]
    GB=[]
    BG=[]
    for i in z:

        #No-No
        if i[0][1]==1 and i[0][2]==1:
            NN.append(i)
            opt_dict['No-No']=NN

        #No-Gel
        elif i[0][1]==1 and i[0][2]==2:
            NG.append(i)
            opt_dict['No-Gel']=NG

        #Gel-No
        elif i[0][1]==2 and i[0][3]==1:
            GN.append(i)
            opt_dict['Gel-No']=GN

        #Gel-Gel
        elif i[0][1]==2 and i[0][3]==2:
            GG.append(i)
            opt_dict['Gel-Gel']=GG

        #No-Bio
        elif i[0][1]==1 and i[0][2]==3:
            NB.append(i)
            opt_dict['No-Bio']=NB

        #Bio-No
        elif i[0][1]==3 and i[0][4]==1:
            BN.append(i)
            opt_dict['Bio-No']=BN


        #Bio-Bio
        elif i[0][1]==3 and i[0][4]==3:
            BB.append(i)
            opt_dict['Bio-Bio']=BB

        #Seq-No
        elif i[0][1]==4 and i[0][5]==1:
            SN.append(i)
            opt_dict['Seq-No']=SN

        #Seq-Gel
        elif i[0][1]==4 and i[0][5]==2:
            SG.append(i)
            opt_dict['Seq-Gel']=SG

        #Seq-Bio
        elif i[0][1]==4 and i[0][5]==3:
            SB.append(i)
            opt_dict['Seq-Bio']=SB

        #Gel-Bio
        elif i[0][1]==2 and i[0][3]==3:
            GB.append(i)
            opt_dict['Gel-Bio']=GB

        #Bio-Gel
        elif i[0][1]==3 and i[0][4]==2:
            BG.append(i)
            opt_dict['Bio-Gel']=BG

        else:
            print(i)
    return opt_dict