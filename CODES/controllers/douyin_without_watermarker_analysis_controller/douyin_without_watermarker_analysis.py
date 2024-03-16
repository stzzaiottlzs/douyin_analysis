# ---encoding:utf-8---
# @Time    : 2024/1/13 16:53
# @Author  : stzz Wang
# @Email   ：1050100468@qq.com
# @Site    : 
# @File    : douyin_without_watermarker_analysis.py
# @Project : douyi_analysis
# @Software: PyCharm
import os
import sys
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(BASE_DIR)

from fastapi import APIRouter
from CODES.controllers.model.douyin import *
from CODES.config.CONFIG import *
import json
from pydantic import BaseModel

douyin_wwa = APIRouter()

douyin_instance = DouYin()


class DouYinWithoutWatermarker(BaseModel):
    url: str


@douyin_wwa.post("/douyin_without_watermarker_analysis")
async def douyin_without_watermarker_analysis(accept: DouYinWithoutWatermarker):
    douyin_instance.load_page(accept.url)
    douyin_instance.start_listen()
    page = douyin_instance.page
    start_time = time.time()
    try:
        while True:
            res = page.listen.wait()  # 等待并获取一个数据包
            print(res.url)


            if "https://www.douyin.com/aweme/v1/web/aweme/post/" in res.url:
                data = json.loads(res._raw_body)
                data_list = data["aweme_list"]
                data = []
                for item in data_list:
                    d = {
                        "title" : item["desc"],
                        "urls" : item["video"]["play_addr"]["url_list"]
                    }
                    data.append(d)
                break

        use_time = time.time() - start_time
        data = {
            "data": data,
            "use_time": use_time
        }
    except Exception as e:
        data = {
            "data": e,
            "error_code": 500
        }
    finally:
        douyin_instance.end_listen()
    return data
