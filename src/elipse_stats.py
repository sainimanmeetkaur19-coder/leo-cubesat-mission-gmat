import re, pandas as pd
pat = re.compile(r'(\d{2} \w{3} \d{4} [\d:.]+)\s+(\d{2} \w{3} \d{4} [\d:.]+)\s+([\d.]+)\s+Earth\s+(\w+)\s+(\d+)\s+([\d.]+)')
rows = []
with open('results/EclipseLocator1.txt') as f:
    for line in f:
        m = pat.search(line)
        if m:
            rows.append(dict(start=pd.to_datetime(m.group(1)), event=int(m.group(5)), total=float(m.group(6))))
ev = pd.DataFrame(rows)
orbits = ev.groupby('event').agg(start=('start', 'min'), total=('total', 'first'))
orbits = orbits.iloc[1:-1]                  # drop partial first and last events
period = orbits.start.diff().dt.total_seconds().median()
print('Mean eclipse per orbit (min):', round(orbits.total.mean()/60, 2))
print('Shortest / longest (min):', round(orbits.total.min()/60, 2), round(orbits.total.max()/60, 2))
print('Orbit period (min):', round(period/60, 2))
print('Sunlit fraction (%):', round(100*(1 - orbits.total.mean()/period), 1))