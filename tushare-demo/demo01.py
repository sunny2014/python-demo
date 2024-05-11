import tushare as ts 
from dotenv import load_dotenv  
import os  
  
load_dotenv()  # 默认会加载项目根目录下的.env文件  
token = os.getenv('TOKEN')  
# print(token) 
  
# 设置tushare的token，你需要在tushare网站上注册并获取token  
ts.set_token(token)  
  
# 初始化pro接口  
pro = ts.pro_api()  
  
# 获取A股列表  
data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')  
  
# 打印A股信息  
print(data)