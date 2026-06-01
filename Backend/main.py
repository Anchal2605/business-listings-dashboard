from fastapi.middleware.cors import CORSMiddleware


from fastapi import FastAPI
from sqlalchemy import text
from database import engine

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Business Dashboard API Running"}

@app.get("/city-wise")
def city_wise():

    with engine.connect() as conn:

        result = conn.execute(text("""
            SELECT city, COUNT(*) as count
            FROM listing_master
            GROUP BY city
        """))

        data = []

        for row in result:
            data.append({
                "city": row.city,
                "count": row.count
            })

    return data


@app.get("/category-wise")
def category_wise():

    with engine.connect() as conn:

        result = conn.execute(text("""
            SELECT category, COUNT(*) as count
            FROM listing_master
            GROUP BY category
        """))

        data = []

        for row in result:
            data.append({
                "category": row.category,
                "count": row.count
            })

    return data


@app.get("/source-wise")
def source_wise():

    with engine.connect() as conn:

        result = conn.execute(text("""
            SELECT source, COUNT(*) as count
            FROM listing_master
            GROUP BY source
        """))

        data = []

        for row in result:
            data.append({
                "source": row.source,
                "count": row.count
            })

    return data