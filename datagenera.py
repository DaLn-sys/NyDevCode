import pandas as pd
import numpy as np

# 生成样本数据
np.random.seed(0)
data_size = 36500
time = np.arange(0, data_size)
load = 50 + 10 * np.sin(time / 200) + np.random.normal(0, 1, data_size)

# 保存到CSV文件
data = pd.DataFrame({'load': load})
data.to_csv('data.csv', index=False)
