
# coding: utf-8

# In[2]:


import csv
f=open("guns.csv","r")
data=list(csv.reader(f))
headers=data[0]
data=data[1:]
print(headers)
print(data[:5])


# In[19]:


year_counts = {}
for row in data:
    years=row[1]
    if years in year_counts:
        year_counts[years]+=1
    else:
        year_counts[years]=1
print(year_counts)


# In[5]:


import datetime
dates=[datetime.datetime(year=int(row[1]),month=int(row[2]), day=1) for row in data[:5]]
print(dates)


# In[6]:


date_counts={}
for row in dates:
    if row in date_counts:
        date_counts[row]+=1
    else:
        date_counts[row]=1
print(date_counts)
    


# In[7]:


sex_counts={}
for row in data[:5]:
    sex=row[5]
    if sex in sex_counts:
        sex_counts[sex]+=1
    else:
        sex_counts[sex]=1
print(sex_counts)


# In[10]:


race_counts={}
for row in data:
    race=row[7]
    if race in race_counts:
        race_counts[race]+=1
    else:
        race_counts[race]=1
print(race_counts)


# In[9]:


g=open("census.csv","r")
census=list(csv.reader(g))
print(census)


# In[18]:


mapping = {
    "Asian/Pacific Islander": 15159516 + 674625,
    "Native American/Native Alaskan": 3739506,
    "Black": 40250635,
    "Hispanic": 44618105,
    "White": 197318956
}
race_per_hundredk={}
for race,number in race_counts.items():
    race_per_hundredk[race]=(number/mapping[race])*100000
print(race_per_hundredk)


# In[36]:


intents=[]
for row in data[:25]:
    intent=row[3]
    intents.append(row[3])
homicide_race_counts={}
races=[row[7] for row in data[:25]]
for i,race in enumerate(races):
    if race not in homicide_race_counts:
        homicide_race_counts[race] = 0
    if intents[i] == "Homicide":
        homicide_race_counts[race] += 1

race_per_hundredk = {}
for k,v in homicide_race_counts.items():
    race_per_hundredk[k] = (v / mapping[k]) * 100000

print(races)

print(intents)
race_per_hundredk


# In[42]:


months=[row[2] for row in data]
intents = [row[3] for row in data]
homicide_month_counts={}
for i,month in enumerate(months):
    if month not in homicide_month_counts:
        homicide_month_counts[month]=0
    if intents[i] == "Homicide":
        homicide_month_counts[month]+=1
homicide_month_counts

