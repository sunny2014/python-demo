'''
   获取所有股票基本信息
   （获取基础信息数据，包括股票代码、名称、上市日期、退市日期等）

'''
import tushare as ts 
from dotenv import load_dotenv  
import os
from datetime import datetime 
  
load_dotenv()  # 默认会加载项目根目录下的.env文件  
token = os.getenv('TOKEN')  
# print(token) 
  
# 设置tushare的token，你需要在tushare网站上注册并获取token  
ts.set_token(token)  
  
# 初始化pro接口  
pro = ts.pro_api()  
  
# 获取A股列表  
data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_status,list_date')  
  
# 打印A股信息  
#print(data)
# 将数据保存为CSV文件 

# 获取当前时间并格式化为字符串  
now = datetime.now()  
timestamp = now.strftime("%Y%m%d_%H%M%S") 
# 使用时间戳创建文件名 
csv_file = f"stock_basic_data_{timestamp}.csv"
data.to_csv(csv_file, index=False) 