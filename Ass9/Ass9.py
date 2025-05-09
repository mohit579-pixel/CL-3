import csv
from functools import reduce
from collections import defaultdict

def mapper(row):
    year = row["Date/Time"].split("-")[0]  
    temperature = float(row["Temp_C"])  
    return (year, temperature)

def reducer(accumulated, current):
    accumulated[current[0]][0] += current[1]
    accumulated[current[0]][1] += 1
    return accumulated

weather_data = []
with open("weather_data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        weather_data.append(row)
        
mapped_data = map(mapper, weather_data)

reduced_data = reduce(reducer, mapped_data, defaultdict(lambda: [0, 0]))

avg_temp_per_year = {year: total_temp / count for year, (total_temp, count) in reduced_data.items()}

coolest_year = min(avg_temp_per_year.items(), key=lambda x: x[1])
hottest_year = max(avg_temp_per_year.items(), key=lambda x: x[1])

print("Coolest Year:", coolest_year[0], "Average Temperature:", coolest_year[1])
print("Hottest Year:", hottest_year[0], "Average Temperature:", hottest_year[1])
