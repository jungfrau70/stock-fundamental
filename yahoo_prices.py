class prices:
    
    def __init__(self, symbol, startDate, endDate):
        self.dataSource = 'yahoo'
        self.symbol = symbol.upper()
        self.startDate = startDate
        self.endDate = endDate

    def getAdjClose(self):
        try:
            dailyPrices = web.DataReader(
                self.symbol, 
                data_source = self.dataSource, 
                start = self.startDate, 
                end = self.endDate)
            dailyPrices['Ticker'] = self.symbol
            return dailyPrices[['Adj Close', 'Ticker']].reset_index()
        except: 
            print(f'Could not fetch data for {self.symbol}')
            pass