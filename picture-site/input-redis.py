import redis
import base64
#import os

# 初始化 Redis 连接
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# 将图片存入 Redis
def save_image_to_redis(image_path, image_key):
    # 打开图片文件并以二进制方式读取
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()
    
    # 将图片的二进制数据存入 Redis，使用 image_key 作为键
    redis_client.set(image_key, image_data)
    print(f"Image saved in Redis with key: {image_key}")

# 将图片进行base64编码
def save_image_to_redis_encode_image(image_path, image_key):
    # 将图片文件读取为二进制数据  
    with open(image_path, 'rb') as image_file:  
        image_data = image_file.read()  
    
    # 将二进制数据转换为Base64编码的字符串  
    # 注意：在将二进制数据转换为Base64时，我们通常会得到一个bytes对象，需要将其解码为str  
    # 同时，为了能在HTML中直接使用，我们需要在Base64字符串前添加MIME类型的信息  
    image_base64 = 'data:image/jpeg;base64,' + base64.b64encode(image_data).decode('utf-8')  
    
    # 将Base64编码的字符串存储到Redis中  
    # 假设我们使用的键是'image_key'  
    redis_client.set(image_key, image_base64)  

if __name__ == "__main__":
    #print(os.getcwd())
    # 输入本地图片路径和图片的键（key）
    image_path = "picture-site/images/3gerns84av7jhw5p.jpg"
    image_key = "3gerns84av7jhw5p"

    # 将图片存入 Redis
    #save_image_to_redis(image_path, image_key)
    save_image_to_redis_encode_image(image_path, image_key)
