from sqlalchemy import create_engine

DATABASE_URL = "mysql+pymysql://root:ANCHAL@localhost/business_dashboard"

engine = create_engine(DATABASE_URL)