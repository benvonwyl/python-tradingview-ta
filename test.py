from tradingview_ta import TA_Handler, Interval, Exchange
from colors import bcolors,colour
import sys 

SCREENER = "CRYPTO" 
EXCHANGE = "BINANCE"

SYMBOLS = sys.argv[1:len(sys.argv)]

INTERVALS = [ Interval.INTERVAL_1_MINUTE, Interval.INTERVAL_5_MINUTES, Interval.INTERVAL_15_MINUTES, Interval.INTERVAL_1_HOUR, Interval.INTERVAL_4_HOURS, Interval.INTERVAL_1_DAY, Interval.INTERVAL_1_WEEK, Interval.INTERVAL_1_MONTH]


for sym in SYMBOLS:
    for i in INTERVALS:
        crypto = TA_Handler(
            symbol=sym,
            screener= SCREENER,
            exchange=EXCHANGE,
            interval=i
        ).get_analysis()
        print(sym, i, colour(crypto.summary["RECOMMENDATION"]))
    print("")
