import pandas as pd, numpy as np, matplotlib.pyplot as plt

df = pd.read_csv('results/orbit_report.txt', sep=r'\s+')
df.columns = ['days','alt','raan','sma','inc','ecc']

d = df[df.days < 30]                          # full days only
dd = d.groupby(d.days.astype(int)).mean()     # one row per day
t = dd.index + 0.5                            # middle of each day

raan_rate, _ = np.polyfit(t, dd.raan, 1)
sma_rate, _ = np.polyfit(t, dd.sma, 1)

print('RAAN drift from daily means (deg/day):', round(raan_rate, 4))   # ideal sun-sync: about 0.985
print('RAAN at end:', round(df.raan.iloc[-1], 2))
print('SMA change per day (km):', round(sma_rate, 3), '| over 30 days:', round(30*sma_rate, 2))

fig, ax = plt.subplots(1, 2, figsize=(11, 4))
ax[0].plot(df.days, df.raan, lw=0.8, label='raw')
ax[0].plot(t, dd.raan, 'o', ms=3, label='daily mean')
ax[0].set_title('RAAN vs time'); ax[0].set_xlabel('Days'); ax[0].set_ylabel('RAAN (deg)'); ax[0].legend()
ax[1].plot(t, dd.sma, marker='o')
ax[1].set_title('Daily mean SMA'); ax[1].set_xlabel('Day'); ax[1].set_ylabel('SMA (km)')
plt.tight_layout(); plt.savefig('results/orbit_check.png', dpi=200)