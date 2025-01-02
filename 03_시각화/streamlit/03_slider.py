import streamlit as st
import pandas as pd 

# 슬라이더 생성
age_range = (18, 65)
selected_age = st.slider("나이 선택:", age_range[0], age_range[1])

# 선택된 값 출력
st.write("선택된 나이:", selected_age)

# 데이터 불러오기
data = {'name': ['Alice', 'Bob', 'Charlie'], 'age': [30, 25, 22]} 
df = pd.DataFrame(data)

# 조건부 실행
if  selected_age in df["age"].values:
    st.dataframe(df) 
else:
    st.write(f"{selected_age}살에 대한 데이터는 존재하지 않습니다.")


st.divider()

# 구간 선택 슬라이더 
from datetime import datetime as dt
st.slider("날짜 슬라이더", min_value = dt(2021,1,1), max_value = dt(2021,12,31), value=(dt(2021,3,1),dt(2021,4,1)))


import time

# 파일 업로드 버튼 (업로드 가능)
file = st.file_uploader('파일 선택(csv or excel)', type = ['csv', 'xls', 'xlsx'])
time.sleep(3)

# Excel or CSV 확장자를 구분하여 출력하는 경우
if file is not None:
	ext = file.name.split('.')[-1]
	if ext == 'csv':
		df = pd.read_csv(file) # 파일 읽기
		st.dataframe(df) # 출력
	elif 'xls' in ext:
		df = pd.read_excel(file, engine='openpyxl') # 엑셀 로드
		st.dataframe(df) # 출력		
