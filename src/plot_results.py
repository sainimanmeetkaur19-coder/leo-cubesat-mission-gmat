import pandas as pd, numpy as np, matplotlib.pyplot as plt
df = pd.read_csv('results/orbit_report.txt', sep=r'\s+')
df.columns = ['days','alt','raan','sma','inc','ecc']

slope, _ = np.polyfit(df.days, df.raan, 1)
print('RAAN drift (deg/day):', round(slope, 4))      # expect about 0.985
print('RAAN at end:', round(df.raan.iloc[-1], 2))    # expect about 108.6

daily = df.groupby(df.days.astype(int)).sma.mean()   # one value per day
print('SMA lost in 30 days (km):', round(daily.iloc[0] - daily.iloc[-1], 2))

fig, ax = plt.subplots(1, 2, figsize=(11, 4))
ax[0].plot(df.days, df.raan, lw=0.8); ax[0].set_title('RAAN vs time')
ax[0].set_xlabel('Days'); ax[0].set_ylabel('RAAN (deg)')
ax[1].plot(daily.index, daily.values, marker='o'); ax[1].set_title('Daily mean SMA')
ax[1].set_xlabel('Day'); ax[1].set_ylabel('SMA (km)')
plt.tight_layout(); plt.savefig('results/orbit_check.png', dpi=200)