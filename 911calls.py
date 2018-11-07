#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 20:26:27 2018

@author: likarajo
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt #visualization library
import seaborn as sns

# ~ Read in the 911.csv file as a dataframe called df
df = pd.read_csv('911.csv') #read the data file as a dataframe
print("Data fetched successfully!")

'''
# ~ Check the info() of the df
print(df.info()) #check info of the dataframe

# ~ Check the head of df
pd.set_option('display.max_columns', None) #enable visibility of all the columns
print(df.head(5)) #check data of first 5 rows of the dataframe
'''

## ~ Top 5 zipcodes for 911 calls
#topZip = df.groupby("zip").size().sort_values(ascending=False)
topZip = df['zip'].value_counts()
#print(top5zip)
fig, ax1 = plt.subplots()
ax1=topZip.head(5).plot(kind='barh')
ax1.invert_yaxis()
ax1.set_title("Top 5 Zip Codes from which 911 calls were made")
ax1.set_ylabel("Zip Codes")
ax1.set_xlabel("No. of 911 calls")
for i in ax1.patches:
    ax1.text(i.get_width()/2, i.get_y()+i.get_height()/2, i.get_width(), \
            ha='center', va='center', color='white', weight='bold')
plt.show()

## ~ Top 5 townships for 911 calls   
#topTtwp = df.groupby("twp").size().sort_values(ascending=False)
topTwp = df['twp'].value_counts()
#print(top5twp)
fig, ax2 = plt.subplots()
ax2=topTwp.head(5).plot(kind='barh')
ax2.invert_yaxis()
ax2.set_title("Top 5 Townships from which 911 calls were made")
ax2.set_ylabel("Townships Codes")
ax2.set_xlabel("No. of 911 calls")
for j in ax2.patches:
    ax2.text(j.get_width()/2, j.get_y()+j.get_height()/2, j.get_width(), \
            ha='center', va='center', color='white', weight='bold')

plt.show()

## ~ Find the number of unique title codes
#print("Number of unique Titles =", df['title'].nunique())

## ~ Create a new column having the reason for 911 call 
#extracted from the title column
df['reason'] = df['title'].apply(lambda title: title.split(':')[0])
#print(df.head(2))

'''
# ~ Find top reason for 911 calls
reason = df.groupby("reason").size().sort_values(ascending=False)
print("Top reason for a 911 call is:", reason.head(1).index[0])
'''

## ~ Display count of 911 calls by reason
fig, ax3 = plt.subplots()
ax3=sns.countplot(y="reason", data=df, palette='magma')
ax3.set_title("Reasons of calling 911")
ax3.set_xlabel("Reason")
ax3.set_ylabel("No. of 911 calls")
for j in ax3.patches:
    ax3.text(j.get_width()/2, j.get_y()+j.get_height()/2, j.get_width(), \
            ha='center', va='center', color='white', weight='bold')
plt.show()

'''
# ~ Find data type of the objects in the timeStamp column
print(type(df['timeStamp'].iloc[0])) #select column='timeStamp' row=0
'''

## ~ Convert the timeStamp column from strings to DateTime objects
df['timeStamp'] = pd.to_datetime(df['timeStamp'])
#print(type(df['timeStamp'].iloc[0]))

'''
## for convenience convert timeStamp of first row to datetime
d = pd.to_datetime(df['timeStamp'].iloc[0]) 
print(d)

## ~ Access datetime attributes
print(d.timestamp())
print(d.year)
print(d.month)
print(d.day)
print(d.hour)
print(d.minute)
print(d.second)
print(d.microsecond)
print(d.dayofweek)
#print(d.weekday())
print(d.isoweekday())
'''

## ~ Create dictionary for Day of Week based on integer value
day_dict = {0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", \
            4:"Friday", 5:"Saturday", 6:"Sunday"}

## ~ Create new column to hold the day of week of the calls made to 911
df['dayOfWeek'] = df['timeStamp'].apply(lambda x: x.dayofweek).map(day_dict)
#print(df['dayOfWeek'].head(1))

## ~ Plot Count of 911 calls w.r.t reason and day of week
fig, ax4 = plt.subplots()
ax4 = sns.countplot(x='dayOfWeek', hue='reason', data=df, palette='rainbow')
ax4.set_title("911 calls per week day")
ax4.set_xlabel("Day of Week")
plt.xticks(rotation=45)
ax4.set_ylabel("No. of 911 calls")
for i in ax4.patches:
    ax4.text(i.get_x()+i.get_width()/2, i.get_height()/2, i.get_height(), \
            ha='center', va='center', color='black', rotation='vertical')
plt.show()

## ~ Create dictionary for Month based on integer value
month_dict = {1:"January", 2:"February", 3:"March", 4:"April", \
              5:"May", 6:"June", 7:"July", 8:"August", \
              9:"September", 10:"October", 11:"November", 12:"December"}

## ~ Create new column to hold the month of the calls made to 911
df['month'] = df['timeStamp'].apply(lambda x: x.month).map(month_dict)
#print(df['month'].head(1))

## ~ Plot Count of 911 calls w.r.t reason and month
fig, ax5 = plt.subplots()
ax5 = sns.countplot(x='month', hue='reason', data=df, palette='rainbow')
ax5.set_title("911 calls per month")
ax5.set_xlabel("Month")
plt.xticks(rotation=45)
ax5.set_ylabel("No. of 911 calls")
for i in ax5.patches:
    ax5.text(i.get_x()+i.get_width()/2, i.get_height()/2, i.get_height(), \
            ha='center', va='center', color='black', rotation='vertical')
plt.show()

## ~ Plot 911 calls per month
countByMonth = df.groupby('month').count()['twp']
fig, ax6 = plt.subplots()
ax6 = countByMonth.plot()
ax6.set_title("911 calls trend based on months")
#sns.lmplot(x='month', y='twp', data=countByMonth.reset_index())
plt.xticks(rotation='vertical')
plt.show()

## ~ Create column date extracting date from timeStamp column
df['date'] = df['timeStamp'].apply(lambda x: x.date())
# print(df['date'].head(2))

## ~ Plot 911 calls per date
countByDate = df.groupby('date').count()['twp']
fig, ax7 = plt.subplots()
ax7 = countByDate.plot()
ax7.set_title("911 calls trend based on dates")
#sns.lmplot(x='date', y='twp', data=countByDate.reset_index())
plt.xticks(rotation='vertical')
plt.show()

## ~ Plot the count of 911 calls per date based on reason
df[df['reason']=='Fire'].groupby('date').count()['twp'].plot()
df[df['reason']=='Traffic'].groupby('date').count()['twp'].plot()
df[df['reason']=='EMS'].groupby('date').count()['twp'].plot()
plt.xticks(rotation=30)
plt.title("911 calls trend based on date by reason")
#plt.legend()
plt.show()

## ~ Create new column to hold the day of week of the calls made to 911
df['hour'] = df['timeStamp'].apply(lambda x: x.hour)
#print(df['dayOfWeek'].head(1))

## ~ restructure the dataframe col=hour and index=dayOfWeek
dayHour = df.groupby(by=['dayOfWeek','hour']).count()['reason'].unstack()
#print(dayHour)

## ~ Create heatmap for no. of 911 calls based on the day of week at apecific hour
plt.figure(figsize=(16,5))
sns.heatmap(dayHour, cmap='magma')
plt.title("911 call count at hourly and day of week basis")
plt.show()

## ~ restructure the dataframe col=month and index=dayOfWeek, and create heatmap
dayHour = df.groupby(by=['month','hour']).count()['reason'].unstack()
#print(dayHour)
plt.figure(figsize=(16,5))
sns.heatmap(dayHour, cmap='rainbow')
plt.title("911 call count at hourly and monthly basis")
plt.show()














