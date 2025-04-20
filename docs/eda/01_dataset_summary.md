# 🧾 Dataset Summary — Formula 1 (1950–2020)

This document summarizes the structure and contents of the Kaggle dataset used in this project.

## 📁 Source

**Dataset:** [Formula 1 World Championship (1950–2020)](https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020)  
**Author:** Rohan Rao  
**License:** Open Data — for research and educational use

---

## 📂 Tables Overview

| Table Name           | Rows    | Columns | Description |
|----------------------|---------|---------|-------------|
| `circuits`           | 77      | 9       | Info about circuits (name, location, country, lat/lon, etc.) |
| `constructor_results`| 12,625  | 5       | Performance of each constructor per race |
| `constructor_standings`| 13,391 | 7      | Cumulative constructor points and rank per season |
| `constructors`       | 212     | 5       | Constructor metadata (name, nationality, etc.) |
| `driver_standings`   | 34,863  | 7       | Standings of each driver per race |
| `drivers`            | 861     | 9       | Driver info (name, code, nationality, birthdate) |
| `lap_times`          | 589,081 | 6       | Per-lap performance for each driver |
| `pit_stops`          | 11,371  | 7       | Pit stop times per race/driver |
| `qualifying`         | 10,494  | 9       | Q1-Q3 results per driver/race |
| `races`              | 1,125   | 18      | Full race metadata (year, round, date, circuit, etc.) |
| `results`            | 26,759  | 18      | Final classification, position, points, fastest laps |
| `seasons`            | 75      | 2       | Season year and associated URL |
| `sprint_results`     | 360     | 16      | Results for sprint qualifying races |
| `status`             | 139     | 2       | Descriptions of race result statuses (e.g. "Finished", "Accident") |

---

## 🧼 Data Quality Notes

- `lap_times` is by far the largest table and may require filtering or partial loading
- `qualifying` contains missing values, especially for older seasons with no Q2/Q3
- `status` table should be used as a lookup for statusId in `results`
- `constructor_results`, `constructor_standings`, and `driver_standings` are linked to raceId and useful for time-series and season analysis

---

## ✅ Next Steps

- Define the core joinable tables: `races`, `results`, `drivers`, `constructors`
- Identify dimension tables for reference: `circuits`, `status`, `seasons`
- Start visual exploration: number of races per year, points trends, winning constructors
