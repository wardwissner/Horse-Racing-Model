import itertools
import numpy as np
import pandas as pd
l = []
df = pd.read_excel("Aqueduct_Summary6.xlsx",sheetname="RACE1")
print(df)
for item in range(0, len(df["Post"])):
  l.append(item)
print(l)
ex_prob_t=[]
ex_t=[]
for items in range(0,len(df["Post"])):
  ex_prob_t.append(df["Exacta"+str(items+1)])
  ex_t.append(df["Pay_Exacta"+ str(items+1)])
exacta_t = np.array(ex_t)
print (exacta_t)
exacta=np.transpose(exacta_t)
print(exacta)
exacta_prob_t = np.array(ex_prob_t)
print(exacta_prob_t)
exacta_prob=np.transpose(exacta_prob_t)
print(exacta_prob)

product = exacta * exacta_prob
print(product.shape)
ones_matrix = np.ones(product.shape)
ex_1 = exacta + ones_matrix
profit = ex_1 * exacta_prob - ones_matrix
print(ones_matrix)
print(product)
print(exacta)
print(exacta_prob)
print(ex_1)
print(profit)
print(profit[0][0])
box = {}
b = list(itertools.combinations(l, 3))
for combo in b:
  c = list(combo)
  print(c)
  d = list(itertools.permutations(c, 2))
  print(d)
  pr = 0
  for perm in d:
    print(perm)
    print(perm[0], perm[1])
    pr += profit[perm[0]][perm[1]]
    print(pr, perm, perm[0], perm[1])
  label=np.array(combo)+([1,1,1])
  label=str(label)
  box[label] = pr
  print(box)
cc = max(box, key=box.get)
print("BOX ", cc, "PROFIT ",box[cc])
