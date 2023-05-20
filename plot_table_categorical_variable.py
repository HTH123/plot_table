# -*- coding: utf-8 -*-
"""
Created on Thu May 18 16:56:28 2023

绘制分类变量表格

@author: Administrator
"""

import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager
from plottable import Table, ColDef
import pandas as pd

matplotlib.use('qtagg')
plt.style.use('default')
font_manager.FontProperties(fname="C:/Windows/Fonts/msyh.ttc")
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

datatable = r'.\table_categorical_variable.xlsx'
df = pd.read_excel(datatable)
df = df.set_index('index')

columns = list(df.columns)
indexs = list(df.index)

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(16, 14))

col_def = []
for col in columns:
    col_def.append(ColDef(name=col, textprops={"ha": "center"}, border="left"))

tab = Table(
      df,
      textprops={
          'fontsize': 14,
          'fontname': 'SimHei'},
      row_divider_kw={"linewidth": 1, "linestyle": '-'},
      column_definitions= [
          ColDef(name="index", textprops={"ha": "left", "weight": "bold"})
          ] + col_def
      )

# 设置表格颜色
for i in range(len(df)):
    for j in range(len(columns) + 1):    # 计入了"index"列
        cell = tab.cells[i, j]
        content = cell.content
        if content == 'A':
            color = 'lime'
        elif content == 'B':
            color = 'cornflowerblue'
        elif content == 'C':
            color = 'yellow'
        elif content == 'D':
            color = 'red'
        else:
            color = 'white'
        cell.rectangle_patch.set_facecolor(color)

plt.show()
