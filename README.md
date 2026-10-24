# 500 km Sun-Synchronous CubeSat Orbit: Mission Analysis in GMAT

![Ground track](images/ground_track.png)

## Objective
Design and analyse a low Earth orbit for a 3U CubeSat (4 kg) in NASA's GMAT.
The study checks that the orbit is sun-synchronous, how much time the
satellite spends in Earth's shadow, and how long it stays in orbit
before atmospheric drag brings it down.

## Method
- Tools: GMAT R2025a, Python (pandas, numpy, matplotlib)
- Orbit: 500 km altitude, inclination 97.4 deg, eccentricity 0.001, RAAN 79 deg
- Spacecraft: mass 4 kg, drag area 0.03 m2, Cd 2.2, Cr 1.3
- Force model: Earth gravity JGM-2 (8x8), JacchiaRoberts drag,
  solar radiation pressure, Sun and Moon as point masses
- Propagator: RungeKutta89, 30-day run

## Results
| Check | Result |
|---|---|
| RAAN drift | 0.969 deg/day (ideal sun-synchronous: 0.986) |
| SMA loss in 30 days | 1.85 km |
| Eclipse per orbit | 34.4 min (range 34.0 to 34.6) |
| Orbit period | 94.5 min |
| Sunlit fraction | 63.6% |

Orbital lifetime (time to reach 120 km altitude):

| Altitude | Quiet sun (F10.7 = 100) | Active sun (F10.7 = 200) |
|---|---|---|
| 400 km | [X] | [X] |
| 500 km | [X] | [X] |
| 600 km | [X] | [X] |

![RAAN and SMA](results/orbit_check.png)

Earth's equatorial bulge turns the orbit plane at 0.969 deg/day in the
simulation, close to the 0.986 deg/day needed to follow the Sun (about 1.7%
lower), so the satellite crosses each latitude at nearly the same local solar
time every day. The satellite spends about 34 minutes of each 94.5-minute
orbit in Earth's shadow, so it is sunlit about 64% of the time, which sets the
solar power budget. Atmospheric drag slowly lowers the orbit, and since the air
thins out quickly with height, a satellite at 400 km re-enters much sooner than
one at 600 km. Strong solar activity heats and expands the upper atmosphere,
which increases drag and shortens the lifetime further, so lifetime is best
given as a range.

## How to reproduce
1. Open `gmat/flagship_500km.script` in GMAT and press Run
2. Copy the report files from GMAT's output folder into `results/`
3. `pip install pandas numpy matplotlib`
4. `python src/plot_results.py` and `python src/eclipse_stats.py`

## Limitations
- Constant drag area and Cd (no attitude model)
- Constant solar flux values, real solar activity varies
- RAAN drift is about 1.7% below the ideal value; the cause was not isolated
- Lifetime depends strongly on solar activity, so results are a range

## Files
- `gmat/`: GMAT script
- `src/plot_results.py`: RAAN and SMA analysis, plots
- `src/eclipse_stats.py`: eclipse statistics
- `results/`: reports and plots
- `images/`: GMAT screenshots
- `docs/report.pdf`: full report

## Author
Manmeet Saini, B.Tech Aerospace Engineering, MIT ADT University
www.linkedin.com/in/manmeet-saini-1916jan