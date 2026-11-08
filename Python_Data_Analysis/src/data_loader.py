"""
数据读取
"""

import pandas as pd


def load_data(file_path):
    filepath = file_path
    suffix = filepath.suffix.lower()
    if not filepath.exists():
        raise FileNotFoundError(f"File {filepath} does not exist")
    if suffix == ".csv":
        data = pd.read_csv(file_path)
        print('csv数据读取成功！')
        print(f'数据规模：{data.shape[0]}行 {data.shape[1]}列')
        return data
    elif suffix in ['.xlsx', '.xls']:
        data = pd.read_excel(file_path,sheet_name=None)
        data = pd.concat(data.values(), ignore_index=True)
        print('csv数据读取成功！')
        print(f'数据规模：{data.shape[0]}行 {data.shape[1]}列')
        return data
    else:
        print('暂不支持此类文件,请使用csv、xlsx、xls文件类型的一种。')
        return None


