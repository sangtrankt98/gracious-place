#!/usr/bin/env python
# coding: utf-8

# In[27]:
#Link case: https://docs.google.com/presentation/d/1F9KeHI5aldbMunOVy67v_TFhKlQf0toLIW1RWoB9k5s

#Step 1: install PuLP (use Google search to know how)
#Step 2: open IDE (sublime_text,jupyter notebook,spyder, microsoft visual studio...) to run code below

from pulp import *

# Initialize model
model = LpProblem("Minimize Transportation Costs", LpMinimize)

# Build the plants and the demand dictionary
 # Sets
plants_var = ['Ethiopia', 'Tanzania','Nigeria']
demand_var = ['Ginko', 'Kola']
plants_cap = [425,400,750]
demand_num = [550, 450]

 # Dictionary
demand = dict(zip(demand_var, demand_num))
plants = dict(zip(plants_var, plants_cap))

# Build the trans cost dictionary
cost={'Ethiopia':{'Ginko':21  , 'Kola':22.5},
      'Tanzania':{'Ginko':22.5, 'Kola':24.5},
      'Nigeria' :{'Ginko':23  , 'Kola':25.5}}

# Build decision variable
routes= [(i,j) for i in plants_var for j in demand_var]
var = LpVariable.dicts("Shipments",(plants_var,demand_var),0,None,LpInteger)

# Define objective function
model += lpSum([cost[i][j] * var[i][j] 
                for (i,j) in routes])

# For each plant, sum products and set smaller than or equal to plant capacity
for i in plants_var:
    model += lpSum([var[i][j] for j in demand_var]) <= plants[i]
# For each customer, sum plants shipments and set equal to customer demand
for j in demand_var:
    model += lpSum([var[i][j] for i in plants_var]) == demand[j]
  
# Solve the model and get result   
model.solve()
print("Status:", LpStatus[model.status])
for v in model.variables():
    print(v.name,"=",v.varValue)
print("Total cost =",value(model.objective))

