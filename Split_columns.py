import pandas as pd
df = pd.read_csv(r"C:\Users\mwalker\Desktop\CS_HR_DASH\Capstone_HR_Dashboard\All Certs_Clean.csv")
p1 = {}
p2 = {}

for i in range(len(df)):
    if ';' in df['Score and Date'].loc[i]:
        p1[df['id'].loc[i]] = df['Score and Date'].loc[i].split(';')[0]
        p2[df['id'].loc[i]] = df['Score and Date'].loc[i].split(';')[1]

df['Score'] = df['id'].map(p1)
df['Date'] = df['id'].map(p2)

df.drop('Score and Date', axis=1)

df.to_csv('new_file.csv', inplace=True)