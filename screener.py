import yfinance as yf
import pandas as pd

def screen_stocks():
    tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]
    filtered_stocks = []

    for ticker in tickers:
        stock = yf.Ticker(ticker)
        info = stock.info

        try:
            pe_ratio = info.get("trailingPE", None)
            if pe_ratio and pe_ratio < 30:
                filtered_stocks.append({
                    "Symbol": ticker,
                    "PE Ratio": pe_ratio,
                    "Price": info.get("regularMarketPrice", None)
                })
        except:
            continue

    return pd.DataFrame(filtered_stocks)
