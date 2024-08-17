import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# 衡阳未来七天的天气预报数据
dates = [datetime(2024, 8, 17) + timedelta(days=i) for i in range(7)]
high_temps = [29, 30, 31, 32, 33, 32, 32]  # 最高温度
low_temps = [25, 25, 25, 25, 25, 26, 26]   # 最低温度

# 创建折线图
plt.figure(figsize=(10, 6))
plt.plot(dates, high_temps, label='最高温度', color='red')
plt.plot(dates, low_temps, label='最低温度', color='blue')

# 设置图表标题和标签
plt.title('衡阳未来七天温度预报')
plt.xlabel('日期')
plt.ylabel('温度 (°C)')
plt.xticks(dates, labels=[date.strftime("%m-%d") for date in dates])  # 日期格式化
plt.legend()

# 显示图表
plt.grid(True)
plt.show()
