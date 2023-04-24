# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
# Transition Probability Matrix


def newTransProb(z1=0.1, z2=0.1,
                 alpha1N=0, beta1N=1, alpha1G=0.1, beta1G=0.1, alpha1B=0.05, beta1B=0.05, alpha1S=0.0001, beta1S=0.0001,
                 r=15, showTable=False):  # r is decimal point number for rounding
    # In the sequencing step we have a dummy operation so z3=0
    # showTable: if you want to see Pa0, Pa1, Pa2,Pa3,Pa4 as table
    # seprately , keep it True but if you want to see result of
    # Transition Probablity change it to False
    # we do not have different values for alpha1B and alpha2B , also beta1B and beta2B

    alpha2N = alpha1N
    beta2N = beta1N

    alpha2G = alpha1G
    beta2G = beta1G

    alpha2B = alpha1B
    beta2B = beta1B

    alpha3S = alpha1S
    beta3S = beta1S


#     #First Inspection
#     alpha1N=0     #alpha when first inspection is Nothing is 0 and beta is 1
#     beta1N=1
#     #alpha1G=0.1
#     #beta1G=0.1
#     alpha1B=0.05
#     beta1B=0.05
#     alpha1S=0.0001
#     beta1S=0.0001

#     #Second Inspection: It does not have sequencing as an inspection
#     alpha2N=0
#     beta2N=1
#     #alpha2G=0.1
#     #beta2G=0.1
#     alpha2B=0.05
#     beta2B=0.05

#     #Third Inspection: Only sequencing
#     alpha3S=0.0001   #alpha when third inspection is Gel electrophorisis
#     beta3S=0.0001

    # Part0:  Step 0 to Step1
    P00010 = 1

    # Part1:  P(I1p)= (1− αlpha1)∗(1−z1) + beta1∗z1     Step 1 to Step2

    P01021 = ((1-alpha1N)*(1-z1)+beta1N*z1)
    P01032 = ((1-alpha1G)*(1-z1)+beta1G*z1)
    P01043 = ((1-alpha1B)*(1-z1)+beta1B*z1)
    P01054 = ((1-alpha1S)*(1-z1)+beta1S*z1)

    # Part2:  P(I2p|I1p)= (1− alpha1)∗(1−z1) ∗(1− alpha2) ∗(1−z2) /P(I1p)    +  (𝑏𝑒𝑡𝑎1∗𝑧1 ∗𝑏𝑒𝑡𝑎2∗(1−𝑧2))/P(I1p) + beta2* z2
    # Step 2 to Step 3

    P02061 = (((1 - alpha1N)*(1-z1) * (1 - alpha2N) * (1-z2) / P01021) +
              (beta1N*z1 * beta2N*(1-z2)/P01021) + (beta2N * z2))
    P02072 = (((1 - alpha1N)*(1-z1) * (1 - alpha2G) * (1-z2) / P01021) +
              ((beta1N*z1 * beta2G*(1-z2))/P01021) + (beta2G * z2))
    P02083 = (((1 - alpha1N)*(1-z1) * (1 - alpha2B) * (1-z2) / P01021) +
              ((beta1N*z1 * beta2B*(1-z2))/P01021) + (beta2B * z2))

    P03092 = (((1 - alpha1G)*(1-z1) * (1 - alpha2G) * (1-z2)/P01032) +
              ((beta1G*z1 * beta2G*(1-z2))/(P01032)) + (beta2G * z2))
    P03101 = (((1 - alpha1G)*(1-z1) * (1 - alpha2N) * (1-z2)/P01032) +
              ((beta1G*z1 * beta2N*(1-z2))/P01032) + (beta2N * z2))
    P03113 = (((1 - alpha1G)*(1-z1) * (1 - alpha2B) * (1-z2) / P01032) +
              ((beta1G*z1 * beta2B*(1-z2))/P01032) + (beta2B * z2))

    P04123 = (((1 - alpha1B)*(1-z1) * (1 - alpha2B) * (1-z2) / P01043) +
              ((beta1B*z1 * beta2B*(1-z2))/P01043) + (beta2B * z2))
    P04131 = (((1 - alpha1B)*(1-z1) * (1 - alpha2N) * (1-z2) / P01043) +
              ((beta1B*z1 * beta2N*(1-z2))/P01043) + (beta2N * z2))
    P04142 = (((1 - alpha1B)*(1-z1) * (1 - alpha2G) * (1-z2) / P01043) +
              ((beta1B*z1 * beta2G*(1-z2))/P01043) + (beta2G * z2))

    P05151 = (((1 - alpha1S)*(1-z1) * (1 - alpha2N) * (1-z2) / P01054) +
              ((beta1S*z1 * beta2N*(1-z2))/P01054) + (beta2N * z2))
    P05162 = (((1 - alpha1S)*(1-z1) * (1 - alpha2G) * (1-z2) / P01054) +
              ((beta1S*z1 * beta2G*(1-z2))/P01054) + (beta2G * z2))
    P05173 = (((1 - alpha1S)*(1-z1) * (1 - alpha2B) * (1-z2)/P01054) +
              ((beta1S*z1 * beta2B*(1-z2))/P01054) + (beta2B * z2))

    # Part3:  Step3 to Step4

    P06184 = ((((1-alpha1N)*(1-alpha2N)*(1-alpha3S)*(1-z1)*(1-z2) + beta1N *
              beta2N*beta3S*z1 + (1-alpha1N)*beta2N*beta3S*(1-z1)*z2))/(P01021*P02061))
    P07184 = ((((1-alpha1N)*(1-alpha2G)*(1-alpha3S)*(1-z1)*(1-z2) + beta1N *
              beta2G*beta3S*z1 + (1-alpha1N)*beta2G*beta3S*(1-z1)*z2))/(P01021*P02072))
    P08184 = ((((1-alpha1N)*(1-alpha2B)*(1-alpha3S)*(1-z1)*(1-z2) + beta1N *
              beta2B*beta3S*z1 + (1-alpha1N)*beta2B*beta3S*(1-z1)*z2))/(P01021*P02083))

    P09184 = ((((1-alpha1G)*(1-alpha2G)*(1-alpha3S)*(1-z1)*(1-z2) + beta1G *
              beta2G*beta3S*z1 + (1-alpha1G)*beta2G*beta3S*(1-z1)*z2))/(P01032*P03092))
    P10184 = ((((1-alpha1G)*(1-alpha2N)*(1-alpha3S)*(1-z1)*(1-z2) + beta1G *
              beta2N*beta3S*z1 + (1-alpha1G)*beta2N*beta3S*(1-z1)*z2))/(P01032*P03101))
    P11184 = ((((1-alpha1G)*(1-alpha2B)*(1-alpha3S)*(1-z1)*(1-z2) + beta1G * beta2B*beta3S*z1 + (1-alpha1G)*beta2B *
              beta3S*(1-z1)*z2))/(P01032*P03113))  # the last probability was P03101, but I changed it because it was not correct

    P12184 = ((((1-alpha1B)*(1-alpha2B)*(1-alpha3S)*(1-z1)*(1-z2) + beta1B *
              beta2B*beta3S*z1 + (1-alpha1B)*beta2B*beta3S*(1-z1)*z2))/(P01043*P04123))
    P13184 = ((((1-alpha1B)*(1-alpha2N)*(1-alpha3S)*(1-z1)*(1-z2) + beta1B *
              beta2N*beta3S*z1 + (1-alpha1B)*beta2N*beta3S*(1-z1)*z2))/(P01043*P04131))
    P14184 = ((((1-alpha1B)*(1-alpha2G)*(1-alpha3S)*(1-z1)*(1-z2) + beta1B *
              beta1G*beta3S*z1 + (1-alpha1B)*beta2G*beta3S*(1-z1)*z2))/(P01043*P04142))

    P15184 = ((((1-alpha1S)*(1-alpha2N)*(1-alpha3S)*(1-z1)*(1-z2) + beta1S *
              beta1N*beta3S*z1 + (1-alpha1S)*beta2N*beta3S*(1-z1)*z2))/(P01054*P05151))
    P16184 = ((((1-alpha1S)*(1-alpha2G)*(1-alpha3S)*(1-z1)*(1-z2) + beta1S *
              beta1G*beta3S*z1 + (1-alpha1S)*beta2G*beta3S*(1-z1)*z2))/(P01054*P05162))
    P17184 = ((((1-alpha1S)*(1-alpha2B)*(1-alpha3S)*(1-z1)*(1-z2) + beta1S *
              beta1B*beta3S*z1 + (1-alpha1S)*beta2B*beta3S*(1-z1)*z2))/(P01054*P05173))

    # Transition Proablity matrix based on each action
    currentState = ['State0', 'State1', 'State2', 'State3', 'State4', 'State5', 'State6',
                    'State7', 'State8', 'State9', 'State10', 'State11', 'State12', 'State13', 'State14',
                    'State15', 'State16', 'State17', 'State18']
    futureState = ['State0', 'State1', 'State2', 'State3', 'State4', 'State5', 'State6',
                   'State7', 'State8', 'State9', 'State10', 'State11', 'State12', 'State13', 'State14',
                   'State15', 'State16', 'State17', 'State18']

    # Pa0   : Transition probability matrix for action a0
    # make a matrix 19*19 and fill diogonal with 1
    Pa0 = np.zeros((19, 19), float)
    np.fill_diagonal(Pa0, 1)

    Pa0[0][0] = 1-P00010
    Pa0[0][1] = P00010

    Pa0 = Pa0.round(r)  # round values of matrix to r decimal points
    table0 = pd.DataFrame(data=Pa0, index=currentState,
                          columns=futureState)  # conver the array to a table

    # Pa1   : Transition probability matrix for action a1
    # make a matrix 19*19 and fill diogonal with 1
    Pa1 = np.zeros((19, 19), float)
    np.fill_diagonal(Pa1, 1)

    Pa1[1][0] = 1-P01021
    Pa1[1][2] = P01021
    # this element is on diagonal and we do not want this to be 1.
    Pa1[1][1] = 0

    Pa1[2][0] = 1-P02061
    Pa1[2][6] = P02061
    # this element is on diagonal and we do not want this to be 1.
    Pa1[2][2] = 0

    Pa1[3][0] = 1-P03101
    Pa1[3][10] = P03101
    # this element is on diagonal and we do not want this to be 1.
    Pa1[3][3] = 0

    Pa1[4][0] = 1-P04131
    Pa1[4][13] = P04131
    # this element is on diagonal and we do not want this to be 1.
    Pa1[4][4] = 0

    Pa1[5][0] = 1-P05151
    Pa1[5][15] = P05151
    # this element is on diagonal and we do not want this to be 1.
    Pa1[5][5] = 0

    Pa1 = Pa1.round(r)  # round values of matrix to r decimal points
    table1 = pd.DataFrame(data=Pa1, index=currentState, columns=futureState)

    # Pa2   : Transition probability matrix for action a2
    # make a matrix 19*19 and fill diogonal with 1
    Pa2 = np.zeros((19, 19), float)
    np.fill_diagonal(Pa2, 1)

    Pa2[1][0] = 1-P01032
    Pa2[1][3] = P01032
    # this element is on diagonal and we do not want this to be 1.
    Pa2[1][1] = 0

    Pa2[2][0] = 1-P02072
    Pa2[2][7] = P02072
    Pa2[2][2] = 0

    Pa2[3][0] = 1-P03092
    Pa2[3][9] = P03092
    Pa2[3][3] = 0

    Pa2[4][0] = 1-P04142
    Pa2[4][14] = P04142
    Pa2[4][4] = 0

    Pa2[5][0] = 1-P05162
    Pa2[5][16] = P05162
    Pa2[5][5] = 0

    Pa2 = Pa2.round(r)  # round values of matrix to r decimal points
    table2 = pd.DataFrame(data=Pa2, index=currentState, columns=futureState)

    # Pa3   : Transition probability matrix for action a3
    # make a matrix 19*19 and fill diogonal with 1
    Pa3 = np.zeros((19, 19), float)
    np.fill_diagonal(Pa3, 1)

    Pa3[1][0] = 1-P01043
    Pa3[1][4] = P01043
    Pa3[1][1] = 0

    Pa3[2][0] = 1-P02083
    Pa3[2][8] = P02083
    Pa3[2][2] = 0

    Pa3[3][0] = 1-P03113
    Pa3[3][11] = P03113
    Pa3[3][3] = 0

    Pa3[4][0] = 1-P04123
    Pa3[4][12] = P04123
    Pa3[4][4] = 0

    Pa3[5][0] = 1-P05173
    Pa3[5][17] = P05173
    Pa3[5][5] = 0

    Pa3 = Pa3.round(r)  # round values of matrix to r decimal points
    table3 = pd.DataFrame(data=Pa3, index=currentState, columns=futureState)

    # Pa4   : Transition probability matrix for action a4
    # make a matrix 19*19 and fill diogonal with 1
    Pa4 = np.zeros((19, 19), float)
    np.fill_diagonal(Pa4, 1)

    Pa4[1][5] = P01054
    Pa4[1][0] = 1-P01054
    Pa4[1][1] = 0

    Pa4[6][0] = 1-P06184
    Pa4[6][18] = P06184
    Pa4[6][6] = 0

    Pa4[7][0] = 1-P07184
    Pa4[7][18] = P07184
    Pa4[7][7] = 0

    Pa4[8][0] = 1-P08184
    Pa4[8][18] = P08184
    Pa4[8][8] = 0

    Pa4[9][0] = 1-P09184
    Pa4[9][18] = P09184
    Pa4[9][9] = 0

    Pa4[10][0] = 1-P10184
    Pa4[10][18] = P10184
    Pa4[10][10] = 0

    Pa4[11][0] = 1-P11184
    Pa4[11][18] = P11184
    Pa4[11][11] = 0

    Pa4[12][0] = 1-P12184
    Pa4[12][18] = P12184
    Pa4[12][12] = 0

    Pa4[13][0] = 1-P13184
    Pa4[13][18] = P13184
    Pa4[13][13] = 0

    Pa4[14][0] = 1-P14184
    Pa4[14][18] = P14184
    Pa4[14][14] = 0

    Pa4[15][0] = 1-P15184
    Pa4[15][18] = P15184
    Pa4[15][15] = 0

    Pa4[16][0] = 1-P16184
    Pa4[16][18] = P16184
    Pa4[16][16] = 0

    Pa4[17][0] = 1-P17184
    Pa4[17][18] = P17184
    Pa4[17][17] = 0

    Pa4 = Pa4.round(r)  # round values of matrix to r decimal points
    table4 = pd.DataFrame(data=Pa4, index=currentState, columns=futureState)

    if showTable == True:
        jadval = input(
            " Which table do you want to see? Choose among Pa0, Pa1, Pa2, Pa3, Pa4")
        if jadval == 'Pa0':
            Table = table0
        elif jadval == 'Pa1':
            Table = table1
        elif jadval == 'Pa2':
            Table = table2
        elif jadval == 'Pa3':
            Table = table3
        elif jadval == 'Pa4':
            Table = table4

        return Table
    else:
        # combine all matrices to 1 array for creating p
        Tp = np.concatenate((Pa0, Pa1, Pa2, Pa3, Pa4))
        return Tp
