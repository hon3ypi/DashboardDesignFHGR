# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 16:39:14 2023

@author: wanda
"""

import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
fig.show()