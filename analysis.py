import ccxt, yfinance
import pandas as pd
import pandas_ta as ta

binancesucks = ccxt.binance()
bybitrocks = ccxt.bybit()

symbol = input('Instrument to inspect: ')
symbol = (symbol+'USDT').upper()

binancebars = binancesucks.fetch_ohlcv(symbol, timeframe='1m', limit=500)
bybitbars = bybitrocks.fetch_ohlcv(symbol, timeframe='1m', limit=500)


binancedf = pd.DataFrame(binancebars, columns = ['time', 'open', 'high', 'low', 'close', 'volume'])
bybitdf = pd.DataFrame(bybitbars, columns = ['time', 'open', 'high', 'low', 'close', 'volume'])

print("Binance data: ", binancedf)
print("-------------------------------")
print("Bybit data: ", bybitdf)
print("-------------------------------")

binanceadx = ta.adx(binancedf['high'], binancedf['low'], binancedf['close']) #length=10
bybitadx = ta.adx(bybitdf['high'], bybitdf['low'], bybitdf['close'])

print("-------------------------------")
print("Binance ADX data: ", binanceadx)
print("-------------------------------")
print("Bybit ADX data: ", bybitadx)