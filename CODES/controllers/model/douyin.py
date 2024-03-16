# ---encoding:utf-8---
# @Time    : 2024/1/13 16:43
# @Author  : stzz Wang
# @Email   ：1050100468@qq.com
# @Site    : 
# @File    : douyin.py
# @Project : douyi_analysis
# @Software: PyCharm
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(BASE_DIR)

from DrissionPage import ChromiumOptions, SessionOptions, WebPage
from CODES.config.CONFIG import *


class DouYin:
    def __init__(self):
        co = ChromiumOptions(ini_path=Config.drission_page_init_file_path)
        so = SessionOptions(ini_path=Config.drission_page_init_file_path)

        self.page = WebPage(chromium_options=co, session_or_options=so)


    def start_listen(self):
        self.page.listen.start()

    def end_listen(self):
        self.page.listen.pause(True)
        self.page.listen.stop()

    def load_page(self, url):
        self.page.get(url)

