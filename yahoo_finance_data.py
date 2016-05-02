from yahoo_finance import *

class YahooFinance:
    
    share_object = ''

    def __init__(self, symbol='YHOO'):
        self.share_object = Share(symbol)

    def get_share(self, symbol='YHOO'):
        self.share_object = Share(symbol)
        data = {}
        data['price'] = share_object.get_price()
        data['change'] = share_object.get_change()
        data['volume'] = share_object.get_volume()
        data['prevClose'] = share_object.get_prev_close()
        data['open'] = share_object.get_open()
        data['averageDailyVolume'] = share_object.get_avg_daily_volume()
        data['stockExchange'] = share_object.get_stock_exchange()
        data['marketCap'] = share_object.get_market_cap()
        data['bookValue'] = share_object.get_book_value()
        data['ebitda'] = share_object.get_ebitda()
        data['dividendShare'] = share_object.get_dividend_share()
        data['dividentYeild'] = share_object.get_dividend_yield()
        data['earningsShare'] = share_object.get_earnings_share()
        data['daysHigh'] = share_object.get_days_high()
        data['daysLow'] = share_object.get_days_low()
        data['yearHigh'] = share_object.get_year_high()
        data['yearLow'] = share_object.get_year_low()
        data['50dayMovingAverage'] = share_object.get_50day_moving_avg()
        data['200dayMovingAverage'] = share_object.get_200day_moving_avg()
        data['priceEarningsRatio'] = share_object.get_price_earnings_ratio()
        data['princeEarningGrowthRatio'] = share_object.get_price_earnings_growth_ratio()
        data['priceSales'] = share_object.get_price_sales()
        data['priceBook'] = share_object.get_price_book()
        data['shortRatio'] = share_object.get_short_ratio()
        data['tradeDateTime'] = share_object.get_trade_datetime()
        data['info'] = share_object.get_info()
        return data

    def set_symbol(self, symbol):
        self.share_object = Share(symbol)
        self.refresh_symbol()

    def refresh_symbol(self):
        self.share_object.refresh()

    def historical_data(self, start_date='2015-04-01', end_date='2015-04-30'):
        return self.share_object.get_historical(start_date, end_date)

    def set_currency(self, from_currency='USD', to_currency='ZAR'):
        symbols = "%s%s" % (from_currency, to_currency)
        #print symbols
        self.currency = Currency(symbols)
        self.refresh_currency()
        
    def refresh_currency(self):
        self.currency.refresh()

    def get_currency(self, from_currency='USD', to_currency='ZAR'):
        self.set_currency(from_currency, to_currency)
        data = {}
        data['bid'] = self.currency.get_bid()
        data['ask'] = self.currency.get_ask()
        data['rate'] = self.currency.get_rate()
        data['tradeDateTime'] = self.currency.get_trade_datetime()
        return data

    def get_rate(self, from_currency='USD', to_currency='ZAR'):
        curr = self.get_currency(from_currency, to_currency)
        return float(curr['rate'])
        
    def convert_currency(self, from_currency='USD', to_currency='ZAR', amount=100 ):
        rate = self.get_rate(from_currency, to_currency)
        conversion = rate * float(amount)
        return "%s %s" % (to_currency, ("{:.2f}".format(conversion)))

'''
USAGE
s = YahooFinance()
print s.get_rate('ZAR','USD')
print s.convert_currency('ZAR','USD', 100)
'''
