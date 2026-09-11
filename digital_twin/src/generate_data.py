import csv
import json
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parents[1]
SCENARIO_FILE = PROJECT_DIR / "data" / "inputs" / "base_scenario.json"
ROUTES_FILE = PROJECT_DIR / "data" / "inputs" / "routes.csv"


with SCENARIO_FILE.open(encoding="utf-8") as file:
    scenario = json.load(file)

with ROUTES_FILE.open(encoding="utf-8", newline="") as file:
    routes = list(csv.DictReader(file))

print(f"Scenario: {scenario['scenario_name']}")
print(f"Simulation duration: {scenario['simulation_duration_hours']} hours")
print(f"Number of trucks: {scenario['fleet']['trucks']['count']}")
print(f"Number of routes: {len(routes)}")