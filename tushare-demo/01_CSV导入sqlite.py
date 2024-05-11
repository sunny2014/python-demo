import pandas as pd  
import sqlite3

# 从CSV文件中读取数据  
df_from_csv = pd.read_csv('stock_basic_data.csv')  
# 连接到SQLite数据库  
conn = sqlite3.connect('stock_data.db')

# 将数据存入数据库中的表，如果表已存在则先删除再创建  
df_from_csv.to_sql('stock_basic_data', conn, if_exists='replace', index=False)

# 关闭数据库连接  
conn.close()