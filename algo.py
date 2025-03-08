#%%
import pandas as pd
from random import randrange


def get_data():
    return pd.read_excel('protein.xlsx')

data = get_data()

# %%
def calculate(data,name, weight):
    data = data[data['name'] == name].iloc[0]
    return {'name': name ,'weight': weight, 'kcal': data['kcal'] * weight , 'fat': data['fat'] * weight, 'protein': data['protein'] * weight, 'carb': data['carb'] * weight}

def calculate_sum(data):
    return {'name': 'Total', 'weight': data['weight'].sum(), 'kcal': data['kcal'].sum(), 'fat': data['fat'].sum(), 'protein': data['protein'].sum(), 'carb': data['carb'].sum()}
def gerenate_data(data,range_of_weight):
    all_names = data['name'].unique()
    result = []
    for name in all_names:
        weight = randrange(range_of_weight)
        result.append(calculate(data, name, weight))
    r =  pd.DataFrame(result)
    result.append(calculate_sum(r))
    return pd.DataFrame(result)

#%%

def select_best(experiences):
    best = experiences[0]
    for e in experiences:
        # favorite protein over fat
        if e['protein'].iloc[-1] > e['fat'].iloc[-1]:
            if e['kcal'].iloc[-1] < best['kcal'].iloc[-1] and e['protein'].iloc[-1] > best['protein'].iloc[-1] and e['fat'].iloc[-1] < best['fat'].iloc[-1] and e['carb'].iloc[-1] < best['carb'].iloc[-1]:
                best = e
    return best

# %%

experiences = []
for i in range(500000):
    experiences.append(gerenate_data(data, 5))

best = select_best(experiences)
best.to_excel('best.xlsx')

# %%
