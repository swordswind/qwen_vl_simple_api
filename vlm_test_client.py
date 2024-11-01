import requests
import base64


def call_vlm_api():
    with open("demo.jpg", "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode('utf-8')
    data = {"image": f"data:image/jpeg;base64,{base64_image}", "msg": "详细描述这张图片"}
    response = requests.post("http://127.0.0.1:8086/qwen_vl", json=data)
    return response.json()


while True:
    input("按任意键开始Qwen-VL测试")
    print("测试指令已发送，等待VLM回答...")
    try:
        result = call_vlm_api()
        print(result)
    except:
        print("提示: 请先运行VLM模型API服务器，再使用客户端进行VLM测试。")
