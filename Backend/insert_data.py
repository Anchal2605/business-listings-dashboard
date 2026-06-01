import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = "mysql+pymysql://root:ANCHAL@localhost/buisness_dashboard"

engine = create_engine(DATABASE_URL)

df = pd.read_csv("businesses.csv")

df.to_sql(
    name="listing_master",
    con=engine,
    if_exists="append",
    index=False
)

print(f"{len(df)} records inserted successfully!")