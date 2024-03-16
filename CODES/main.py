# ---encoding:utf-8---
# @Time    : 2024/1/13 16:38
# @Author  : stzz Wang
# @Email   ：1050100468@qq.com
# @Site    : 
# @File    : main.py
# @Project : douyi_analysis
# @Software: PyCharm
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
print(BASE_DIR)
from fastapi import FastAPI
import uvicorn
from CODES.controllers.douyin_without_watermarker_analysis_controller import douyin_wwa

app = FastAPI()

app.include_router(douyin_wwa, prefix="/douyin_without_watermarker" , tags=["抖音无水印下载"])

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8080)