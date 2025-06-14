from screener import screen_stocks

if __name__ == "__main__":
    print("Running CLI Stock Screener...")
    results = screen_stocks()
    print("Top Results:")
    print(results.head())
