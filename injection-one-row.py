
from models import SessionLocal, Fundamental

session = SessionLocal()
try:
    row = Fundamental(ticker="SHOP", category="ABC", date="2014-12-1", value=1234)
    session.add(row)
    session.commit()
except Exception as e:
    print(e)