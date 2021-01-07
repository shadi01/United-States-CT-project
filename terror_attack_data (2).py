#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
import chart_studio.plotly as py
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import plotly.graph_objects as go 
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.figure_factory as ff


# In[2]:


df = pd.read_excel(r'C:\Users\shiwi\OneDrive\Desktop\terrorist_data.xlsx')


# In[82]:


df.head()


# In[4]:


df.rename(columns={'iyear':'Year','imonth':'Month','iday':'Day','country_txt':'Country','region_txt':'Region','attacktype1_txt':'AttackType','target1':'Target','nkill':'Killed','nwound':'Wounded','summary':'Summary','gname':'Group','targtype1_txt':'Target_type','weaptype1_txt':'Weapon_type','motive':'Motive'},inplace=True)
df=df[['Year','Month','Day','Country','Region','city','latitude','longitude','AttackType','Killed','Wounded','Target','Summary','Group','Target_type','Weapon_type','Motive']]
df['Casualities']=df['Killed']+df['Wounded']
df=df


# In[5]:


df.info()


# In[6]:


# Filter data to terrorist attacks in the U.S. only
df_us = df[df['Country'] == 'United States']


# In[7]:


# Top 5 terrorist groups in the U.S. based on number of attacks
df_us['Group'].value_counts().head(5)


# In[111]:


# Plot shwoing top 5 terrorist groups by attack count (1970-2018)
ax = sns.barplot(df_us['Group'].value_counts().head(5).index, y = df_us['Group'].value_counts().head(5))

# Format plot
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.1f'), 
                   (p.get_x() + p.get_width() / 2., p.get_height()), 
                   ha = 'center', va = 'center', 
                   size=15,
                   xytext = (0, 10), 
                   textcoords = 'offset points')
    sns.set(rc={'figure.figsize':(20,10)})

    plt.tight_layout()
    
def change_width(ax, new_value) :
    for patch in ax.patches :
        current_width = patch.get_width()
        diff = current_width - new_value

        # we change the bar width
        patch.set_width(new_value)

        # we recenter the bar
        patch.set_x(patch.get_x() + diff * .5)

change_width(ax, .35)

# Set labels
ax.set(xlabel="Terrorist Groups", ylabel = "Number of Terrorist Attacks", title = 'Top five Terrorist Groups in the United States by attacks (1970-2017)')

plt.rcParams["axes.labelsize"] = 15

for ax in plt.gcf().axes:
    l = ax.get_title()
    ax.set_title(l, fontsize=20)

plt.show()


# In[37]:


# Attacks caused by terrorists with unknown group affiliation
df_us_unk = df_us[df_us['Group'] == 'Unknown']

# Plot showing activity of terrorists with unknown group affiliation from 1970-2017
ax = sns.countplot(x = df_us_unk['Year'], data = df_us_unk)
plt.tight_layout()

#Format plot
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.1f'), 
                   (p.get_x() + p.get_width() / 2., p.get_height()), 
                   ha = 'center', va = 'center', 
                   size=10,
                   xytext = (0, 10), 
                   textcoords = 'offset points')
sns.set(rc={'figure.figsize':(20,10)})

# Set labels
ax.set(xlabel="Group: Unkown Affiliation", ylabel = "Number of Terrorist Attacks", title = 'Number of attacks caused by terrorists with unknown group affiliation (1970-2017)')
plt.rcParams["axes.labelsize"] = 15

for ax in plt.gcf().axes:
    l = ax.get_title()
    ax.set_title(l, fontsize=20)

plt.show()


# In[41]:


# Attacks caused by Anti-Abortion extremists (AAE)
df_us_AAE = df_us[df_us['Group'] == 'Anti-Abortion extremists']

# Plot showing activity of anti-abortion extremists from 1970-2017
ax = sns.countplot(x = df_us_AAE['Year'], data = df_us_AAE)

# Format plot
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.1f'), 
                   (p.get_x() + p.get_width() / 2., p.get_height()), 
                   ha = 'center', va = 'center', 
                   size=10,
                   xytext = (0, 10), 
                   textcoords = 'offset points')
sns.set(rc={'figure.figsize':(20,10)})
plt.tight_layout()

# Set labels
ax.set(xlabel="Group: Anti-Abortion extremists", ylabel = "Number of Terrorist Attacks", title = 'Number of attacks caused by Anti-Abortion extremists (1970-2017)')
plt.rcParams["axes.labelsize"] = 15
for ax in plt.gcf().axes:
    l = ax.get_title()
    ax.set_title(l, fontsize=20)
    
plt.show()


# In[83]:


# Terrorisy attacks caused by Left-Wing Militants
df_us_lwe = df_us[df_us['Group'] == 'Left-Wing Militants']

# Plot showing attacks by Left-Wing Militants (1970-2017)
ax = sns.countplot(x = df_us_lwe['Year'], data = df_us_lwe)

# Format plot
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.1f'), 
                   (p.get_x() + p.get_width() / 2., p.get_height()), 
                   ha = 'center', va = 'center', 
                   size=20,
                   xytext = (0, 10), 
                   textcoords = 'offset points')
    plt.tight_layout()
    
# Set labels
ax.set(xlabel="Group: Left-Wing Militants", ylabel = "Number of Terrorist Attacks", title = 'Attack activity by Left-Wing Militants (1970-2017)')
plt.rcParams["axes.labelsize"] = 15
for ax in plt.gcf().axes:
    l = ax.get_title()
    ax.set_title(l, fontsize=20)
    
def change_width(ax, new_value) :
    for patch in ax.patches :
        current_width = patch.get_width()
        diff = current_width - new_value

        # we change the bar width
        patch.set_width(new_value)

        # we recenter the bar
        patch.set_x(patch.get_x() + diff * .5)

change_width(ax, .35)
    
plt.xticks(fontsize= 20) 
plt.yticks(fontsize= 20) 

plt.show()


# In[80]:


# Attacks caused by FALN
df_us_FALN = df_us[df_us['Group'] == 'Fuerzas Armadas de Liberacion Nacional (FALN)']

# Plot showing attacks by FALN (1970-2017)
ax = sns.countplot(x = df_us_FALN['Year'], data = df_us_FALN)

# Format plot
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.1f'), 
                   (p.get_x() + p.get_width() / 2., p.get_height()), 
                   ha = 'center', va = 'center', 
                   size=20,
                   xytext = (0, 10), 
                   textcoords = 'offset points')
sns.set(rc={'figure.figsize':(20,10)})
plt.tight_layout()


# Set labels
ax.set(xlabel="Group: FALN (Fuerzas Armadas de Liberacion Nacional)", ylabel = "Number of Terrorist Attacks", title = 'Attack activity by FALN (1970-2017)')
plt.rcParams["axes.labelsize"] = 20
for ax in plt.gcf().axes:
    l = ax.get_title()
    ax.set_title(l, fontsize=20)
    
plt.xticks(fontsize= 20) 
plt.yticks(fontsize= 20) 


plt.show()


# In[71]:


# Attacks by White extremists
df_us_we = df_us[df_us['Group'] == 'White extremists']

# Plot showing attacks by White extremists (1970-2018)
ax = sns.countplot(x = df_us_we['Year'], data = df_us_we)

# Format plot
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.1f'), 
                   (p.get_x() + p.get_width() / 2., p.get_height()), 
                   ha = 'center', va = 'center', 
                   size=15,
                   xytext = (0, 10), 
                   textcoords = 'offset points')
    plt.tight_layout()
    
# Set labels
ax.set(xlabel = "Group: White extremists", ylabel = "Number of Terrorist Attacks", title = 'Attack activity by White extremists (1970-2017)')
plt.rcParams["axes.labelsize"] = 20
for ax in plt.gcf().axes:
    l = ax.get_title()
    ax.set_title(l, fontsize=20)
        
plt.xticks(fontsize= 20) 
plt.yticks(fontsize= 20) 

plt.show()


# In[78]:


# Attacks by White extremists
df_us_we = df_us[df_us['Group'] == 'White extremists']

# Plot showing attacks by White extremists (1970-2018)
ax = sns.countplot(x = df_us_we['Year'], data = df_us_we)

# Format plot
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.1f'), 
                   (p.get_x() + p.get_width() / 2., p.get_height()), 
                   ha = 'center', va = 'center', 
                   size=20,
                   xytext = (0, 10), 
                   textcoords = 'offset points')
    plt.tight_layout()
    sns.set(rc={'figure.figsize':(20,10)})
    
# Set labels
ax.set(xlabel="Group: White extremists", ylabel = "Number of Terrorist Attacks", title = 'Attack activity by White extremists (1970-2017)')
plt.rcParams["axes.labelsize"] = 20
for ax in plt.gcf().axes:
    l = ax.get_title()
    ax.set_title(l, fontsize=20)
    
plt.xticks(fontsize= 20) 
plt.yticks(fontsize= 20) 


plt.show()


# In[49]:


df_us['text'] = df_us['city'] + ' (' + df['Year'].astype(str) + ')' +'<br>Group: ' + df_us['Group'] + '<br>Casualities: ' + (df_us['Casualities']).astype(str) +'<br>Attack Type: ' + df_us['AttackType'] 
colors = ["royalblue","crimson","lightseagreen","orange","lightgrey"]
cities = []
scale = 5000

fig = go.Figure()


fig.add_trace(go.Scattergeo(
        locationmode = 'USA-states',
        lon = df_us['longitude'],
        lat = df_us['latitude'],
        text = df_us['text'],
        marker = dict(
            size = 3,
            line_color='rgb(40,40,40)',
            line_width=0.5,
            sizemode = 'area'
        )
        ))

fig.update_layout(
        title_text = 'U.S. Terrorist Attack Map<br>(1970 - 2017)',
        showlegend = True,
        geo = dict(
            scope = 'usa',
            landcolor = 'rgb(217, 217, 217)',
        )
    )

fig.show()


# In[126]:


# Plot shwoing top 5 terrorist groups by attack count (1970-2018)
ax = sns.barplot(x = df_us['Weapon_type'].value_counts().head(5).index, y = df_us['Weapon_type'].value_counts().head(5))

# Format plot
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.1f'), 
                   (p.get_x() + p.get_width() / 2., p.get_height()), 
                   ha = 'center', va = 'center', 
                   size=12,
                   xytext = (0, 5), 
                   textcoords = 'offset points')
    sns.set(rc={'figure.figsize':(10,5)})

    plt.tight_layout()
    
def change_width(ax, new_value) :
    for patch in ax.patches :
        current_width = patch.get_width()
        diff = current_width - new_value

        # we change the bar width
        patch.set_width(new_value)

        # we recenter the bar
        patch.set_x(patch.get_x() + diff * .5)

change_width(ax, .35)

# Set labels
ax.set(ylabel="Amount of Times used", xlabel = "Weapon Types", title = 'Top 5 weapon types used (1970-2017)')
plt.rcParams["axes.labelsize"] = 12
for ax in plt.gcf().axes:
        l = ax.get_title()
        ax.set_title(l, fontsize=12)

plt.show()


# In[117]:


# Plot shwoing top 5 terrorist groups by attack count (1970-2018)
ax = sns.barplot(x = df_us['Target_type'].value_counts().head(5).index, y = df_us['Target_type'].value_counts().head(5))

# Format plot
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.1f'), 
                   (p.get_x() + p.get_width() / 2., p.get_height()), 
                   ha = 'center', va = 'center', 
                   size=12,
                   xytext = (0, 6), 
                   textcoords = 'offset points')
    sns.set(rc={'figure.figsize':(10,5)})

    plt.tight_layout()
    
def change_width(ax, new_value) :
    for patch in ax.patches :
        current_width = patch.get_width()
        diff = current_width - new_value

        # we change the bar width
        patch.set_width(new_value)

        # we recenter the bar
        patch.set_x(patch.get_x() + diff * .5)

change_width(ax, .35)

# Set labels
ax.set(ylabel="Amount of Attacked", xlabel = "Targets", title = 'Top 5 targets of terrosit attacks within the U.S. (1970-2017)')
plt.rcParams["axes.labelsize"] = 12
for ax in plt.gcf().axes:
        l = ax.get_title()
        ax.set_title(l, fontsize=12)

plt.show()


# In[ ]:




