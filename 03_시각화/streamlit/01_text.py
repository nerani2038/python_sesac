import streamlit as st 

# 타이틀 적용 예시
st.title('이것은 타이틀 입니다.')

# 특수 이모티콘 삽입 예시 
# emoji: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
st.title('스마일 :sunglasses:')

# Header 적용 (마크다운 헤더 개념)
st.header('헤더를 입력할 수 있어요! :sparkles:')

# SubHeader wjrdyd
st.subheader('이것은 subheader예요')

# 캡션 적용
st.caption('캡션을 넣어 봤습니다.')

# 코드 표시
sample_code = '''
df function():
    print('hello, world')
'''
st.code(sample_code, language='python')

# 일반 텍스트
st.text('일반 텍스트를 입력해봤습니다.')

# 마크다운 문법 지원
st.markdown('streamlit은 **마크다운 문법을 지원**합니다.')

# 구분선 생성
st.divider()

# *************************************************
st.text('아래의 예제는 echo에 대한 예제입니다.')


# echo 예제
def get_user_name():
    return 'John'


# Want people to see this part of the code...

def get_punctuation():
    return '!!!'

greeting = "Hi there, "
user_name = get_user_name()
punctuation = get_punctuation()

st.write('이 윗 부분의 함수 정의부는 화면에 출력되지 않습니다.')
st.write(greeting, user_name, punctuation)

# ...up to here

foo = 'bar'
st.write('Done!')


# *************************************************
# *************************************************
st.divider()
st.write('아래 코드는 화면에 출력되는 코드입니다!')


def get_user_name():
    return 'John'

with st.echo():
    # Everything inside this block will be both printed to the screen
    # and executed.

    def get_punctuation():
        return '!!!'

    greeting = "Hi there, "
    value = get_user_name()
    punctuation = get_punctuation()

    st.write(greeting, value, punctuation)

# And now we're back to _not_ printing to the screen
foo = 'bar'
st.write('Done!')

# *************************************************
 
st.divider()

# write와 text 차이
st.text(123)
st.text({'test': 1})

st.write(123) 
st.write({'test': 1})

