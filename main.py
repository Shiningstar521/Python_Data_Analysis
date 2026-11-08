"""
主程序
"""

from config.config import RAW_DATA_FILE
from src.data_loader import load_data
# 加载原始数据集
data = load_data(RAW_DATA_FILE)