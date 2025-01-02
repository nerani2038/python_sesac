import streamlit as st

# CSS 스타일 적용
st.markdown("""
    <style>
        .section {
            padding: 50px 0;
            margin: 50px 0;
            border-top: 1px solid #ddd;
        }
        .sidebar-button {
            margin: 10px 0;
            background-color: #f0f0f0;
            border: none;
            padding: 10px;
            text-align: left;
            cursor: pointer;
            width: 100%;
        }
        .sidebar-button:hover {
            background-color: #ddd;
        }
    </style>
""", unsafe_allow_html=True)

# 사이드바 버튼 추가
st.sidebar.title("탐색 메뉴")
st.sidebar.markdown(
    """
    [이미지 섹션으로 이동](#이미지-섹션)  
    [그래프 섹션으로 이동](#그래프-섹션)  
    [민원 분석 섹션으로 이동](#민원-분석-섹션)
    """, unsafe_allow_html=True
)

# 콘텐츠 섹션 1: 이미지 섹션
st.markdown('<div id="이미지-섹션" class="section"></div>', unsafe_allow_html=True)
st.header("이미지 섹션")
st.image("https://via.placeholder.com/400", caption="샘플 이미지")

# 콘텐츠 섹션 2: 그래프 섹션
st.markdown('<div id="그래프-섹션" class="section"></div>', unsafe_allow_html=True)
st.header("그래프 섹션")
st.line_chart({"데이터": [1, 2, 3, 4, 5]})

# 콘텐츠 섹션 3: 민원 분석 섹션
st.markdown('<div id="민원-분석-섹션" class="section"></div>', unsafe_allow_html=True)
st.header("민원 분석 섹션")
st.bar_chart({"항목": [10, 20, 30, 40, 50]})
