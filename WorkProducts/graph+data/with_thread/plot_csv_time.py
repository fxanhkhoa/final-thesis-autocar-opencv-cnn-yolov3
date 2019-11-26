# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go

# df = pd.read_csv('data.csv')
# # fig = px.line(df, x = 'current_time',
# #              y = 'frame_processing', 
# #              title='processing without multithreading')

# fig = go.Figure(go.Scatter(x = df['current_time'], y = df['frame_processing'],
#                   name='time each frame process'))

# fig.update_layout(title='processing without multithreading',
#                    plot_bgcolor='rgb(230, 230,230)',
#                    showlegend=True)

# fig.show()


import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data.csv')
# gca stands for 'get current axis'
ax = plt.gca()

df.plot(kind='line',x='current_time',y='frame_processing',ax=ax)
# df.plot(kind='line',x='name',y='num_pets', color='red', ax=ax)

plt.show()