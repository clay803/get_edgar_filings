from openbb import obb

msft = obb.equity.price.historical(
    symbol='MSFT', start_date='2025-01-01', end_date= '2025-09-30'
).to_df()
print(msft)


aapl = obb.equity.search(query='AAPL', is_symbol=False, use_cache=True, provider='sec').to_df()
print(aapl)