from typing import List
from fastapi import APIRouter, Depends

from yf.statistics import statistics

from db.config import async_session
from db.models.fundamental import Fundamental
from db.dals.fundamental_dal import FundamentalDAL
from db.dependencies import get_fundamental_dal

router = APIRouter()

@router.get("/fundamentals/{ticker}")
async def get_fundamental(ticker: str, category: str, date: str, fundamental_dal = Depends(get_fundamental_dal)):
    shopify_stats = statistics(ticker)
    table_list = shopify_stats.scrape()
    table_list = shopify_stats.labelTables(table_list)
    print(table_list)
    
    return await fundamental_dal.get_fundamental(ticker, category, date)

    """
    convert table_list to somthing
    
    fundamental_dal = FundamentalDAL(session)
    return await fundamental_dal.update_fundamental(ticker, category, date, value)
    """
            
@router.get("/fundamentals")
async def get_all_fundamentals(fundamental_dal = Depends(get_fundamental_dal)) -> List[Fundamental]:
    return await fundamental_dal.get_all_fundamentals()
        
@router.post("/fundamentals")
async def create_fundamental(ticker: str, category: str, date: str, value: int, fundamental_dal = Depends(get_fundamental_dal)):
    return await fundamental_dal.create_book(ticker, category, date, value)
        
@router.put("/fundamentals/{ticker}")
async def create_fundamental(ticker: str, category: str, date: str, value: int, fundamental_dal = Depends(get_fundamental_dal)):
    return await fundamental_dal.update_fundamental(ticker, category, date, value)
        