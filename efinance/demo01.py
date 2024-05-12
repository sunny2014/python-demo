import efinance as ef

# 股票代码
stock_code = '600519'  # 例如，茅台的股票代码是 600519

# 数据间隔时间为 1 分钟
freq = 1

# 获取最新一个交易日的分钟级别股票行情数据
df = ef.stock.get_quote_history(stock_code, klt=freq)

# 将数据存储到 CSV 文件中
df.to_csv(f'{stock_code}.csv', encoding='utf-8-sig', index=None)

print(f'股票: {stock_code} 的行情数据已存储到文件: {stock_code}.csv 中！')
