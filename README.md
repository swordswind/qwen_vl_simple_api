# qwen_vl_simple_api

## Project Introduction

`qwen_vl_simple_api` is an API server project based on Alibaba's developed Qwen2-VL-2B AWQ quantified multimodal large model. The project aims to provide a fast and accurate image understanding and Q&A service, allowing users to integrate the multimodal large model into their applications through API calls, enabling intelligent Q&A functionality based on user-uploaded images.

## Project Address

- GitHub Project Address: [https://github.com/swordswind/qwen_vl_simple_api](https://github.com/swordswind/qwen_vl_simple_api)
- Qwen2-VL Source Address: [https://github.com/QwenLM/Qwen2-VL](https://github.com/QwenLM/Qwen2-VL)
- Qwen2-VL-2B AWQ Quantified Edition Source Address: [https://modelscope.cn/models/Qwen/Qwen2-VL-2B-Instruct-AWQ](https://modelscope.cn/models/Qwen/Qwen2-VL-2B-Instruct-AWQ)

## Hardware Requirements

Ensure that your computer has an NVIDIA graphics card installed with a memory capacity of ≥6G.

## Server Address

The API server address for the Qwen-VLM large model is: `http://your_computer_IP:8086/`

## API Interface

### Interface Address

`/qwen_vl`

### Request Method

POST

### Request Parameters

The request body content is in JSON format, including the following fields:

- `image`: Base64 encoded image data, in string format. Must include the image prefix, for example: `data:image/png;base64,`
- `msg`: The text information input by the user, in string format, which is a question about the image.

## Usage Example

Please refer to the `vlm_test_client.py` for example client code.

### Testing Method

1. Run "python vlm_test_client.py" to perform a usage test.
2. You can customize and replace the `demo.jpg` example image.

## Notes

This API server only supports the POST request method.

## Dependency Installation

Install project dependencies through the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Quick Start

1. Start the API server:

   ```bash
   python api.py
   ```

2. Test the API with a client:

   ```python
   import requests
   import base64
   
   def call_vlm_api():
       with open("demo.jpg", "rb") as image_file:
           base64_image = base64.b64encode(image_file.read()).decode('utf-8')
       data = {"image": f"data:image/jpeg;base64,{base64_image}", "msg": "Describe this picture in detail"}
       response = requests.post("http://127.0.0.1:8086/qwen_vl", json=data)
       return response.json()
   
   while True:
       input("Press any key to start Qwen-VL testing")
       print("Test command has been sent, waiting for VLM response...")
       try:
           result = call_vlm_api()
           print(result)
       except:
           print("Note: Please run the VLM model API server first, then use the client to perform VLM testing.")
   ```

## Contribution

Contributions to the project are welcome, including but not limited to:

- Code optimization
- New feature development
- Bug fixing

## License

This project is licensed under the [MIT](LICENSE) license.