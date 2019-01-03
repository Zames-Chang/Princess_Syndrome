from princess import Princess_Syndrome 
from numpy import random

def new_cost(arg,table):
    mean = {}
    for char in arg['costs']:
        mean[char] = 0;
        num = 0
        for person in arg['costs'][char]:
            num+=1
            mean[char]+=person
        mean[char]/=num
    num = 0
    for char in arg['costs']:
        for person in range(0,len(arg['costs'][char])):
            if table.values[num][person] == 1:
                arg['costs'][char][person] *=(abs(arg['costs'][char][person]-mean[char])/mean[char]+1)
            else:
                arg['costs'][char][person] *=(-abs(arg['costs'][char][person]-mean[char])/mean[char]+1)
            arg['costs'][char][person] = int(arg['costs'][char][person])+1
        num+=1
    return arg;

arg = {
    'characteristic': ["A","B","C"], # 工具人有幾項工作要做
    'peoples' : ["0","1","2","3"], # 手上有幾個工具人(必須是0-n)
    'costs' : {
        'A':[2,4,5,5], # 從0-3號工具人 做Ａ工作所需要的cost
        'B':[0,99,99,5], # 從0-3號工具人 做B工作所需要的cost
        'C':[1,2,1,5] # 從0-3號工具人 做C工作所需要的cost
    },
    'quality' : {
        'A':[1,2,3,5], # 從0-3號工具人 做Ａ工作所做的品質（可以想成工具人寫作業，每個工具人寫出來的分數不一樣）
        'B':[4,5,6,5], # 從0-3號工具人 做B工作所做的品質
        'C':[7,8,9,5] # 從0-3號工具人 做C工作所做的品質
    },
    'demand' : {
        'A':2, #A工作最低需要的品質 可以想成你希望工具人幫你寫作業，但至少寫出來要60分吧？
        'B':5, #B工作最低需要的品質
        'C':7  #C工作最低需要的品質
    },
}

Princess = Princess_Syndrome(arg)
result = Princess.solve()
table = Princess.get_table()
print(arg['costs'])
print(table.values)
arg = new_cost(arg,table)
Princess.print_result()
print(arg['costs'])
