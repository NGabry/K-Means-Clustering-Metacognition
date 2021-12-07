import random

import numpy as np
import pandas as pd

def randrange_float(start, stop, step):
    return random.randint(0, int((stop-start) / step)) * step + start

if __name__ == '__main__':

    #Make a high-MC low-PD dataframe
    MAS_S = []
    MAS_O = []
    MAS_D = []
    MAS_M = []
    PD_Traits = []
    for i in range (0,33333):
        s   = randrange_float(5.5,8,.01)
        MAS_S.append(s)
        o   = randrange_float(4,6,.01)
        MAS_O.append(o)
        d   = randrange_float(1.5,3,.01)
        MAS_D.append(d)
        m   = randrange_float(4.5,8,.01)
        MAS_M.append(m)
        pdt = random.randint(0,27)
        PD_Traits.append(pdt)

    df1 = pd.DataFrame(list(zip(MAS_S, MAS_O, MAS_D, MAS_M, PD_Traits)),
                      columns = (['MAS_S', 'MAS_O', 'MAS_D', 'MAS_M', 'PD']))

    #Make a low-MC high-PD dataframe
    MAS_S = []
    MAS_O = []
    MAS_D = []
    MAS_M = []
    PD_Traits = []
    for i in range (0,33333):
        s   = randrange_float(3,4.5,.01)
        MAS_S.append(s)
        o   = randrange_float(2,2.5,.01)
        MAS_O.append(o)
        d   = randrange_float(0,1,.01)
        MAS_D.append(d)
        m   = randrange_float(1,3,.01)
        MAS_M.append(m)
        pdt = random.randint(28,50)
        PD_Traits.append(pdt)

    df2 = pd.DataFrame(list(zip(MAS_S, MAS_O, MAS_D, MAS_M, PD_Traits)),
                      columns = (['MAS_S', 'MAS_O', 'MAS_D', 'MAS_M', 'PD']))

    #Make a high-MC high-PD dataframe
    MAS_S = []
    MAS_O = []
    MAS_D = []
    MAS_M = []
    PD_Traits = []
    for i in range (0,33333):
        s   = randrange_float(6,8,.01)
        MAS_S.append(s)
        o   = randrange_float(4.5,6,.01)
        MAS_O.append(o)
        d   = randrange_float(1.5,3,.01)
        MAS_D.append(d)
        m   = randrange_float(5,8,.01)
        MAS_M.append(m)
        pdt = random.randint(37,50)
        PD_Traits.append(pdt)

    df3 = pd.DataFrame(list(zip(MAS_S, MAS_O, MAS_D, MAS_M, PD_Traits)),
                      columns = (['MAS_S', 'MAS_O', 'MAS_D', 'MAS_M', 'PD']))


    #Concatenage all dataframes
    full_df = pd.concat([df1,df2,df3], ignore_index=True)

    #Sprinkle in random 999s
    ids_to_alt = []
    for i in range (0,156):
        j = random.randint(0,99999)
        ids_to_alt.append(j)

    for i in ids_to_alt:
        full_df.loc[i] = 999

    full_df.to_csv('Metacog_PD.csv',index=False)
