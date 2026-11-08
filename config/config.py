from pathlib import Path

# 项目根目录
BASE_DIR = Path(__file__).resolve().parent.parent

# 数据目录
DATA_DIR = BASE_DIR / "data"

# 原始数据目录
RAW_DATA_DIR = DATA_DIR / "raw"

# 处理后的数据目录
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# 原始数据文件
RAW_DATA_FILE = RAW_DATA_DIR / "online_retail_II.xlsx"

# 清洗后的数据文件
CLEAN_DATA_FILE = PROCESSED_DATA_DIR / "clean_transactions.csv"

# 图表输出目录
FIGURE_DIR = BASE_DIR / "output" / "figures"

# 图表参数
FIGURE_SIZE = (12, 6)
FIGURE_DPI = 300

# 数据分析参数
TOP_N = 10