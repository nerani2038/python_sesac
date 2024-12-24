import pandas as pd 
import streamlit as st
# import matplotlib as plt 
import matplotlib.pyplot as plt
import seaborn as sns 

# 앱 제목 설정
st.title("첫 번째 Streamlit 앱")

# 데이터 프레임 변환
data = {'name': ['Alice', 'Bob', 'Charlie'], 'age': [30, 25, 22]} 
df = pd.DataFrame(data)

# 데이터 프레임 출력 
st.dataframe(df)

# 데이터 프레임 정렬
sorted_df = df.sort_values(by="age") 

# 데이터 프레임 집계
average_age = sorted_df["age"].mean()
st.write("") # 공백

# 정렬된 데이터 프레임 출력 
st.write('정렬된 데이터 프레임')
st.dataframe(sorted_df) # 새로변수에 담고 st. 로 표현

# 평균 연령 출력
st.write("평균 연령:", round(average_age, 4))

# 막대 그래프 생성 
plt.figure(figsize=(8, 6)) 
sns.barplot(data=df, x="name", y="age", ci=None)
# plt.bar(df["gender"], df["age"]) 
plt.xlabel("Sex") 
plt.ylabel("Age") 
plt.title("Age distribution by gender") # matplotlib으로 만든 그래프를 
st.pyplot(plt) # streamlit에 전달