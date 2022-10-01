

@app.get("/ticker/{ticker_id}")
async def get_ticker(ticker_id: str):
    shopify_stats = statistics(ticker_id)
    table_list = shopify_stats.scrape()
    table_list = shopify_stats.labelTables(table_list)
    #return {"message": table_list}
    if table_list:
        return {"key": "success"}