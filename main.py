from xml.etree.ElementTree import TreeBuilder
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')


# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
#     )

#st.dataframe(df.style.highlight_max(axis=0), width=1000, height=1000)
#st.table(df.style.highlight_max(axis=0))

# st.map(df)

st.write('プレグレスバーの表示')
'Start!!'


latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
'Done!!'


left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここはカラムです')

expander1 = st.expander('問い合わせ1')
expander1.write('回答1')
expander2 = st.expander('問い合わせ2')
expander2.write('回答2')
expander3 = st.expander('問い合わせ3')
expander3.write('回答3')

# text = st.sidebar.text_input('あなたの趣味を教えてください')
# condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50) #スタート,エンド, デフォルト

# 'あなたの趣味:',text
# 'コンディション:',condition


# if st.checkbox('Show Image'):
#     img = Image.open('Okada.jpg')
#     st.image(img, caption='Rio Okada', use_column_width=True)