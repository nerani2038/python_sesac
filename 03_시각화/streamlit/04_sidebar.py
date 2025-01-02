import streamlit as st 

st.title('사이드바 예제 페이지')

# Using "with" notation with st.sidebar:
add_radio = st.radio(
"Choose a shipping method",
("Standard (5-15 days)", "Express (2-5 days)")
)


st.set_page_config(page_title="홈페이지", page_icon=":sunglasses:")
st.write("안녕하세요! 이곳은 홈페이지입니다.")