# ---encoding:utf-8---
# @Time    : 2024/1/13 16:46
# @Author  : stzz Wang
# @Email   ：1050100468@qq.com
# @Site    : 
# @File    : CONFIG.py
# @Project : douyi_analysis
# @Software: PyCharm

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)

class Config(object):
    base_dir = os.path.join(BASE_DIR, "CODES")
    drission_page_init_file_path = os.path.join(base_dir, "./config/drission_page_init")

