# import streamlit as st
# import pandas as pd

# st.title("Saylani Data Science Batch-4")


# L = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# print(L[::3])
# st.text("Pakistan zinda bad!")
# st.markdown('# _Markdown_')  # see *
# st.header('My header')
# st.subheader('My sub')
# st.code('for i in range(8): foo()')

# st.latex(r''' e^{i\pi} + 1 = 0 ''')

# df = pd.DataFrame({
#     'A': [1, 2, 3],
#     'B': [7, 8, 9]
# })

# st.dataframe(df)
# st.table(df)
# st.json({'foo': 'bar', 'fu': 'ba'})

# name = "Muhammad Qasim"

# st.text(f"My name is {name}")
# st.text(name)

# a = st.sidebar.radio('Select one:', [1, 2])

# st.header(a)

# col1, col2 = st.columns(2)
# col1.write("This is column 1")
# col2.write("This is column 2")

# col1, col2, col3 = st.columns([3, 1, 1])
# col1.write("This is column 1")
# col2.write("2")
# col3.write("Hello")

# with st.form(key='my_form'):
#     username = st.text_input('Username')
#     password = st.text_input('Password')
#     st.form_submit_button('SignIn')

# # username = st.text_input('Username')
# # password = st.text_input('Password')

# st.write(username)
# st.write(password)

# st.button('Click me')

# st.checkbox('I agree')
# st.radio('Pick one', ['cats', 'dogs'])
# st.selectbox('Pick one', ['cats', 'dogs'])
# cols = st.multiselect('Select Columns', df.columns)
# st.write(cols)
# st.data_editor(df[cols])

# st.slider('Pick a number', 0, 100)
# st.select_slider('Pick a size', ['S', 'M', 'L'])
# st.text_input('First name')
# st.number_input('Pick a number', 0, 10)
# st.text_area('Text to translate')
# st.date_input('Your birthday')
# st.time_input('Meeting time')
# st.file_uploader('Upload a CSV')
# st.download_button('Download file', data)
# st.camera_input("Take a picture")
# st.color_picker('Pick a color')


import streamlit as st
import pandas as pd
import numpy as np

x = [24.94310953459412]
y = [67.10453061184627]

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(df)
