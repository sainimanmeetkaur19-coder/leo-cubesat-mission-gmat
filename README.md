# 500 km Sun-Synchronous CubeSat Orbit: Mission Analysis in GMAT

![Ground track](images\ground_track.png.png)

## Objective
Design and analyse a low Earth orbit for a 3U CubeSat (4 kg) in NASA's GMAT.
The study checks that the orbit is sun-synchronous, how much time the
satellite spends in Earth's shadow, and how long it stays in orbit
before atmospheric drag brings it down.

## Method
- Tool: GMAT R2025a, with Python (pandas, matplotlib) for plots
- Orbit: 500 km altitude, inclination 97.4 deg, eccentricity 0.001, RAAN 79 deg
- Spacecraft: mass 4 kg, drag area 0.03 m2, Cd 2.2, Cr 1.3
- Force model: Earth gravity JGM-2 (8x8), JacchiaRoberts drag,
  solar radiation pressure, Sun and Moon as point masses
- Propagator: RungeKutta89, 30-day run

## Results
| Check | Result |
|---|---|
| RAAN drift | [X] deg/day (expected about 0.985) |
| SMA loss in 30 days | [X] km |
| Eclipse per orbit | [X] min ([X]% sunlit) |

Orbital lifetime from 120 km re-entry:

| Altitude | Quiet sun (F10.7 = 100) | Active sun (F10.7 = 200) |
|---|---|---|
| 400 km | [X] | [X] |
| 500 km | [X] | [X] |
| 600 km | [X] | [X] |

![RAAN and SMA](results/orbit_check.png)

The orbit is sun-synchronous because Earth's equatorial bulge slowly turns the orbit plane at [X] deg/day in the simulation. This matches the Earth's motion around the Sun (about 0.985 deg/day), so the satellite crosses each latitude at the same local solar time every day and gets steady lighting, which is useful for imaging. Atmospheric drag slowly lowers the orbit, and since the air thins out quickly with height, a satellite at 400 km re-enters much sooner than one at 600 km. Strong solar activity heats and expands the upper atmosphere, which increases drag and shortens the lifetime further, so lifetime is best given as a range.

## How to reproduce
1. Open `gmat/flagship_500km.script` in GMAT and press Run
2. Copy the report files from GMAT's output folder into `results/`
3. `pip install pandas numpy matplotlib`
4. `python src/plot_results.py`

## Limitations
- Constant drag area and Cd (no attitude model)
- Constant solar flux values, real solar activity varies
- Lifetime depends strongly on solar activity, so results are a range

## Files
- `gmat/`: GMAT script
- `src/plot_results.py`: analysis and plots
- `results/`: reports and plots
- `docs/report.pdf`: full report

## Author
Manmeet Saini, B.Tech Aerospace Engineering, MIT ADT University
www.linkedin.com/in/manmeet-saini-1916jan