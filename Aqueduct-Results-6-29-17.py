# import modules
import pandas as pd
import numpy as np
df = pd.read_excel("Belmont-7-07-17.xlsx")
stat_list=["Finish1","Finish2","Finish3","TRAINER%","JOCKEY%","BESTYR","TRAINER1","TRAINER2","FINISHED"]
df["TRAINER%"] = df["TRAINERWINS"] / df["TRAINERSTARTS"]
df["JOCKEY%"] = df["JOCKEYWINS"] / df["JOCKEYSTARTS"]
print(df["TRAINER%"])
print(df["JOCKEY%"])
print(df["NAME"].index.values)
race_list=list(df["Race"])
cc=max(race_list)
print(race_list,cc," number races  ")
num_races=cc
num_horses=[0]
scratch_list =[]
scratch_list_name=[]
rank_list = []
for races in range(0, num_races):
    horses=[k+1 for k in range(0,len(df["Race"])) if df["Race"][k]==races +1]
    maximum= max(horses)
    num_horses.append(maximum)
    print(num_horses)
       
df1 =  pd.read_excel("Belmont-Results-7-07-17.xlsx")
df["FINISHED"]=len(df["Race"])*[999]
df["ODDS"] = len(df["Race"])*[999.0]
df["NAME"]=[x.lower() for x in df["NAME"]]
df1["NAME"]= [x.lower() for x in df1["NAME"]]
for races in range(0,num_races):
  horse_names=[df1["NAME"][lk]  for lk in df1["NAME"].index.values if df1["RACE"][lk]== races +1]
  print(horse_names)
  print(num_horses)
  for horsespp in range(num_horses[races],num_horses[races+1]):
    kk=horsespp
    print(kk)
    if df["NAME"][horsespp] in horse_names:
      print(df["NAME"][horsespp])
      print(df1["NAME"])
      print(df["NAME"])
      print(df1["FINISH"])
      print(df["FINISHED"])
      kkk=list(df1["NAME"]).index(df["NAME"][horsespp])
      print (kkk,df1["FINISH"][kkk],df["FINISHED"][horsespp])
      df.loc[horsespp,"FINISHED"]=df1.loc[kkk,'FINISH']
       #df["FINISHED"][horsespp]=df1["FINISH"][kkk]
      df.loc[horsespp,"ODDS"]= df1.loc[kkk,"ODDS"]
       #df["ODDS"][horsespp]=df1["ODDS"][kkk]
      print(df["NAME"][horsespp],df["FINISHED"][horsespp],df1["FINISH"][kkk])
    else:
      print("scratch", df["NAME"][horsespp],"row",horsespp)
      df["FINISHED"][horsespp]="scratched"
      scratch_list.append(horsespp)
      scratch_list_name.append(df["NAME"][horsespp])
print(df)
df=df.drop(df.index[scratch_list])
print(df)
num_horses_new=[0]
for races in range(0, num_races):
    horses_new=[k+1 for k in range(0,len(df["Race"])) if df1["RACE"][k]==races +1]
    maximum= max(horses_new)
    num_horses_new.append(maximum)
    print(num_horses_new)      

print(scratch_list)
print(scratch_list_name)
for stat in stat_list:
    df[stat+"zscore"]=len(df["Race"])*[999]
for stat in stat_list:
    rank_list = []
    stat_zscore=stat +"zscore"
    for races in range(0, num_races):
      beg= num_horses_new[races]
      end=num_horses_new[races+1]
      # best_race = [df[stat][k] for k in df["NAME"].index.values if df["Race"][k] == races + 1]
      best_race=df[stat][beg:end]
      array = [-1] * np.array(best_race)
      ranks = np.array(array).argsort().argsort()
      rank_list += list(ranks)
      print(best_race)
      print(ranks)
      df[stat_zscore][beg:end] = (df[stat][beg:end] -df[stat][beg:end].mean())/df[stat][beg:end].std(ddof=1)
    print(df[stat_zscore])
    print(rank_list)
    df[stat+"RANK"]=rank_list 
    stat_zscore=stat +"zscore"
    df[stat_zscore][beg:end] = (df[stat][beg:end] -df[stat][beg:end].mean())/df[stat][beg:end].std(ddof=1)
    print(df[stat_zscore])
    print(df[stat+"RANK"])
matrix = {"TRACK": df["TRACK"],
          "DATE": df["DATE"],
          "RACE": df["Race"],
          "Post": df["Post"],
          "PGM#": df["PGM#"],
          "NAME": df["NAME"],         
          "Finish1": df["Finish1"],
          "Finish2": df["Finish2"],
          "Finish3": df["Finish3"],
          "TRAINER%": df["TRAINER%"],
          "JOCKEY%": df["JOCKEY%"],
          "BESTYR": df["BESTYR"],
          "TRAINER1": df["TRAINER1"],
          "TRAINER2": df["TRAINER2"],
          "Finish1RANK": df["Finish1RANK"],
          "Finish2RANK": df["Finish2RANK"],
          "Finish3RANK": df["Finish3RANK"],
          "TRAINER%RANK": df["TRAINER%RANK"],
          "JOCKEY%RANK": df["JOCKEY%RANK"],
          "BESTYRRANK": df["BESTYRRANK"],
          "TRAINER1RANK": df["TRAINER1RANK"],
          "TRAINER2RANK": df["TRAINER2RANK"],
          "FINISHED":df["FINISHED"],
          "Finish1zscore": df["Finish1zscore"],
          "Finish2zscore": df["Finish2zscore"],
          "Finish3zscore": df["Finish3zscore"],
          "TRAINER%zscore": df["TRAINER%zscore"],
          "JOCKEY%zscore": df["JOCKEY%zscore"],
          "BESTYRzscore": df["BESTYRzscore"],
          "TRAINER1zscore": df["TRAINER1zscore"],
          "TRAINER2zscore": df["TRAINER2zscore"],
          "FINISHEDzscore":df["FINISHEDzscore"],
          "ODDS":df["ODDS"]}
matrix
columns_list=["TRACK",
          "DATE",
          "RACE",
          "Post",
          "PGM#",
          "NAME",         
          "Finish1",
          "Finish2",
          "Finish3",
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
          "FINISHED",
          "Finish1zscore",
          "Finish2zscore",
          "Finish3zscore",
          "TRAINER%zscore",
          "JOCKEY%zscore",
          "BESTYRzscore",
          "TRAINER1zscore",
          "TRAINER2zscore",
          "FINISHEDzscore",
          "ODDS"]
df = pd.DataFrame(matrix, columns=columns_list)
df
writer = pd.ExcelWriter("Belmont_Summary-7-07-17.xlsx")
df.to_excel(writer, sheet_name='Sheet1')
writer.save()
