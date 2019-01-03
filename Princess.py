from pulp import *
import pandas as pd
import numpy as np
from IPython.display import display, HTML
class Princess_Syndrome(object):
    def __init__(self,arg):
        self.costs = arg['costs']
        self.quality = arg['quality']
        self.demand = arg['demand']
        self.characteristic = arg['characteristic']
        self.peoples = arg['peoples']
        self.prob = LpProblem("Princess_Syndrome Problem",LpMinimize)
        # Creates a list of tuples containing all the possible routes for transport
        self.Routes = [(w,b) for w in self.characteristic for b in self.peoples]
        # A dictionary called self.route_vars is created to contain the referenced variables (the routes)
        self.route_vars = LpVariable.dicts("var",(self.characteristic,self.peoples),0,None,LpInteger)
        self.prob += lpSum([self.route_vars[w][b]*self.costs[w][int(b)] for (w,b) in self.Routes])
        self.table = ""
        for w in self.characteristic:
            self.prob += lpSum([self.route_vars[w][b] for b in self.peoples]) == 1
        # The demand minimum constraints are added to prob for each demand node (bar)
        for b in self.peoples:
            self.prob += lpSum([self.route_vars[w][b] for w in self.characteristic]) <= 1
            self.prob += lpSum([self.route_vars[w][b] for w in self.characteristic]) >= 0
        for w in self.characteristic:
            self.prob += lpSum([self.route_vars[w][b]*self.quality[w][int(b)] for b in self.peoples]) >= self.demand[w]
    def solve(self):
        self.prob.solve()
        print("Status:", LpStatus[self.prob.status])
        return self.prob.variables()
    def loss(self):
        return value(self.prob.objective)
    def print_result(self):
        temp = []
        for v in self.prob.variables():
            temp.append(v.varValue)
        self.table = pd.DataFrame(np.reshape(temp, (len(self.characteristic), len(self.peoples))),columns = self.peoples)
        self.table.index = self.characteristic
        display(self.table)
    def get_table(self):
        temp = []
        for v in self.prob.variables():
            temp.append(v.varValue)
        self.table = pd.DataFrame(np.reshape(temp, (len(self.characteristic), len(self.peoples))),columns = self.peoples)
        self.table.index = self.characteristic
        return self.table
        