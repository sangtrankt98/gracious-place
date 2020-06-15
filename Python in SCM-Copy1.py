#!/usr/bin/env python
# coding: utf-8

# In[27]:


#Ipsum function can help you to tackle the complex problems
from pulp import *

# Initialize Model
model = LpProblem("Minimize Transportation Costs", LpMinimize)

# Build the lists and the demand dictionary
 #Sets
plants_var = ['Ethiopia', 'Tanzania','Nigeria']
demand_var = ['Ginko', 'Kola']
 #Dictionary
plants_cap = [425,400,750]
demand_num = [550, 450]
demand = dict(zip(demand_var, demand_num))
plants = dict(zip(plants_var, plants_cap))

# Build the trans cost dictionary
cost={'Ethiopia':{'Ginko':21  , 'Kola':22.5},
      'Tanzania':{'Ginko':22.5, 'Kola':24.5},
      'Nigeria' :{'Ginko':23  , 'Kola':25.5}}

# Build decision variable
routes= [(i,j) for i in plants_var for j in demand_var]
var = LpVariable.dicts("Shipments",(plants_var,demand_var),0,None,LpInteger)

# Define Objective Function
model += lpSum([cost[i][j] * var[i][j] 
                for (i,j) in routes])

# For each customer, sum plants shipments and set equal to customer demand
for i in plants_var:
    model += lpSum([var[i][j] for j in demand_var]) <= plants[i]
for j in demand_var:
    model += lpSum([var[i][j] for i in plants_var]) == demand[j]
    
model.solve()
print("Status:", LpStatus[model.status])
for v in model.variables():
    print(v.name,"=",v.varValue)
print("Total cost =",value(model.objective))

