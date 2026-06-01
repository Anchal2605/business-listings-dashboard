import pandas as pd
import random

cities = ["Delhi", "Mumbai", "Kanpur", "Lucknow", "Noida", "Pune"]
categories = ["Restaurant", "Hospital", "School", "Gym", "Salon", "Clinic"]

data = []

for i in range(600):
    data.append({
        "business_name": f"Business {i+1}",
        "category": random.choice(categories),
        "city": random.choice(cities),
        "address": f"Address {i+1}",
        "phone": f"98{str(i).zfill(8)}",
        "source": "Google Maps"
    })

df = pd.DataFrame(data)
df.to_csv("businesses.csv", index=False)

print("600 records generated successfully!")