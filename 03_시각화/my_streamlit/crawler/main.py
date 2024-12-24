import streamlit as st
import webbrowser 

st.set_page_config(page_title="홈페이지", page_icon=":sunglasses:")
st.write("안녕하세요! 이곳은 홈페이지입니다.")

st.title('사이드바 예제 페이지')

# Using "with" notation 
with st.sidebar: # with 구문 사용 시 사이드바에 관련된 UI요소들을 묶어서 설정할 수 있음 
    # 라디오 버튼 생성 (버튼 그룹 레이블, 버튼 선택 항목)
    add_radio = st.radio(
    "Choose a shipping method",
    ("Standard (5-15 days)", "Express (2-5 days)")
    )
    clear_btn = st.button('버튼')


if add_radio == 'Express (2-5 days)':
    webbrowser.open("https://www.naver.com")

if 'test' not in st.session_state:
    st.session_state['test'] = '예제로 작성된 글입니다.'

st.write(st.session_state['test'])

if clear_btn:
    st.session_state['test'] = ''