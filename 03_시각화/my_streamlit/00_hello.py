import streamlit as st
import pandas as pd

# 웹 제목 설정
st.title('My Streamlit App(First)')

# 텍스트 출력
st.write('안녕하세요! streamlit입니다!')

# 데이터 프레임 만들기
data = {'name': ['Alice', 'Bob', 'Charlie'], 'age': [30, 25, 22]} 
df = pd.DataFrame(data=data)

# 데이터 츠레임 출력
st.dataframe(df)

# 막대 그래프 생성
st.bar_chart(df['age'])