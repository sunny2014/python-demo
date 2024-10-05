from flask import Flask, request, send_file, jsonify
import redis
from io import BytesIO
from PIL import Image
import os

app = Flask(__name__)

# 初始化 Redis 连接
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)


# 从 Redis 获取图片
@app.route('/image/<image_key>', methods=['GET'])
def get_image_from_redis(image_key):
    # 从 Redis 中获取图片二进制数据
    image_data = redis_client.get(image_key)
    if image_data is None:
        return jsonify({"error": "Image not found"}), 404

    # 将图片数据转为BytesIO流并发送给客户端
    image_io = BytesIO(image_data)
    image_io.seek(0)
    
    # 使用 PIL 来检查图片类型并设置 Content-Type
    image = Image.open(image_io)
    image_format = image.format.lower()

    return send_file(BytesIO(image_data), mimetype=f'image/{image_format}')


@app.route('/get-base64image/<image_key>',methods=['GET'])  
def get_base64image(image_key):  
    # 假设你之前已经使用'image_key'这个键存储了Base64编码的图片  
    image_base64 = redis_client.get(image_key)  
    
    # 检查键是否存在以及是否成功获取到了值  
    if image_base64 is None:  
        # 如果键不存在或没有获取到值，返回404或自定义错误信息  
        return jsonify({'error': 'Image not found in Redis'}), 404  
    
    # 如果成功获取到了Base64编码的图片，将其作为响应返回  
    # 注意：Redis返回的是bytes对象，所以需要解码为str  
    return jsonify({'image_base64': image_base64.decode('utf-8')})  


if __name__ == "__main__":
    # 创建存储上传图片的目录
    if not os.path.exists('./uploads'):
        os.makedirs('./uploads')

    # 启动Flask应用
    app.run(host="0.0.0.0", port=5000, debug=True)
