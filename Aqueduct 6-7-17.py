import pandas as pd
import numpy as np
def sort_lists(lists):
  array = 1 * np.array(lists)
  print(array)
  ranks = np.array(array).argsort().argsort()
  rank_list = list(ranks)
  first=rank_list.index(0)
  second=rank_list.index(1)
  third=rank_list.index(2)
  print(first,second,third)
  win_place_show=[first,second,third]
  return win_place_show
  

df = pd.read_excel("Belmont-6-18-17.xlsx")
stat_list=["Finish1","Finish2","Finish3","TRAINER%","JOCKEY%","BESTYR","TRAINER1","TRAINER2"]
df["TRAINER%"] = df["TRAINERWINS"] / df["TRAINERSTARTS"]
df["JOCKEY%"] = df["JOCKEYWINS"] / df["JOCKEYSTARTS"]
race_list=list(df["Race"])
cc=max(race_list)
print(race_list,cc," number races  ")
num_races=cc
for stat in stat_list:
    rank_list = []
    num_horses=[0]
    for races in range(0, num_races):
       best_race = [df[stat][k] for k in range(len(rank_list), len(df["Race"])) if df["Race"][k] == races + 1]
       array = [-1] * np.array(best_race)
       ranks = np.array(array).argsort().argsort()
       rank_list += list(ranks)
       num_horses.append(len(rank_list))
    df[stat+"RANK"]=rank_list
    print(num_horses)
root_mse=1.921
num_trials=100
payoff_matrix={}
exacta_list=[]
RACES=['RACE1','RACE2','RACE3','RACE4','RACE5','RACE6','RACE7','RACE8','RACE9','RACE10']
for i in range(0,20):
  exacta_list.append("Exacta"+ str(i+1))
column_list= ["TRACK","DATE","RACE","Post","PGM#","NAME", "Finish1" , "Finish2",
              "TRAINER%",
              "JOCKEY%",
              "BESTYR",
              "TRAINER1",
              "TRAINER2",
              "Finish1RANK",
              "Finish2RANK",
              "Finish3RANK",
              "TRAINER%RANK",
              "JOCKEY%RANK",
              "BESTYRRANK",
              "TRAINER1RANK",
              "TRAINER2RANK",
              "PROBABILITY"
              ]
columns_race=[]
for races in range(0,10):
    k=num_horses[races+1]-num_horses[races]
    win=np.zeros((k))# import modules

    exacta=np.zeros((k,k))
    trifecta=np.zeros((k,k,k))
    for trials in range (0,num_trials):
      begin=num_horses[races]
      end=num_horses[races+1]
      s = np.random.normal(0,root_mse,len(df["Race"]))
      df["norm"]=list(s) 
      print (df["norm"])
      df["constant"] = len(df["Race"])*[1.227]
      print(df["constant"])
      df["finish"]= df["constant"] +.343*df["BESTYRRANK"] + .437*df["TRAINER2RANK"] + df["norm"]
      df["PROBABILITY"]=len(df["Race"])*[0.]
      print (df["finish"],df["BESTYRRANK"],df["TRAINER2RANK"] )
      print(df["PROBABILITY"])
      finish_list=list(df["finish"])
      win_place_show=sort_lists(finish_list[begin:end])
      first=win_place_show[0]
      second=win_place_show[1]
      third=win_place_show[2]
      print(win)
      print(exacta)
      print(trifecta)
      win[first]+=1
      exacta[first,second]+=1
      trifecta[first,second,third]+=1
      print(win)
      print(exacta)
      print(trifecta)
    payoff_matrix[RACES[races]]=[win,exacta,trifecta]    
    print(payoff_matrix)
    list_win=list(win)
    print (list_win)
    list_probability=list(1/num_trials*win)
    exacta1_probability=list(1/num_trials*exacta[:,0])
    print(list_probability)
    print(exacta1_probability)
    matrix = {"TRACK": df["TRACK"][begin:end],
              "DATE": df["DATE"][begin:end],
              "RACE": df["Race"][begin:end],
              "Post": df["Post"][begin:end],
              "PGM#": df["PGM#"][begin:end],
              "NAME": df["NAME"][begin:end],
              "Finish1" :df["Finish1"][begin:end] ,     
              "Finish2": df["Finish2"][begin:end],
              "Finish3": df["Finish3"][begin:end],
              "TRAINER%": df["TRAINER%"][begin:end],
              "JOCKEY%": df["JOCKEY%"][begin:end],
              "BESTYR": df["BESTYR"][begin:end],
              "TRAINER1": df["TRAINER1"][begin:end],
              "TRAINER2": df["TRAINER2"][begin:end],
              "Finish1RANK": df["Finish1RANK"][begin:end],
              "Finish2RANK": df["Finish2RANK"][begin:end],
              "Finish3RANK": df["Finish3RANK"][begin:end],
              "TRAINER%RANK": df["TRAINER%RANK"][begin:end],
              "JOCKEY%RANK": df["JOCKEY%RANK"][begin:end],
              "BESTYRRANK": df["BESTYRRANK"][begin:end],
              "TRAINER1RANK": df["TRAINER1RANK"][begin:end],
              "TRAINER2RANK": df["TRAINER2RANK"][begin:end],
              "PROBABILITY":list_probability
              }
    for lll in range(0,k):
      matrix[exacta_list[lll]]= list(1/num_trials*exacta[:,lll])
    columns_race=column_list+exacta_list[0:k]
    if races==0:
       df1 = pd.DataFrame(matrix, columns=columns_race)
       print(df1)
       writer = pd.ExcelWriter("Belmont_Summary6-18-17.xlsx")
       df1.to_excel(writer, sheet_name=RACES[races])
       del columns_race [: ] 
    elif races==1:
       df2 = pd.DataFrame(matrix, columns=columns_race)
       print(df2)
       df2.to_excel(writer, sheet_name=RACES[races])
    elif races==2:
       df3 = pd.DataFrame(matrix, columns=columns_race)
       print(df3)
       df3.to_excel(writer, sheet_name=RACES[races])
       del columns_race [: ]
    elif races==3:
       df4 = pd.DataFrame(matrix, columns=columns_race)
       print(df4)
       df4.to_excel(writer, sheet_name=RACES[races])
       del columns_race [: ]
    elif races==4:
       df5 = pd.DataFrame(matrix, columns=columns_race)
       print(df5)
       df5.to_excel(writer, sheet_name=RACES[races])
       del columns_race [: ]
    elif races==5:
       df6 = pd.DataFrame(matrix, columns=columns_race)
       print(df6)
       df6.to_excel(writer, sheet_name=RACES[races])
       del columns_race [: ]
    elif races==6:
       df7 = pd.DataFrame(matrix, columns=columns_race)
       print(df7)
       df7.to_excel(writer, sheet_name=RACES[races])
       del columns_race [: ]

    elif races==7:
       df8 = pd.DataFrame(matrix, columns=columns_race)
       print(df8)
       df8.to_excel(writer, sheet_name=RACES[races])
       del columns_race [: ]

    elif races==8:
       df9 = pd.DataFrame(matrix, columns=columns_race)
       print(df9)
       df9.to_excel(writer, sheet_name=RACES[races])
       del columns_race [: ]
    elif races==9:
       df10 = pd.DataFrame(matrix, columns=columns_race)
       print(df10)
       df10.to_excel(writer, sheet_name=RACES[races])
       del columns_race [: ]
    elif races==10: 
       df11 = pd.DataFrame(matrix, columns=columns_race)
       print(df10)
       df11.to_excel(writer, sheet_name=RACES[races])
       del columns_race [: ]
writer.save()
