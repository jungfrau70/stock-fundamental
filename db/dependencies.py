from db.config import async_session
from db.dals.fundamental_dal import FundamentalDAL

async def get_fundamental_dal():
    async with async_session() as session:
        async with session.begin():
            yield FundamentalDAL(session)