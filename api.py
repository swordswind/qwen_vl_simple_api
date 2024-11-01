from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from transformers import Qwen2VLForConditionalGeneration, AutoProcessor
from qwen_vl_utils import process_vision_info
import uvicorn
import base64
from io import BytesIO
from PIL import Image

app = FastAPI()
print("正在加载Qwen-VLM模型，请稍后...")
model_dir = "model/Qwen2-VL-2B-Instruct-AWQ"
model = Qwen2VLForConditionalGeneration.from_pretrained(model_dir, device_map="cuda")
processor = AutoProcessor.from_pretrained(model_dir)


@app.post("/qwen_vl")
async def run_qwen_vl(request: Request):
    data = await request.json()
    input_image_base64 = data['image']
    msg = data['msg']
    image_data = base64.b64decode(input_image_base64.split(",")[1])
    image = Image.open(BytesIO(image_data))
    messages = [{"role": "user", "content": [{"type": "image", "image": image}, {"type": "text", "text": msg}]}]
    text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    image_inputs, video_inputs = process_vision_info(messages)
    inputs = processor(text=[text], images=image_inputs, videos=video_inputs, padding=True,
                       return_tensors="pt").to("cuda")
    generated_ids = model.generate(**inputs, max_new_tokens=128)
    generated_ids_trimmed = [out_ids[len(in_ids):] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)]
    output_text = processor.batch_decode(generated_ids_trimmed, skip_special_tokens=True,
                                         clean_up_tokenization_spaces=False)[0]
    return JSONResponse(content={"answer": output_text})

print("本地Qwen-VLM模型API服务器启动成功!")
uvicorn.run(app, host="0.0.0.0", port=8086)
