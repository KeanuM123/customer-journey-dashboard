import pandas as pd
import random
from datetime import datetime, timedelta

n_customers = 100
stages = ["Signup", "Onboarding", "Usage"]
segments = ["Free", "Premium"]
regions = ["Gauteng", "Western Cape", "KZN", "Eastern Cape"]

rows = []

for cust_id in range(1, n_customers + 1):
    base_time = datetime(2025, 6, 1) + timedelta(days=random.randint(0, 5))
    stage_count = random.choices([2, 3], weights=[0.3, 0.7])[0]
    segment = random.choice(segments)
    region = random.choice(regions)

    for i in range(stage_count):
        stage = stages[i]
        time_offset = timedelta(days=random.randint(1, 5) * i)
        timestamp = base_time + time_offset
        satisfaction_score = random.randint(4, 10)
        rows.append([cust_id, stage, timestamp, satisfaction_score, segment, region])

df = pd.DataFrame(rows, columns=["customer_id", "stage", "timestamp", "satisfaction_score", "segment", "region"])
df.to_csv("data.csv", index=False)
print("✅ data.csv with segments and regions created.")
