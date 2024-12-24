import streamlit as st
import pandas as pd

st.title('데이터프레임 튜토리얼')

# DF 생성
data = {
    'col_1': [1,2,3,4],
    'col_2': [10,20,30,40]
}
df = pd.DataFrame(data)

# 컨테이너: 화면의 일정 영역 -> 웹 브라우저 화면을 컨테이너로 사용 -> 텍스트, DF, 차트 등이 화면의 크기에 따라 위치와 크기가 조정됨
st.dataframe(df, use_container_width=True)

# interactive 한 UI를 제공하지 않음
st.table(df)

# 메트릭
st.metric(label='온도', value='10c', delta='1.2c')
st.metric(label='삼성전자', value='61,000원', delta='-1,200원')
st.metric(label='현재 사용자', value='25,000')

# 칼럼으로 영역 나누어 표기
col1, col2, col3 = st.columns(3)
col1.metric(label='온도', value='10c', delta='1.2c')
col2.metric(label='삼성전자', value='61,000원', delta='-1,200원')
col3.metric(label='현재 사용자', value='25,000')

# ------------------------------ text ------------------------------
st.title('스마일 :sunglasses:') 

st.header('헤더를 입력할 수 있습니다.')

st.subheader('서브헤더입니다.')

# 코드 표시
sample_coe = """
def function():
    print('heelo, world')
"""

st.code(sample_coe, language='python')

# text 종류
st.text('일반 문자열 지원 메서드')
st.write('파이썬의 자료형 지원 메서드')

st.text({'test': 1})
st.write({'test': 1})

st.markdown('streamlit은 **마크다운 문법을 지원**합니다.')

st.divider()