from datetime import datetime
from operator import and_
from typing import List, Optional

from sqlalchemy import update
from sqlalchemy.future import select
from sqlalchemy.orm import Session

from db.models.fundamental import Fundamental

class FundamentalDAL():
    def __init__(self, db_session: Session):
        self.db_session = db_session
        
    async def create_fundamental(self, ticker: str, category: str, date: str, value: int):
        dateOJT = datetime.strptime(date, '%m/%d/%y %H:%M:%S')
        new_fundamental = Fundamental(ticker=ticker, category=category, date=dateOJT, value=1234)
        self.db_session.add(new_fundamental)
        await self.db_session.flush()

    async def get_fundamental(self, ticker: str, category: str, date: str):
        q = await self.db_session.execute(select(Fundamental)
            .where(and_(Fundamental.ticker == ticker, Fundamental.ticker == ticker, Fundamental.category == category))
            .order_by(Fundamental.ticker))
        return q.scalars().all()
    
    async def get_all_fundamentals(self) -> List[Fundamental]:
        q = await self.db_session.execute(select(Fundamental).order_by(Fundamental.ticker))
        return q.scalars().all()
    
    async def update_fundamental(self, ticker: str, category: str, date: str, value: int):
        q = update(Fundamental).where(and_(Fundamental.ticker == ticker, Fundamental.ticker == ticker, Fundamental.category == category))
        if value:
            q = q.values(value=value)
        q.execution_options(synchronize_session="fetch")
        await  self.db_session.execute(q)
        