import sqlite3  
  
try:  
    # 连接到SQLite数据库（如果数据库不存在，将会创建一个新的数据库）  
    conn = sqlite3.connect('stock_data.db')  
    cursor = conn.cursor()  

    # 先删除准备导入数据的表的旧数据 
    cursor.execute("delete from stock_basic_data_new")
    
    # 执行查询语句，使用WHERE条件过滤结果  
    query = "SELECT * FROM stock_basic_data"  
    cursor.execute(query)  
    
    # 获取查询结果  
    results = cursor.fetchall()  


    # 使用循环来插入数据  
    for record in results:  
        print(record)
      
    # 提交事务，确保数据被保存到数据库中  
    conn.commit()  
    print("数据插入成功！")  
except sqlite3.Error as error:  
    print(f"数据插入失败: {error}")  
    conn.rollback()  # 如果出现错误，回滚事务  
finally:  
    # 关闭数据库连接  
    cursor.close()  
    conn.close()  
    print("SQLite连接已关闭")

