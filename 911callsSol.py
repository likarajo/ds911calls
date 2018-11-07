import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

df = pd.read_csv('911.csv')
#df.info()
#df.head(3)
#df['zip'].value_counts().head(5)
#df['twp'].value_counts().head(5)
#df['title'].nunique()

df['Reason'] = df['title'].apply(lambda title: title.split(':')[0])
#df['Reason'].value_counts()

#sns.countplot(x='Reason', data=df, palette='viridis')

print(type(df['timeStamp'].iloc[0]))
#df['timeStamp'] = pd.to_datetime(df['timeStamp'])

#`df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)
#df['Month'] = df['timeStamp'].apply(lambda time: time.month)
#df['Day of Week'] = df['timeStamp'].apply(lambda time: time.dayofweek)

#dmap = {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'}
#df['Day of Week'] = df['Day of Week'].map(dmap)
#sns.countplot(x='Day of Week', data=df, hue='Reason', palette='viridis')

# It is missing some months! 9,10, and 11 are not there.
#byMonth = df.groupby('Month').count()
#byMonth.head()
# Could be any column
#byMonth['twp'].plot()

#sns.lmplot(x='Month', y='twp', data=byMonth.reset_index())
#df['Date'] = df['timeStamp'].apply(lambda t: t.date())

# df.groupby('Date').count()['twp'].plot()
# plt.tight_layout()
#df[df['Reason'] == 'Traffic'].groupby('Date').count()['twp'].plot()
# plt.title('Traffic')
# plt.tight_layout()

#df[df['Reason'] == 'Fire'].groupby('Date').count()['twp'].plot()
# plt.title('Fire')
# plt.tight_layout()

#df[df['Reason'] == 'EMS'].groupby('Date').count()['twp'].plot()
# plt.title('EMS')
# plt.tight_layout()

#dayHour = df.groupby(by=['Day of Week', 'Hour']).count()['Reason'].unstack()
# dayHour.head()


#plt.figure(figsize=(12, 6))
#sns.heatmap(dayHour, cmap='viridis')
