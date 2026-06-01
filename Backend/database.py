from sqlalchemy import create_engine

DATABASE_URL = "mysql+pymysql://root:ANCHAL@localhost/buisness_dashboard"

engine = create_engine(DATABASE_URL)