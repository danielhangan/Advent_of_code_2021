with open("/home/scooch/Downloads/day_3_input.txt") as f:
    lines = f.readlines()

import pandas as pd

d = {
        "col1": [],
        "col2": [],
        "col3": [],
        "col4": [],
        "col5": [],
        "col6": [],
        "col7": [],
        "col8": [],
        "col9": [],
        "col10": [],
        "col11": [],
        "col12": []
        }

dt = pd.DataFrame(data=d)

for line in lines:
    line = list(line.strip())
    dt.loc[len(dt)] = line


def day_3_1():
    gamma = ''
    epsilon = ''

    for col in dt.columns:
        if dt[col].astype(int).sum() > 500:
            gamma = gamma + '1'
            epsilon = epsilon + '0'
        else:
            gamma = gamma + '0'
            epsilon = epsilon + '1'

    return int(gamma, 2) * int(epsilon, 2)

def day_3_2(): 
    return int(oxygen(dt,0), 2) * int(co2(dt,0) ,2)

def oxygen(df: pd.DataFrame, index: int):    
    if len(df) == 1:
        return "".join(df.iloc[0])

    new_index = index + 1
    
    if df.iloc[:,index].astype(int).sum() >= len(df) / 2:
        return oxygen(df[df.iloc[:,index] == "1"], new_index)
    return oxygen(df[df.iloc[:,index] == "0"], new_index)


def co2(df: pd.DataFrame, index: int):    
    if len(df) == 1:
        return "".join(df.iloc[0])

    new_index = index + 1
    
    if df.iloc[:,index].astype(int).sum() >= len(df) / 2:
        return co2(df[df.iloc[:,index] == "0"], new_index)
    
    return co2(df[df.iloc[:,index] == "1"], new_index)

print(day_3_1())
print(day_3_2())
